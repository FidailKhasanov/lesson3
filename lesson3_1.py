while True:
	comand = input('Выберите операцию: ')
	if comand in '+-/*9':
		break
	print('Ошибка ввода. Такой команды не существует. Попробуйте еще раз.')

count = 1
operand_amound = int(input('Введите количество слогаемых: '))
number = int(input(f'Введите число {count}: '))
result = number

while operand_amound != 1:
	operand_amound -= 1
	count += 1
	number = int(input(f'Введите число {count}: '))

	if number != 0:
		if comand =='-':
			result -= number
		if comand == '*':
			result *= number
		if comand == '9':
			result += 9
	result_string += " " + comand + " " + str(number)
print(result_string + " = " + str(result))
