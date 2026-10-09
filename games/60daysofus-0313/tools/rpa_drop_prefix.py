# -*- coding: utf-8 -*-
"""Remove a path prefix from an RPA-3 archive index, in place.

Why this exists
---------------
This game ships its own Chinese translation *inside* archive.rpa, at
tl/Chinese/. Dropping our own game/tl/Chinese/*.rpy on top does not replace it:
Ren'Py collects translations from both the filesystem and the archive, so
every `translate Chinese strings:` old/new pair is registered twice and

    TranslationStringRegistry.add()
    if old in self.translations: raise Exception("A translation for ... already exists.")

fires at startup -- the game crashes before the menu. The only way to make ours
the only copy is to delete the archived one, and the retail build ships no
`archive` subcommand to do that.

How it stays cheap
----------------
It never rewrites asset data. The new index is appended at the end of the file
and the 34-byte header is patched in place with the new index offset; every
surviving entry keeps the offset it already had. On this game that is 2.5 GB
of images and audio that are not touched, not copied, not re-compressed.
Cost is O(index size), a few hundred KB.

Usage
-----
    python rpa_drop_prefix.py <archive.rpa> --drop tl/Chinese/           # dry run
    python rpa_drop_prefix.py <archive.rpa> --drop tl/Chinese/ --apply   # writes

The dry run is the default and it is the one the installer does first: it prints
what would go and refuses to touch anything. --apply takes a backup unless
--no-backup is given, and afterwards re-reads the archive the way Ren'Py does
and fails loudly if anything does not add up.
"""
import argparse
import hashlib
import os
import pickle
import random
import shutil
import sys
import zlib

MAGIC = b"RPA-3.0 "
HEADER = 40


def read_header(fh):
    head = fh.read(HEADER)
    if head[:8] != MAGIC:
        raise SystemExit("not an RPA-3 archive: %r" % head[:8])
    return {
        "raw": head,
        "index_offset": int(head[8:24], 16),
        "key": int(head[25:33], 16),
    }


def read_index(fh, index_offset, key):
    fh.seek(index_offset)
    raw = pickle.loads(zlib.decompress(fh.read()))
    out = {}
    for name, entries in raw.items():
        plain = []
        for off, length, prefix in entries:
            plain.append((off ^ key, length ^ key,
                          prefix if isinstance(prefix, bytes) else str(prefix).encode("latin-1")))
        out[name] = plain
    return out


def write_index(index, key):
    obf = {k: [(o ^ key, d ^ key, s) for o, d, s in v] for k, v in index.items()}
    return zlib.compress(pickle.dumps(obf, pickle.HIGHEST_PROTOCOL), 9)


def obfuscate_header(head, new_offset, key):
    # same byte length as the original, so nothing downstream shifts
    return head[:8] + ("%016x" % new_offset).encode() + head[24:25] + ("%08x" % key).encode() + head[33:]


def spot_check(path, index, key, n=12, seed=20261009):
    """Decompress a few surviving entries and confirm they look like data."""
    picked = sorted(index)
    rnd = random.Random(seed)
    rnd.shuffle(picked)
    checked = 0
    with open(path, "rb") as fh:
        for name in picked:
            off, length, prefix = index[name][0]
            fh.seek(off)
            try:
                blob = zlib.decompress(fh.read(length))
            except zlib.error:
                raise SystemExit("entry %s failed to decompress -- archive is damaged" % name)
            if prefix:
                if not blob.startswith(prefix):
                    raise SystemExit("entry %s does not start with its stored prefix" % name)
            checked += 1
            print("   ok %-46s %9d bytes" % (name, len(blob)))
            if checked >= n:
                break
    return checked


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("archive")
    ap.add_argument("--drop", required=True, action="append",
                    help="path prefix to remove; repeatable")
    ap.add_argument("--apply", action="store_true", help="actually write (default is a dry run)")
    ap.add_argument("--no-backup", action="store_true")
    ap.add_argument("--verify", type=int, default=12, help="how many surviving entries to spot-check")
    args = ap.parse_args(argv)

    path = args.archive
    size = os.path.getsize(path)
    with open(path, "rb") as fh:
        head = read_header(fh)
        key = head["key"]
        index = read_index(fh, head["index_offset"], key)

    dropped = sorted(k for k in index
                     if any(k.startswith(p) for p in args.drop))
    kept = {k: v for k, v in index.items()
            if not any(k.startswith(p) for p in args.drop)}

    print("archive      %s" % path)
    print("size         %s bytes" % format(size, ","))
    print("index at     0x%x   key 0x%08x" % (head["index_offset"], key))
    print("entries      %d" % len(index))
    print("dropping     %d entr%s matching %s" %
          (len(dropped), "y" if len(dropped) == 1 else "ies", ", ".join(args.drop)))
    for name in dropped:
        print("   - %s" % name)
    print("keeping      %d" % len(kept))

    if not dropped:
        print("\nalready clean -- nothing to remove, nothing written")
        return 0

    blob = write_index(kept, key)
    print("new index    %s bytes, appended at %s" % (format(len(blob), ","), format(size, ",")))

    # round-trip before touching anything
    back = pickle.loads(zlib.decompress(blob))
    back = {k: [(o ^ key, d ^ key, s) for o, d, s in v] for k, v in back.items()}
    if back != kept:
        raise SystemExit("index round-trip mismatch -- refusing to write")
    if any(any(k.startswith(p) for p in args.drop) for k in back):
        raise SystemExit("prefix still present after rebuild -- refusing to write")
    print("round-trip   OK")

    if not args.apply:
        print("\ndry run. nothing was written. re-run with --apply to do it.")
        return 0

    if not args.no_backup:
        bak = path + ".pre-l10n"
        if not os.path.exists(bak):
            print("\nbackup       %s" % bak)
            shutil.copy2(path, bak)
        else:
            print("\nbackup       %s already there, keeping it" % bak)

    with open(path, "r+b") as fh:
        fh.seek(0)
        fh.write(obfuscate_header(head["raw"], size, key))
        fh.seek(size)
        fh.write(blob)
        fh.flush()
        os.fsync(fh.fileno())

    after = os.path.getsize(path)
    print("size         %s -> %s (+%s)" %
          (format(size, ","), format(after, ","), format(after - size, ",")))

    # verify exactly the way Ren'Py reads it
    with open(path, "rb") as fh:
        h2 = read_header(fh)
        i2 = read_index(fh, h2["index_offset"], h2["key"])
    if len(i2) != len(kept):
        raise SystemExit("re-read %d entries, expected %d" % (len(i2), len(kept)))
    if [k for k in i2 if any(k.startswith(p) for p in args.drop)]:
        raise SystemExit("prefix still present after write")
    print("\nre-read      %d entries, prefix gone" % len(i2))
    spot_check(path, i2, h2["key"], args.verify)
    print("\nOK. the archived copies are gone; the files dropped into game/tl/ "
          "are now the only ones the loader sees.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
