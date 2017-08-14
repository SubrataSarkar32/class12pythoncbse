def insertsort1dig(array):
    for i in range(1,len(array)):
        v=array[i]
        j=i
        while array[j-1]%10>v%10 and j>=1:
            array[j]=array[j-1]
            j-=1
        array[j]=v
        print 'List after pass',i,array
    return array
#-----main----------------------
n=input('Enter number of elements: ')
L=[]
for i in range (n):
    L.append(input('Enter element: '))
sortlist=insertsort1dig(L)
print 'List after sorting to one\'s digit is ',sortlist

