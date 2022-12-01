#Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.

print('Введи число ')
n = int(input())
summa = 0
while n > 0:
    symbol = n % 10
    summa = summa + symbol
    n = n // 10

print(summa)