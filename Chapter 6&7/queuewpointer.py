class queue:
    '''This normal queue'''
    
    def __init__(self,limit):
        self.L=[]
        self.limit=limit
        self.fp=-1
        self.rp=0
        for i in range(self.limit):
            self.L+=[None]
        self.insertstat=True
        
    def insert(self,element):
        if self.fp+1<self.limit:
            self.fp+=1
            self.L[self.fp]=element
        else:
           print 'OVERFLOW!!'
            
    def delete(self):
        if self.rp<=self.fp:
            print 'Element removed ',self.L[self.rp]
            self.rp+=1
            if self.rp==self.limit:
                self.fp=-1
                self.rp=0
        else:
            print 'UNDERFLOW!!'

    def display(self):
        for j in range(self.rp,self.fp+1):
            print self.L[j],
        if self.fp<self.rp:
            print 'Queue is empty',
        print
        print '#'*30

    def __str__(self):
        return str(self.L)

#--------------------------main----------------------------------
while True:
    g=[]
    print 'Creating new queue'
    limit=input('Enter number of blocks you want in queue:')
    st1=queue(limit)
    while True:
        print 'queue created'
        print '1.Enqueue element'
        print '2.Dequeue element'
        print '3.Display queue'
        print '4.Create new queue'
        print '5.Quit'
        res=raw_input('Enter your choice: ')
        if res=='1':
            element=input('Enter element: ')
            st1.insert(element)
        elif res=='2':
            st1.delete()
        elif res=='3':
            st1.display()
        elif res=='4':
            break
        elif res=='5':
            import sys
            sys.exit()
        else:
            print 'Invalid command'
