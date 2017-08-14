class sortins:
    def __init__(self):
        self.n=input('Enter number of elements: ')
        self.L=[]
        for i in range (self.n):
            self.L.append(input('Enter element: '))
        self.sortlist=self.insertsort1dig()
        print 'List after sorting is ',self.sortlist
    def insertsort1dig(self):
        array=self.L
        print 'List is',array
        for i in range(1,len(array)):
            v=array[i]
            j=i
            while array[j-1]>v and j>=1:
                array[j]=array[j-1]
                j-=1
            array[j]=v
            
        return array
#-----main----------------------
nowsor=sortins()
