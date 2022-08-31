# 4-3
# for value in range(1, 21):
#     print(value)

# 4-4 / 4-5
numbers = list(range(1, 1000001))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6
for value1 in range(1, 21, 3):
    print(value1)

# 4-7
for value2 in range(3, 30, 3):
    print(value2)

# 4-8
for value3 in range(1, 11):
    cube = value3 ** 3
    print(cube)

# 4-9
cubes = [value4 ** 3 for value4 in range(1,11)]
print(cubes)