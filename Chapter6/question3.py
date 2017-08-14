def binsearchdec(array,item):
    beg=0
    last=len(array)-1
    while(beg<=last):
        mid=(beg+last)/2
        if item==array[mid]:
            return mid
        elif array[mid]<item:
            lasst=mid-1
        else:
            beg=mid+1
    else:
        return False

#--------------------------main--------------------
n=input('Enter number of lements: ')
L=[]
for i in range (n):
    L.append(input('Enter element: '))
itemi=input('Enter element to be searched for ; ')
L.sort(reverse=True)
index=binsearchdec(L,itemi)
if index:
    print 'Element found at index:',index,'position:',index+1
else:
    print 'The element could not be found'
