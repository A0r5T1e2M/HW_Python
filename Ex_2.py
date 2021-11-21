# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

import math

sek = int(input('Введите время в секундах: '))
# min = 1min = 60sek
# hour = 1hour = 60min = 3600sek
minute = math.trunc(sek/60)
hour = math.trunc(sek/3600)
if minute < 1:
    minute = 0
if hour < 1:
    hour = 0
print('Время:', f'Часов {hour} Минут {minute} Секунд {sek}')
