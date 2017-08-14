def sortstrlist(array):
    length=len(array)
    for i in range(1,len(array)):
        v=array[i]
        j=i
        while len(array[j-1])>len(v) and j>=1:
            array[j]=array[j-1]
            j-=1
        array[j]=v
        print 'List after pass',i,array
    return array
#-----main----------------------
n=input('Enter number of elements: ')
L=[]
for i in range (n):
    L.append(raw_input('Enter element: '))
sortlist=sortstrlist(L)
print 'List after sorting to one\'s digit is ',sortlist    
