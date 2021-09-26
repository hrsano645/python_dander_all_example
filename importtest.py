from module_1 import *

m1_func1
_m1_func2
m1_func3
_m2_func4 

m1_class1
m1_class2

from module_2 import *

# __all__ = ["m2_func1", "m2_class2", "_m2_func4"]

m2_func1
_m2_func2 # importできない
m2_func3 # importできない
_m2_func4 # __all__に明示的に入れてあるとimportできる

m2_class1 # importできない
m2_class2


