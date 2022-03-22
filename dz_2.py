number = range(1, 1000 + 1, 2)

sum_with_17: int = 0
sum_without_17: int = 0

for el in number:
    cube = el ** 3
    cube_with_17 = (el + 17) ** 3

    if cube % 7 == 0:
        sum_without_17 += cube

    if cube_with_17 % 7 == 0:
        sum_with_17 += cube_with_17

print("сумма без 17:", sum_without_17)
print("сумма c 17:", sum_with_17)
