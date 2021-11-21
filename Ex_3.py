# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num_user = input('Введите число: ')
sum_user_num = num_user*2
sum_user_num_2 = num_user*3
print(num_user)
print(sum_user_num)
print(sum_user_num_2)
input_num = int(num_user)
num_2 = int(sum_user_num)
num_3 = int(sum_user_num_2)
final_num = input_num + num_2 + num_3
print(final_num)
