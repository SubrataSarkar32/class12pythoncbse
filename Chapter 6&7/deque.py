class deque:
    '''This both side insertion and deletion deque'''
    
    def __init__(self,limit):
        self.L=[]
        self.limit=limit
        
    def insertl(self,element):
        if len(self.L)==0:
            self.L.append(element)
        elif len(self.L)<self.limit:
            L1=[element]
            L1=L1+self.L
            from copy import deepcopy
            self.L=deepcopy(L1)
        else:
            print 'OVERFLOW!!'
    
    def insertr(self,element):
        if len(self.L)==0:
            self.L.append(element)
        elif len(self.L)<self.limit:
            L1=[element]
            L1=self.L+L1
            from copy import deepcopy
            self.L=deepcopy(L1)
        else:
            print 'OVERFLOW!!'
    def deletel(self):
        if len(self.L)==0:
            print 'UNDERFLOW!!'
        else:
            k=self.L.pop(0)
            print 'Element removed ',k

    def deleter(self):
        if len(self.L)==0:
            print 'UNDERFLOW!!'
        else:
            k=self.L.pop()
            print 'Element removed ',k
            
    def insert(self,element):
        ch='i'
        while ch.lower()!='l' and ch.lower()!='r':
            ch=raw_input('Insert element from left or right?(L\R)')
        else:
            if len(self.L)!=self.limit:
                if ch.lower()=='l':
                    self.insertl(element)
                else:
                    self.insertr(element)
            else:
                print 'OVERFLOW!!'
                
    def delete(self):
        ch='i'
        while ch.lower()!='l' and ch.lower()!='r':
            ch=raw_input('Delete element from left or right?(L\R)')
        else:
            if ch.lower()=='l':
                self.deletel()
            else:
                self.deleter()
                
    def display(self):
        for i in self.L:
            print i,
        if len(self.L)==0:
            for j in range(len(self.L)-1,self.limit):
                print '_',
        print
        print '#'*30

    def __str__(self):
        return str(self.L)

#--------------------------main----------------------------------
while True:
    g=[]
    print 'Creating new deque'
    limit=input('Enter number of blocks you want in deque:')
    st1=deque(limit)
    print 'Deque created'
    print '1.Enqueue element'
    print '2.Dequeue element'
    print '3.Display deque'
    print '4.Display list'
    print '5.Quit'
    while True:
        res=raw_input('Enter your choice: ')
        if res=='1':
            element=input('Enter element: ')
            st1.insert(element)
        elif res=='2':
            st1.delete()
        elif res=='3':
            st1.display()
        elif res=='5':
            import sys
            sys.exit()
        elif res=='4':
            print st1
        else:
            print 'Invalid command'

