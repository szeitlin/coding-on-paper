#practice writing code on paper

def unique_chars(word):
	''' string -> bool
	
	Compares the characters in a string to determine if any appear more than once.

	>>>unique_chars(appear)
	False
	>>>unique_chars(False)
	True

	precondition: len(word) >1
	'''
	charlist = []
	
	flag = True

	for char in word:
		if char not in charlist:
			charlist.append(char)
		elif char in charlist:
			flag = False

	print charlist

	print flag

unique_chars('appear')
unique_chars('False')

