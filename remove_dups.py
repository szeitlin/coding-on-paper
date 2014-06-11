def remove_dups(uns):
    ''' unsorted list -> unsorted list with no duplicates

        remove duplicates from an unsorted list.

        >>>remove_dups([2,3,2,1,5,3,1])
	[2,3,1,5]

    '''
    unique = []
    for item in uns:
	if item not in unique:
	    unique.append(item)
	else:
	    continue

    print unique

remove_dups([2,3,2,1,5,3,1])

