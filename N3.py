#Реализуйте алгоритм перемешивания списка.
# Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
import random

print('Ввидите длинну списка (число)')
n = int(input())

list = [random.randint(1, 100) for i in range(n)]
print(f'Сгенерированный список {list}')
mass = []
r = random.sample(range(n), n)

for i in range(n):
    mass.append(list[r[i]])

print(f'Перемешанный список {mass}')