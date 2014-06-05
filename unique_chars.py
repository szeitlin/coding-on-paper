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
	
	n=0

	for char in word:
		if char not in charlist:
			charlist.append(char)
		elif char in charlist:
			n +=1

	print charlist

	if n>1:
		print False
	
	elif n==0:
		print True

unique_chars('appear')
unique_chars('False')

