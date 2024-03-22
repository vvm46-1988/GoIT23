# Map and filter

# 1
nums = [i for i in range(1, 100)]
print(nums)


sq = map(lambda x: x**2, nums)

result = filter(lambda value: bool(value % 2), sq)
print(list(result))

# 2
result = filter(lambda value: bool(value % 2), map(lambda x: x**2, [i for i in range(1, 100)]))
print(list(result))
