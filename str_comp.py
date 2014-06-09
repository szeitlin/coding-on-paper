def str_comp(word):
	''' char str --> char + num str
	
	returns a string compressed with counts for repeated chars.

	>>>abc
	abc
	>>>aabcccaa
	a2bc3a2
	'''
	#first, just count the characters

	count = 1
	countlist = []
	for i in range(len(word)-1):
		if word[i] == word[i+1]:
		    count +=1
		else:
		    countlist.append(count)
		    count = 1
	
	countlist.append(count) #kind of a hack
	
	#reformat to give back the character only if count = 1, else give back 
	#character + count

	comp = " "
	for i in range(len(countlist)):
		if countlist[i] ==1:
		    comp += word[i]
		else:
		    comp += word[i] + str(countlist[i])
	print comp


str_comp('abc')
str_comp('aabcccaaa')

				
		
