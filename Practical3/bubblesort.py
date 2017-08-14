class searchbub:
    def __init__(self):
        self.n=input('Enter number of elements: ')
        self.L=[]
        for i in range (self.n):
            self.L.append(input('Enter element: '))
        self.sortlist=self.extrabubblesort()
        print 'List after sorting is ',self.sortlist
    def extrabubblesort(self):
        array=self.L
        print 'List is',array
        for j in range(len(array)-1):
            for k in range(len(array)-1):
                if(array[k]>array[k+1]):
                    temp=array[k]
                    array[k]=array[k+1]
                    array[k+1]=temp
                
        return array
#-----main----------------------
sod=searchbub()
