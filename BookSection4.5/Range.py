# for value in range(1, 10):
#     print(value)
# print(f'\n')
# for value2 in range(5):
#     print(value2)

# ------------------------------

# numbers = list(range(10))
# print(numbers)
#
# parni_num = list(range(2, 20, 2)) # Берет каждое второе число, если указать 1 будет не парное число
# print(parni_num)

# ------------------------------

# squares = []  # Степень чисел
# for value3 in range(1, 11):
#     square = value3 ** 2
#     squares.append(square)  # Апенд добавляет новое значение в список без изменения
#
# print(squares)
#
# print(min(squares))
# print(max(squares))
# print(sum(squares))

# # Генераторный список ниже, это тот же самый код что выше, но в одну строку
# squares = [value ** 2 for value in range(1, 11)]
# print(squares)
