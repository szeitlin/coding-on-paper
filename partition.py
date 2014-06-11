def partition(linked_list, x):
    ''' linked_list -> 2 lists

	partition a linked list around a value x, so that nodes <x, nodes >= x

	>>>partition([1,2,3,5,6,7], 4)
	[1,2,3] [5,6,7]

	>>>partition([7,8,9,6,3,2], 5)
	[3,2] [6,7,8,9]

	'''
    left = []
    right = []

    for i in linked_list:
        if i <x:
            left.append(i)
        elif i >= x:
            right.append(i)

    print left, right

#partition([1,2,3,5,6,7], 4)

partition([7,8,9,6,3,2],5)
