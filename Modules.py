import time


def StrToList (NameSym):
	NameSym = list(NameSym)
	Search = []
	NameSym.append('iTech')
	Counter = 0
	Keyword = ""
	Lenth = NameSym.index('iTech')
	ExcList = [' ', ',']


	for Counter in range(Lenth):
		if NameSym[Counter] in ExcList:
			if Keyword != "":
				Search.append(Keyword)
			Keyword = ""
		else:
			Keyword += NameSym[Counter]
		Counter += 1
	if Keyword != "":
		Search.append(Keyword)
	return Search


def AnimPrint (text):
	for i in text:
		print(i, end = '', flush=True)
		time.sleep(0.1)
	print('\n', end = '')


def FastPrint (text):
	for i in text:
		print(i, end = '', flush=True)
		time.sleep(0.04)
	print('\n', end = '')


def GreetingPrint (text):
	print(text)
	time.sleep(0.15)