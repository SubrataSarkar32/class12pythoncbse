def extrabubblesort(array):
    for i in range(len(array)):
        if array[i]/5==0:
            array[i]/=5
        else:
            array[i]*=2
    print 'New list is',array
    for j in range(len(array)-1):
        print 'Iteration',j
        print
        for k in range(len(array)-1):
            if(array[k]>array[k+1]):
                temp=array[k]
                array[k]=array[k+1]
                array[k+1]=temp
            print 'List after pass ',k,array
    return array
#-----main----------------------
n=input('Enter number of elements: ')
L=[]
for i in range (n):
    L.append(input('Enter element: '))
sortlist=extrabubblesort(L)
print 'List after sorting to one\'s digit is ',sortlist
