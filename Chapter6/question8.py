def binsearchdec(array,item):
    beg=0
    last=len(array)-1
    while(beg<=last):
        mid=(beg+last)/2
        if item==array[mid]:
            return True
        elif item<array[mid]:
            beg=mid+1
        else:
            last=mid-1
    else:
        return False

#--------------------------main--------------------
n=input('Enter number of elements: ')
L=[]
for i in range (n):
    L.append(input('Enter element: '))
itemi=input('Enter element to be searched for ; ')
L.sort(reverse=True)
index=binsearchdec(L,itemi)
print index
if index:
    print 'Element found at index:',index,'position:',index+1
else:
    print 'The element could not be found'
