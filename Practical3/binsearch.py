class binsearch:
    def __init__(self):
        self.n=input('Enter number of elements: ')
        self.L=[]
        for i in range (self.n):
            self.L.append(input('Enter element: '))
        itemi=input('Enter element to be searched for : ')
        self.L.sort(reverse=True)
        self.index=self.binsearchdec(itemi)
        if self.index:
            print 'Element found at index:',self.index,'position:',self.index+1
        else:
            print 'The element could not be found'

    def binsearchdec(self,item):
        array=self.L
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
fiop=binsearch()
