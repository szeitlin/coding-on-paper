def remove_dups(uns):
    ''' unsorted list -> unsorted list with no duplicates

        remove duplicates from an unsorted list.

        >>>remove_dups([2,3,2,1,5,3,1])
	[2,3,1,5]

    '''
    unique = []
    return [unique.append(x) for x in uns if x not in unique]

remove_dups([2,3,2,1,5,3,1])

