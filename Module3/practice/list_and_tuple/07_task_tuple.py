# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

# Вариант 1
# big_number = max(tup)
# print(big_number)
# Вариант 2

big_number = 0
for number in tup:
    if big_number <= number:
        big_number = number
print(big_number)

