def bubblesortpoints(array):
    for j in range(len(array)-1):
        print 'Iteration',j
        print
        for k in range(len(array)-1,0,-1):
            if(array[k][2]>array[k-1][2]):
                temp=array[k]
                array[k]=array[k-1]
                array[k-1]=temp
            print 'List after pass ',k,array
    return array
#-----main----------------------
n=input('Enter number of elements: ')
L=[]
for i in range (n):
    playno=input('Enter player number: ')
    playname=raw_input('Enter player name: ')
    playpoint=input('Enter player\'s points: ')
    tupl=(playno,playname,playpoint)
    L.append(tupl)
sortlist=bubblesortpoints(L)
print 'List after sorting to one\'s digit is ',sortlist
