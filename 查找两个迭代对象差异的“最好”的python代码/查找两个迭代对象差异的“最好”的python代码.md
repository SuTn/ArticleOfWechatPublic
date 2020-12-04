# 查找两个迭代对象差异的“最好”的python代码

在日常编程中，我们经常会遇到需要寻找两个迭代对象之间差异的问题，这虽然是一个很简单的问题，只需要几行代码就可以实现，小编相信大家也都能很快写出来解决掉，但是我们写的代码真的高效吗？你是否有想过这一问题，今天小编就带大家学习下**最好**的代码。

## 01 第一代
看到这个问题，相信大家都能写出下面的代码。

```python
def difference1(x, y):
  return [i for i in x if i not in y]
```
在上面的代码中，x和y为两个可以迭代的变量，i为寻找出的存在a中但不在b中的变量值，整个代码看上去没有任何问题，合情合理，实现效果也会很好。

但是粗心的小编还是漏掉了一些问题，没有考虑变量y中的重复项，因此在第二个列表中有很多重复项的情况下，代码花费的时间比必要的更多。为了解决这个问题，可以使用set（）方法，该方法仅将唯一值保留在列表中。
## 02 第二代
在第一代的问题上，我们加入了set()函数解决了上述问题。
```python
def difference2(x, y):
    return [i for i in x if i not in set(y)]
```
等等！似乎有什么不对，这样效率真的会提高吗？但在实际的过程中，这个版本可能还不如上一个版本，因为在每次循环中，都需要对变量y进行set（）方法的操作，这样就极大的增加了运行负担，那该怎么做呢？只需要将set(y)放在外面赋值给另一个变量就可以了，相信大家都想到了。
## 03 第三代
在第二代的问题上，我们引入变量_y解决了上述问题。
```python
def difference3(x, y):
    _y = set(y)
    return [i for i in x if i not in _y]
```
到这里总算完成了吧，这不会再有问题了吧，理论上这样的。但是python中处理这类方法中，也可以使用list()和filter()这类函数,以及lambda表达式进行处理。

## 04 第四代
```python
def difference4(x, y):
    _y = set(y)
    return list(filter(lambda i :i not in _y,x))
```
其中filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。其包含两个参数filter(function, iterable)，function是判断函数，iterable是可迭代对象。在上面的代码中，通过lambda函数实现对元素的选取，再通过list转换为列表。这个方法的可读性和上面三个相比比较差，效率和第三代相差不大。

## 05 测试
为了真实比较个算法的性能，这里使用python的内置库timeit进行四种算法的测试，对比其效率，分别在小型数据和大型数据中进行了测试。关于内置库timeit的使用，在之前的文章中已经进行了详细介绍，这里不再解释。

```python

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,3,5,7,9,1,3,5]

print("difference1:")
print(timeit.timeit(stmt = "difference1(x,y)",number=1000000, globals=globals()))

print("difference2:")
print(timeit.timeit("difference2(x,y)",number=1000000, globals=globals()))

print("difference3:")
print(timeit.timeit("difference3(x,y)",number=1000000, globals=globals()))

print("difference4:")
print(timeit.timeit("difference4(x,y)",number=1000000, globals=globals()))

# difference1:
# 1.0368192999999999
# difference2:
# 3.1586304000000003
# difference3:
# 0.8646398
# difference4:
# 1.4599234999999995
```
在上面的代码中，我们可以看到代码输入的变量x,y都是较小的数据集，使用四种算法，分别测试1000000次的运行时长在可以看出，其中第三种算法最快，第一种和第四种都较快于第二种，可见set（）方法花费时间较长，对于第四种算法，由于数据量过小，其性能未能得到体现。
```python
x1 = ['阿城', '阿克苏', '阿勒泰',···]
y1 = ['阿城', '阿克苏', '阿勒泰',···]
print("difference1:")
print(timeit.timeit(stmt = "difference1(x1,y1)",number=100, globals=globals()))

print("difference2:")
print(timeit.timeit("difference2(x1,y1)",number=100, globals=globals()))

print("difference3:")
print(timeit.timeit("difference3(x1,y1)",number=100, globals=globals()))

print("difference4:")
print(timeit.timeit("difference4(x1,y1)",number=100, globals=globals()))

# difference1:
# 4.411927
# difference2:
# 19.6072971
# difference3:
# 0.02149789999999996
# difference4:
# 0.04120109999999855
```

在第二段代码中，输入变量x1，y1都是数据量很大的数据，其中x1大小为4005，y1大小1352，测试100次，从运行时间来看，可以第三种和第四种算法性能远超第一二种，第三种还是最优。

***
到这里，小编的探索就结束了，第三代和第四代算法的性能很好，不过在较小的数据集中，大家还是选用第三种算法较好。