#given 2 strings, decide if one is a permutation of the other. 

def is_permut(word1, word2):
	''' 2 strings -> bool

	Compares 2 strings to determine whether the second is a permutation
	of the first. 
	Criteria: 
	same length
	different order of letters (special case if words are identical)
	same letters

	>>>is_permut('on', 'no')
	True
	>>>is_permut('tile', 'elite')
	False
	'''

	flag = True

	if word1 == word2:
		flag = False
		print flag

	elif len(word1) != len(word2):
		flag = False
		print flag

	else:
		charlist = []
		for char in word1:
			charlist.append(char)
		for char in word2:
			if char not in charlist:
				flag = False
				print flag

			
		print flag

is_permut('on', 'no')
is_permut('elite', 'tile')

