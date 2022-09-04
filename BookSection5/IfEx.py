# 5-1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')

# 5-2 conditional_tests
test0 = 'string'
if test0 == 'string':
    print('pass')
else:
    print('false')

test1 = "BMW"
if test1.lower() == 'bmw':
    print('pass')
else:
    print('false')

test2 = 10
if test2 == 10:
    print('pass')
else:
    print('false')
if test2 != 10:
    print('pass')
else:
    print('false')
if test2 <= 10:
    print('pass')
else:
    print('false')
if test2 < 10:
    print('pass')
else:
    print('false')

test3 = 10
if test3 == 10 or test3 != 10:
    print('pass')
else:
    print('false')

if test3 == 10 and test3 != 10:
    print('pass')
else:
    print('false')

elements = ['line', 'micro', 'lean']
result = 'line' in elements
print(result)
result2 = '123' in elements
print(result2)
