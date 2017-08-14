def searchar(array,num,length):
    '''Call to search integer in array'''
    if array.sort()==None:
        for i in range(length):
            if array[i]==num:
                return 1
        return 0
    else:
        print 'Array not in ascending order'
        print 'Correct order is :',array.sort()
#------------------------main---------------------
array1=[1,2,5,15,9,11,23]
leng=len(array1)
a=searchar(array1,6,leng)
b=searchar(array1,3,leng)
print a,b
