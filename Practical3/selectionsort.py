class sort3:
    def __init__(self):
        a=input('Enter how many numbers are in the list?')
        self.list1=[]
        for i in range(a):
            b=input('Enter a number:')
            self.list1+=[b]
        
    def selection_sort(self):
        print 'List is ',self.list1
        for curpos in range(len(self.list1)):
            minpos=curpos
            for scanpos in range(curpos+1,len(self.list1)):
                if self.list1[scanpos]<self.list1[minpos]:
                    minpos=scanpos
            temp=self.list1[minpos]
            self.list1[minpos]=self.list1[curpos]
            self.list1[curpos]=temp
        return self.list1
#----------main-----------------------
newl=sort3()
k=newl.selection_sort()
print 'Sorted list is ',k
