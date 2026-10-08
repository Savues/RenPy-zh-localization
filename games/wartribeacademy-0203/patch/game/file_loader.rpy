define config.images_directory = None

init -10 python:
    import os
    class GameFileManager(object):
        def __init__(self, ignored_roots={'gui', 'saves', 'tl', 'cache'}, ignored_exts={'.rpy', '.rpyc', '.py'}):
            self._file_handlers_root_index = {} # dict of lists of ext/handler pairs
            self._file_handlers_extension_index = {} # dict of ext/handler pairs
            self._file_handler_default = None # file handler to use on files that don't match
                                        # any roots, exts, and are not explicitly ignored

            self._file_handlers_to_files = {}
            self._file_handlers_ordered = []

            self._all_reg_roots = set()
            self._all_reg_exts = set()

            self._ignored_roots = ignored_roots
            self._ignored_exts = ignored_exts

        # static helper function for file handlers to parse options
        @staticmethod
        def parse_file_opts(file):
            opts = file.split('.')
            opt_vals = {}
            for opt in opts[1:-1]: # first is main name, last is extension
                o, _, val = opt.partition('#')
                opt_vals[o.lower()] = (val and val.lower()) or False
            return opts[0].lower(), opt_vals, opts[-1].lower()

        def register_file_handler(self, callback, root_folders=None, extensions=None, priority=0):
            self._file_handlers_to_files[callback] = []
            self._file_handlers_ordered.append((callback, priority))

            if isinstance(root_folders, (str, unicode)):
                root_folders = [root_folders]
            if isinstance(extensions, (str, unicode)):
                extensions = [extensions]
            handler = (callback, root_folders, extensions)

            if root_folders:
                self._all_reg_roots.update(root_folders)
                for root_folder in root_folders:
                    if root_folder not in self._file_handlers_root_index:
                        self._file_handlers_root_index[root_folder] = []
                    self._file_handlers_root_index[root_folder].append(handler)
            if extensions:
                self._all_reg_exts.update(extensions)
                for ext in extensions:
                    self._file_handlers_extension_index[ext] = handler
            else:
                self._file_handler_default = callback

        def match_file_to_handler(self, f, fext, sorted_roots):
            # Phase one, handlers that act on root paths
            for rt in sorted_roots:
                if not f.startswith(rt):
                    continue
                lst = self._file_handlers_root_index[rt]
                for hnd in lst:
                    if not hnd[2]: # no extensions defined for this handler
                        self._file_handlers_to_files[hnd[0]].append((f, f.partition(rt)[2][1:]))
                        return
                    if fext in hnd[2]:
                        self._file_handlers_to_files[hnd[0]].append((f, f.partition(rt)[2][1:]))
                        return
            # Phase two, handlers that act globally based on extension
            if fext in self._file_handlers_extension_index:
                hnd = self._file_handlers_extension_index[fext]
                self._file_handlers_to_files[hnd[0]].append(f)
                return
            
            # Phase three, a single global handler for all files not covered by the others
            # and not in the ignored root or extension list
            if self._file_handler_default:
                self._file_handlers_to_files[self._file_handler_default].append(f)

        def scan_handlers(self):
            # test root paths from most specific to least
            sorted_roots = sorted(self._all_reg_roots, reverse=True)
            for _, f in renpy.loader.listdirfiles(False):
                path, ext = os.path.splitext(f)
                for root in self._ignored_roots:
                    if f.startswith(root):
                        ext = False # cheap cancel
                        break
                if not ext or ext in self._ignored_exts:
                    continue
                if not self._file_handler_default and ext not in self._all_reg_exts:
                    continue
                else:
                    self.match_file_to_handler(f, ext, sorted_roots)

        def run_handlers(self):
            sorted_handlers = sorted(self._file_handlers_ordered, key=lambda hnd: hnd[1])
            for hnd, _ in sorted_handlers:
                file_list = self._file_handlers_to_files[hnd]
                for file in file_list:
                    # if we got this by matching a root folder, we pass in the sub folders
                    # for convenience. Might be empty, will need to be handled
                    subd = None
                    if isinstance(file, tuple): 
                        file, subd = file
                    head, tail = os.path.split(file)
                    hnd(tail, head, file, (subd and subd.partition(tail)[0]))



    def reg_movies(file, folder, full_path, subd):
        name, opts, ext = GameFileManager.parse_file_opts(file)
        img = None
        if 'i' in opts:
            img = opts['i'] or name + '_still'
        renpy.image(name, Movie(play=full_path, loop=('noloop' not in opts), image=img))
        
    def reg_normal_images(file, folder, full_path, subd):
        opts = file.split('.')
        renpy.image(opts[0].lower(), Image(full_path))

    game_files_mgr = GameFileManager()
    game_files_mgr.register_file_handler(reg_movies, priority=10, root_folders='images', extensions='.webm')
    game_files_mgr.register_file_handler(reg_normal_images, root_folders='images', extensions=('.webp', '.png'))

init 10 python:
    game_files_mgr.scan_handlers()
    game_files_mgr.run_handlers()


