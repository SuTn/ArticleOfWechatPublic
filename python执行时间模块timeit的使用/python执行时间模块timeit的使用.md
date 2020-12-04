# python执行时间模块timeit的使用
在日常工作中，总会遇到代码优化的问题，以提高代码运行的**效率**，一般都是在代码前后定义时间差进行衡量，今天小编就向大家介绍python中内置的timeit模块，**一行**实现对代码运行时间的测量，让我们一起来看看吧！
![](pic/fengmian.jpg)
## 01 timeit库概述
timeit库是python中一个测量 Python 脚本执行效率，时间的模块，是 Python 标准库中的模块，无需安装，直接导入就可以使用。timeit模块总共源码只有300多行，有兴趣的同学可以看看源码，使用起来十分简单。

```python
import timeit
```
## 02 timeit库方法介绍
在timeit模块中总共包含了三个函数：timeit.timeit(),timeit.repeat(),timeit.default_timer(),下面小编将对这三个函数进行逐一介绍。
### a. timeit.timeit
```
timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)
```

- stmt 这个参数就是statement,是指要执行的代码段。
- setup 执行代码的准备工作,初始化代码或构建环境导入语句,不计入时间，一般是import之类的。
- timer 计时器，在不同的环境下不同，为默认参数，不用管。
- number 代码段（stmt)要执行的次数。
- 返回值：返回执行代码所需要的时间，即执行stmt代码段number次所花费的时间。
- globals 可以指定globals=globals()，表明代码在当前的全局命名空间中执行。
__该模块中最常用的函数，用来测量某段程序所花费的时间。__
### b. timeit.repeat
```
timeit.repeat(stmt='pass', setup='pass', timer=<default timer>, repeat=5, number=1000000, globals=None)
```

- stmt 这个参数就是statement,是指要执行的代码段。
- setup 执行代码的准备工作,初始化代码或构建环境导入语句,不计入时间，一般是import之类的。
- timer 计时器，在不同的环境下不同，为默认参数，不用管。
- repeat 代码段（stmt*number）执行的大循环的次数，表明多测实验，默认值为5
- number 代码段（stmt)要执行的次数。
- globals 可以指定globals=globals()，表明代码在当前的全局命名空间中执行。
- 返回值： 返回执行代码所需要的时间列表，即执行stmt代码段number次所花费的时间列表，列表大小为repeat。
__该函数经常用来被做多次实验求平均值。__

### c.  timeit.default_timer
此为默认的计时器，默认为timeit.perf_counter()。

## 03 timeit库使用示例
为了方便大家使用，这里就用例子对timeit的不同使用方法进行讲解。

这里以求解重1到1000的和的问题为例，求解次数为100000次，进行示例演示。
### a 将测试的代码直接包含在字符串
```python
sum_string = """
sum = 0
for i in range(1000):
    sum += i
"""
print(timeit.timeit(stmt=sum_string, number=100000))
print(timeit.repeat(stmt=sum_string, number=100000,repeat=2))
# 4.1959263
# [4.2018374000000005, 4.321623999999999]
```
在上面的代码中，将要测试的代码包含在字符串中赋值给stmt，运行次数设置为100000，输出测试代码的时长，在timeit.repeat中，将repeat设置为2，可见其输出为大小为2的列表，表明两次测试的结果。

### b 测试代码封装在方法中

```python
def test():
    sum = 0
    for i in range(1000):
        sum+=i
    return sum

print(timeit.timeit("test()", setup='from __main__ import test',number=100000))
print(timeit.timeit(stmt = test, setup='from __main__ import test',number=100000))
print(timeit.repeat("test()", setup='from __main__ import test',number=100000,repeat=2))
# 4.2138227
# 4.2212262
# [4.2065454, 4.2259149]
```
如果想要直接在stmt处调用函数，只需要将函数申明在当前文件下，令 stmt = ‘func()’ 执行函数。然后使用 setup = ‘from __ main __ import func’ 即可，在上面的代码中，显示了调用timeit.timeit和timeit.repeat的操作。另外，还可以将 stmt = ‘func()’ 替换为 stmt=func,也可以达到相同的人运算结果。

### c 使用globals全局变量
```python
def test():
    sum = 0
    for i in range(1000):
        sum+=i
    return sum
print(timeit.timeit('test()',number=100000, globals=globals()))
print(timeit.timeit(test,number=100000, globals=globals()))
```
将测试代码封装在方法中时，也可使用globals=globals()，使得不需要使用setup参数（setup='from __main__ import test'）单独指定，直接在全局空间中运行。

***
到这里，小编的介绍就完成了，大家快快使用起来吧！