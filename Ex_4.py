# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

num_user = int(input("Введи целое  положительное число: "))
last = num_user % 10
print('Остаток от деления:', last)
num_user = num_user // 10
print('Результат деления:', num_user)
count = 0
while num_user > 0:
    if num_user % 10 > last:
        last = num_user % 10
        print('Новый остаток:', last)
    num_user = num_user // 10
    count += 1
print('Ответ:' ,last)
print('Пройденных циклов', count)
