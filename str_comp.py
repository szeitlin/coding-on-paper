def str_comp(word):
    ''' char str --> char + num str

    returns a string compressed with counts for repeated chars.

    >>>str_comp('abc')
    abc
    >>>str_comp('aabcccaa')
    a2bc3a2
    '''

    marker = ''
    count = 1
    out = ''

    for char in word:
        if marker != char:
            marker = char
            out = out + char + str(count)
            count = 1
        elif marker == char:
            count +=1

    out = out.replace('1','')

    print out


str_comp('abc')
str_comp('aabcccaaa')



