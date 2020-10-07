# Импортируем необходимые модули
import random as rand
from colorama import init
from colorama import Fore, Back, Style
from Modules import AnimPrint as aprint
from Modules import FastPrint as fprint


# Вывод приветствия
init()
print(Fore.BLACK)
print(Back.YELLOW)
fprint('Здравствуйте!\n')
fprint('Это программа для бросания кубиков.')
fprint('В игре 2 кубика. После броска, Вы увидите выброшенное Вами значение.')
fprint('В случае выпадения 2х одиннаковых значений - итог умножится на 2!')
fprint('Приятной игры ')


# Ввод количества игроков
print(Back.GREEN)
while True:
	try:
		NumOfPlayers = int(input('Введите количество игроков: '))
		break
	except ValueError:
		aprint('Попробуй еще раз!')
		continue


# Объявляю переменные
Dice = 0
PlayerCounter = 1
Base = {}
Score = 0
RoundList = {}
WinnerList = []


# Записываем Игроков в словарь
print(Back.CYAN)
while PlayerCounter <= NumOfPlayers:
	NickName = input('Введите имя для Игрока' + str(PlayerCounter) + ': ')
	PlayerList = {PlayerCounter : {'Name': NickName}}
	Base.update(PlayerList)
	PlayerCounter += 1


# Вводим количество раундов
print(Back.YELLOW)
while True:
	try:
		NumOfRounds = int(input('Введите количество раундов: '))
		break
	except ValueError:
		aprint('Попробуй еще раз!')
		continue
RoundList = {RoundCounter + 1 : None for RoundCounter in range(NumOfRounds)}


# Кидаем кубики и присваеваем значения игрокам
RoundCounter = 1
while RoundCounter <= NumOfRounds:
	PlayerCounter = 1
	while PlayerCounter <= NumOfPlayers:
		print(Back.GREEN)
		input('Игрок ' + Base[PlayerCounter]['Name'] + ' нажмите ENTER, что бы бросить кубики')
		print(Back.YELLOW)
		Dice1 = rand.randint(1, 6)
		Dice2 = rand.randint(1, 6)
		aprint('Выпало ' + str(Dice1) + ' и ' + str(Dice2) + '.')
		if Dice1 == Dice2:
			Score = (Dice1 + Dice2) * 2
		else:
			Score = Dice1 + Dice2
		aprint('Ваш результат: ' + str(Score) + '.')
		PlayerList = {PlayerCounter : {'Name': Base[PlayerCounter]['Name'], RoundCounter : Score}}
		Base.update(PlayerList)
		try:
			if Base[PlayerCounter][RoundCounter] == Base[PlayerCounter - 1][RoundCounter]:
				aprint('\nИгроки ' + str(Base[PlayerCounter]['Name']) + ' и ' + str(Base[PlayerCounter -1]['Name']) + ' выкинули одиннаковые значения!')
				aprint('Перебрасывайте!')
				PlayerCounter -= 1
				continue
			else:
				PlayerCounter += 1
				input('ENTER что бы продолжить!\n')
		except KeyError:
			PlayerCounter += 1
			input('ENTER что бы продолжить!\n')
	

# Добавляем игроков с СПИСОК победителей
	PlayerCounter = 1
	WinnerPos = 0
	while PlayerCounter <= NumOfPlayers:
		if WinnerPos < Base[PlayerCounter][RoundCounter]:
			WinnerPos = Base[PlayerCounter][RoundCounter]
			WinnerName = Base[PlayerCounter]['Name']
		PlayerCounter += 1
	WinnerList.append(WinnerName)
	
	
	# Победитель раунда:	
	print(Back.CYAN)
	aprint('По результатам раунда ' + str(RoundCounter) + ' победил игрок ' + str(WinnerName) + ' со счетом ' + str(WinnerPos))
	RoundCounter += 1


# Считаем кто и сколько раз победил
WinnerList.append('Control')
PlayerCounter = 1
Wins = 0
AlterWins = 0
while PlayerCounter <= NumOfPlayers:
	if WinnerList.count(Base[PlayerCounter]['Name']) > Wins:
		Wins = WinnerList.count(Base[PlayerCounter]['Name'])
		PlayerNum = PlayerCounter
	elif WinnerList.count(Base[PlayerCounter]['Name']) == Wins:
		AlterWins += 1
	PlayerCounter += 1


# Итоговый победитель или ничья
print(Back.YELLOW)
if AlterWins > 0:
	aprint('По итогам игры - НИЧЬЯ')
else:
	aprint('Игрок ' + str(Base[PlayerNum]['Name']) + ' победил по итогам игры!')


# Press ANY key
print(Back.CYAN)
input('Press ENTER to exit!')