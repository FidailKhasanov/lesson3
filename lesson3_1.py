while True:
	comand = input('Выберите операцию: ')
	if comand in '+-/*9':
		break
	print('Ошибка ввода. Такой команды не существует. Попробуйте еще раз.')

count = 1
operand_amound = int(input('Введите количество операндов: '))
number = int(input(f'Введите число {count}: '))
result = number
result_string = str(number)

while operand_amound != 1:
	operand_amound -= 1
	count += 1
	number = int(input(f'Введите число {count}: '))

	if number != 0:
		if comand =='-':
			result -= number
		if comand == '*':
			result *= number
		if comand == '+':
			result += number
	result_string += " " + comand + " " + str(number)
print(result_string + " = " + str(result))
