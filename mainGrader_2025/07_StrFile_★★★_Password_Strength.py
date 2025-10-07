consecChar = "!@#$%^&*()_+qwertyuiopasdfghjklzxcvbnm"
consecAlp = "abcdefghijklmnopqrstuvwxyz"
consecNum = "01234567890123456789"
symbols = "!@#$%^&*()_+\'\""

def containMoreEightChar(passw):
	if len(passw) < 8:
		return False
	else: return True

def containUpper(passw):
	for e in passw:
		if e in consecAlp.upper():
			return True
	return False

def containLower(passw):
	for e in passw:
		if e in consecAlp.lower():
			return True
	return False

def containNumber(passw):
	for e in passw:
		if e in consecNum:
			return True
	return False

def containSymbol(passw):
	for e in passw:
		if e in symbols:
			return True
	return False

def containRep(passw):
	for i in range(0, len(passw)-3):
		if passw[i] == passw[i+1] == passw[i+2] == passw[i+3]:
			return True
		else: pass
	return False

def containConsecNum(passw):
	for i in range(0, len(passw)-3):
		checking = passw[i] + passw[i+1] + passw[i+2] + passw[i+3]
		if checking in consecNum or checking in consecNum[::-1]:
			return True
		else: pass
	return False

def containConsecAlp(passw):
	for i in range(0, len(passw)-3):
		checking = (passw[i] + passw[i+1] + passw[i+2] + passw[i+3]).lower()
		if checking in consecAlp or checking in consecAlp[::-1]:
			return True
		else: pass
	return False

def containConsecChar(passw):
	for i in range(0, len(passw)-3):
		checking = (passw[i] + passw[i+1] + passw[i+2] + passw[i+3]).lower()
		if checking in consecChar or checking in consecChar[::-1]:
			return True
		else: pass
	return False

def main():
	passw = input().strip()
	output = ""

	if not containMoreEightChar(passw): output += ("Less than 8 characters\n")
	if not containLower(passw): output += ("No lowercase letters\n")
	if not containUpper(passw): output += ("No uppercase letters\n")
	if not containNumber(passw): output += ("No numbers\n")
	if not containSymbol(passw): output += ("No symbols\n")
	if containRep(passw): output += ("Character repetition\n")
	if containConsecNum(passw): output += ("Number sequence\n")
	if containConsecAlp(passw): output += ("Letter sequence\n")
	if containConsecChar(passw): output += ("Keyboard pattern\n")
	if output == "": output += ("OK")

	print(output)
	return

if __name__ == "__main__":
	main()
