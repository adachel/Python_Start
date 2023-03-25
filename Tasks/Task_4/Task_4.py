# Искомое число всегда является трехзначным и вторая его цифра всегда равна девяти, 
# а для получения значения последней достаточно отнять от девяти первую, 
# т.е. в рассмотренном выше случае последняя цифра равна 9-2=7.
# Задана единственная цифра К, соответствующая первой цифре искомого числа.
# Нужно вывести трехзначное чило, вторая цифра 9, последняя - разность 9 и введенного числа.

# print('Введите число до от 1 до 9')
# number = int(input())
# num_3 = 9 - number
# resalt = str(number) + '9' + str(num_3)
# print(resalt)

input_data = open('D:\Works\IT\Python_Start\Tasks\Task_4\input.txt', 'r')
number = int(input_data.read())
num_3 = 9 - number
resalt = str(number) + '9' + str(num_3)
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_4\output.txt', 'w')
output_data.write(resalt)
print(resalt)

