from functools import reduce
nums = input("Enter the numbers\n").split()
l = list(map(int, nums))
#print(l)
res = reduce(lambda x, y : x + y, l)
#print(res)
avg = res / len(l)
print("{0:.4f}".format(avg))
print("{0:^14.4f}".format(avg))
