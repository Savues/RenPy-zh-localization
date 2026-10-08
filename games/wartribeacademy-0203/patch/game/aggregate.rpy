init -800 python:
    ''' 
    版权所有 (C) 2021-2022 由 3 Pood Productions 制作

    特此免费授予任何获得本软件
    及其相关文档文件（"本软件"）副本的人许可，
    可在不受限制的情况下
    使用、复制、修改、合并、发布、分发、再许可和/或出售
    本软件的副本，并允许获得本软件的人
    从事上述操作，但须遵守以下条件：

    上述版权声明及本许可声明
    应包含在本软件的所有副本或实质性部分中。

    本软件按"现状"提供，不附带任何明示或默示的担保，
    包括但不限于对适销性及特定用途适用性的默示保证。
    在任何情况下，作者或版权持有人
    均不对任何索赔、损害或其他
    责任负责，无论其因合同、侵权
    还是其他原因引起，也不论是否
    与本软件的使用或其他行为有关。
'''

    # This aggregates many conditions mapping them to a score, and then
    # adding the total value of all of those that are True
    @unpickleable
    class ScoreAggregate(object):
        def __init__(self, **scores):
            self.scores = dict(**scores)

        def __repr__(self):
            return str(int(self))

        def __int__(self):
            total = 0
            for flag, score in self.scores.items():
                value = True
                if isinstance(flag, basestring):
                    value = globals()[flag]
                total += int(score) if value != None and bool(value) else 0
            return total

        def __add__(self, other):
            return int(self) + int(other)
        def __radd__(self, other):
            return int(self) + int(other)
        def __sub__(self, other):
            return int(self) - int(other)
        def __rsub__(self, other):
            return int(other) - int(self)
        def __eq__(self, other):
            return int(self) == int(other)
        def __ne__(self, other):
            return int(self) != int(other)
        def __gt__(self, other):
            return int(self) > int(other)
        def __ge__(self, other):
            return int(self) >= int(other)
        def __lt__(self, other):
            return int(self) < int(other)
        def __le__(self, other):
            return int(self) <= int(other)

    # This aggregates many items that can be converted to values, and then
    # returns the total of all of them
    class SumAggregate(ScoreAggregate):
        def __init__(self, *values):
            d = {}
            for i, v in enumerate(values):
                d[i] = v
            super(SumAggregate, self).__init__(**d)

    # This aggregates many conditions, and returns the count of them
    # that return True at the time it is evaluated
    class CountAggregate(ScoreAggregate):
        def __init__(self, *flags):
            d = {}
            for f in flags:
                d[f] = 1
            super(CountAggregate, self).__init__(**d)

    # This aggregates many conditions, and returns True only if
    # every single condition it has return True
    class AndAggregate(CountAggregate):
        def __init__(self, *flags):
            super(AndAggregate, self).__init__(*flags)

        def __bool__(self):
            count = int(self)
            return count == len(self.scores)

        def __nonzero__(self):
            return self.__bool__()

        def __repr__(self):
            return str(bool(self))

    # This aggregates many conditions, and returns True only if
    # there exists at least one condition it has that returns True
    class OrAggregate(CountAggregate):
        def __init__(self, *flags):
            super(OrAggregate, self).__init__(*flags)

        def __bool__(self):
            count = int(self)
            return count > 0

        def __nonzero__(self):
            return self.__bool__()

        def __repr__(self):
            return str(bool(self))

    # This aggregates many conditions, and returns True only if
    # there exists exactly one condition it has that returns True
    class XorAggregate(CountAggregate):
        def __init__(self, *flags):
            super(OrAggregate, self).__init__(*flags)

        def __bool__(self):
            count = int(self)
            return count == 1

        def __nonzero__(self):
            return self.__bool__()

        def __repr__(self):
            return str(bool(self))
            
    # This aggregates many conditions mapping them to a score, and then
    # adding the total value of all of those that are True
    # Figures what the maximum score would be and allows getting a percentage
    # NOTE: Does not account for negative scores, so do not include them
    class CappedScoreAggregate(ScoreAggregate):
        def __init__(self, **scores):
            super(CappedScoreAggregate, self).__init__(**scores)
            self.max = float(sum(self.scores.values()))

        def getPercentage(self):
            return int(self) / self.max
            
        def __str__(self):
            return "{}%".format(100.0 * self.getPercentage())  

    _condition_cache = {}
    # This allows you to pass in any code expression as a string
    # and evaluate it like a boolean. 
    @unpickleable
    class ComplexFlag(object):
        def __init__(self, expression):
            global _condition_cache
            if expression not in _condition_cache:
                code = renpy.python.py_compile(expression, 'eval')
                _condition_cache[expression] = code
            self.code = _condition_cache[expression]

        def __repr__(self):
            return str(self)

        def __str__(self):
            return str(bool(self))

        def __bool__(self):
            return bool(renpy.python.py_eval_bytecode(self.code))

        def __nonzero__(self):
            return self.__bool__()  
    
    @unpickleable
    class ConstValue(object):
        def __init__(self, val):
            self._value = val

        def __str__(self):
            return str(self._value)
            
        @property
        def value(self):
            return self._value


    @unpickleable
    class ConditionSelectValue(object):
        def __init__(self, *args):
            self.values = []
            self.append(*args)

        def __str__(self):
            return str(self.value)

        def __getitem__(self, i):
            return self.value[i]

        def __getattr__(self, k):
            return getattr(self.value, k)

        def __bool__(self):
            return bool(self.value)

        def __nonzero__(self):
            return self.__bool__()  

        def append(self, *args):
            global _condition_cache
            if len(args) % 2 != 0:
                raise Exception("ConditionSelect takes an even number of arguments")

            for condition, val in zip(args[0::2], args[1::2]):
                if condition not in _condition_cache:
                    code = renpy.python.py_compile(condition, 'eval')
                    _condition_cache[condition] = code
                self.values.append((condition, val))

        @property
        def value(self):
            global _condition_cache
            for condition, val in reversed(self.values):
                if renpy.python.py_eval_bytecode(_condition_cache[condition]):
                    return val
            raise Exception("No valid conditions!")
            return None

        def dump(self):
            for condition, val in self.values:
                print("{} if {} ({})", val, self.cond,
                renpy.python.py_eval_bytecode(_condition_cache[condition]))

    @unpickleable
    class OrderedSelectValue(object):
        def __init__(self, func, default, *args):
            if not callable(func):
                raise Exception("func argument needs to be callable")
            self.func = func
            self.def_val = default
            self.values = []
            if len(args) % 2 != 0:
                raise Exception("PrioritySelect takes an even number of arguments")
            for test_value, val in zip(args[0::2], args[1::2]):
                self.values.append((test_value, val))

        def __str__(self):
            return str(self.value)

        def __getitem__(self, i):
            return self.value[i]

        def __getattr__(self, k):
            return getattr(self.value, k)

        def __bool__(self):
            return bool(self.value)

        def __nonzero__(self):
            return self.__bool__()  

        @property
        def value(self):
            rv = max(self.values, key=self.func)
            if self.func(rv) == -1:
                return self.def_val
            return rv[1]

        def dump(self):
            for key, val in self.values:
                print("{} for {} ({})", val, key, self.func(key))

    class ConditionColor(Color):
        def __new__(cls, *args):
            return super(ConditionColor, cls).__new__(cls)

        def __init__(self, *args):
            self.values = []
            self.append(*args)

        def __str__(self):
            return str(self.value)

        def __getitem__(self, i):
            return self.value[i]

        def __getattr__(self, k):
            return getattr(self.value, k)

        def append(self, *args):
            global _condition_cache
            if len(args) % 2 != 0:
                raise Exception("ConditionSelect takes an even number of arguments")

            for condition, val in zip(args[0::2], args[1::2]):
                if condition not in _condition_cache:
                    code = renpy.python.py_compile(condition, 'eval')
                    _condition_cache[condition] = code
                self.values.append((condition, val))

        @property
        def value(self):
            global _condition_cache
            for condition, val in reversed(self.values):
                if renpy.python.py_eval_bytecode(_condition_cache[condition]):
                    return val
            raise Exception("No valid conditions!")
            return None

        def dump(self):
            for condition, val in self.values:
                print("{} if {} ({})", val, self.cond,
                renpy.python.py_eval_bytecode(_condition_cache[condition]))