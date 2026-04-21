import numpy
n, m = map(int, input().split())
storage = []
for _ in range(n):
    row = list(map(int, input().split()))
    storage.append(row)

my_array = numpy.array(storage)
min_axis_1 = numpy.min(my_array, axis=1)
result = numpy.max(min_axis_1)
print(result)