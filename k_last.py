def k_last(sll, k):
    ''' singly-linked list -> element at index k
  
    find the k-th to last element of a singly-linked list. 

    >k_last([1,2,3,4,k,last])
    k

    '''
 
    #have to start at the beginning 
    #think this uses pop to remove each of the elements?

    #pop is by index, remove is by element

    for i in range(len(sll)-k):
	sll.pop(i)
	print sll

k_last([1,2,3], 1)
