import timeit

def test():
    sum = 0
    for i in range(1000):
        sum+=i
    return sum

sum_string = """
sum = 0
for i in range(1000):
    sum += i
"""
# print(timeit.timeit(stmt=sum_string, number=100000))
# print(timeit.repeat(stmt=sum_string, number=100000,repeat=2))
# print(timeit.timeit("test()", setup='from __main__ import test',number=100000))

# print(timeit.repeat("test()", setup='from __main__ import test',number=100000,repeat=2))
# print(timeit.timeit(stmt = test, setup='from __main__ import test',number=100000))
print(timeit.timeit('test()',number=100000, globals=globals()))
print(timeit.timeit(test,number=100000, globals=globals()))