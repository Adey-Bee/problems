f = open("passwords.txt", "r")
#password = f.readlines()


def chkgid(password):
	for letters in password:
		if letters.isdigit():
			if len(letters.isdigit) >= 4:
				return True
        

def chkupc(password):
	for letters in password:
		if letters.isupper():
			if len(letters.isupper) >= 4:
			    return True
			
		
def chklwc(password):
	for letters in password:
		if letters.islower():
			if len(letters.islower) >= 2:
			    return True
			

def acptpswd(password):
	x = 0
	for value in password:
		dg = chkgid(password)
		lw = chklwc(password)
		up = chkupc(password)
		
		if dg == True:
			if lw == True:
				if up == True:
				    x = x + 1
	print x
acptpswd(f)