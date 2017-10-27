import sys

def parse_ip(myString, delimiter='tofrom'):
	if delimiter == 'tofrom':
		return tofrom(myString)
	else:
		return symbol(myString, delimiter)

def tofrom(myString):
	if myString is None:
		return "Please enter an IP address."
	else:
		myList = myString.split()
		toReturn = ''
		inRange = False
		# find the Strings that represent IP addresses
		for idx, iP in enumerate(myList):
			# check if ip is in a range or independent
			if is_from(iP):
				inRange = True
			elif is_to(iP):
				toReturn += '-'
				inRange = False
			elif validateIP(iP):
				if inRange:
					toReturn += iP
				else:
					toReturn += iP + '\n'
			elif validateIP(iP) == False:
				return "The " + str(idx+1) + " word in the input is an invalid IP address."
		return toReturn


def symbol(myString, symbol):
	myList = myString.split()
	toReturn = ''
	for idx, iP in enumerate(myList):
		print("index is " + str(idx))
		if validateIP(iP):
			print("made it into the first if " + str(idx) + " " + str(len(myList)))
			if idx + 1 < len(myList):
				print("made it into the second if " + str(idx))
				if myList[idx + 1] == symbol:
					toReturn += iP + '-'
				else:
					toReturn += iP + '\n'
			else:
				toReturn += iP + '\n'
	return toReturn


def is_from(x):
	myFrom = 'from'
	possibleFrom = x.lower()
	if (myFrom == possibleFrom):
		return True
	else:
		return False

def is_to(x):
	myTo = 'to'
	possibleTo = x.lower()
	if (myTo == possibleTo):
		return True
	else:
		return False

def is_int(x):
	firstChar = x[:1]
	try:
		int (firstChar)
		return True
	except ValueError:
		return False

def validateIP(ip):
	section = ip.split('.')
	if len(section) != 4:
		return False
	for c in section:
		if len(c) > 3:
			return False
		if not c.isdigit():
			return False
		i = int(c)
		if i < 0 or i > 255:
			return False
	return True
