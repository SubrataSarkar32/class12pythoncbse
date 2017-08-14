class queue:
    '''Implementing circular queue with list'''
    from copy import deepcopy
    def __init__(self,limit,L=[],rear=0,front=-1):
        self.L=L
        if len(self.L)==0:
            for i in range(limit):
                self.L+=[None]
            self.fp=front
            self.rp=rear
            self.limit=limit
        else:
            self.limit=limit
            self.fp=front
            self.rp=rear
    def add(self,element):
        if self.fp==-1:
                    self.fp+=1
                    self.L[self.fp]=element
                    
        elif self.fp>=self.rp:
            if self.fp<self.limit-1:
                self.fp+=1
                self.L[self.fp]=element
                
            elif self.fp==self.limit-1:
                if self.rp!=0:
                    self.fp=0
                    self.L[self.fp]=element
                else:
                    print 'OVERFLOW!!'                    
            else:
                    print 'OVERFLOW!!'
        elif self.fp<self.rp:
            if self.fp<self.limit-1:
                if self.fp+1<self.rp:
                    self.fp+=1
                    self.L[self.fp]=element
                    
                else:
                    print 'OVERFLOW!!'
            elif self.fp==self.limit-1:
                if self.rp!=0:
                    self.fp=0
                    self.L[self.fp]=element
                    
            else:
                    print 'OVERFLOW!!'
        else:
                    print 'OVERFLOW!!'

    def remove(self):
        if self.fp==-1 and self.rp==0:
            print 'UNDERFLOW!!'
        elif self.fp==self.rp:
            self.rp=0
            self.fp=-1
        elif self.fp>self.rp:
            i=self.L[self.rp]
            self.rp+=1
            return i
        elif self.rp==self.limit-1:
            if self.fp>=0:
                i=self.L[self.rp]
                self.rp=0
                return i
            else:
                print 'UNDERFLOW!!'
        elif self.rp>self.fp:
            if self.rp<self.limit-1:
                i=self.L[self.rp]
                self.rp+=1
                return i
            else:
                print 'UNDERFLOW!!'
        else:
            print 'UNDERFLOW!!'
    def display(self):
        if self.fp==-1 and self.rp==0:
            print 'UNDERFLOW!!'
        else:
            print 'Printing Circular Queue:'
            if self.rp<self.fp:
                for i in range(self.rp,self.fp+1,1):
                    print self.L[i],
                for j in range(self.fp,self.limit-1,1):
                    print '_',
                for k in range(0,self.rp,1):
                    print '_',
                print
                print '#'*30
            elif self.rp==self.fp:
                for i in range(self.rp):
                    print '_',
                print self.L[self.rp],
                for j in range(self.rp,self.limit-1):
                    print'_',
                print
                print '#'*30
            elif self.rp>self.fp:
                for i in range(self.rp,self.limit,1):
                    print self.L[i],
                if self.fp!=0:
                    for j in range(0,self.fp+1,1):
                        print self.L[j],
                elif self.fp==0:
                    print self.L[0],
                for k in range(self.fp,self.rp-1,1):
                    print '_',
                print
                print '#'*30
            else:
                print 'UNDERFLOW!!'
            
    def __len__(self):
        return len(self.L)
    def __str__(self):
        print self.L
        print self.fp,self.rp,self.limit
        return str(self.L)
#--------------------------main----------------------------------
while True:
    
    print 'Creating new circular queue'
    limit=input('Enter number of blocks you want in queue:')
    st1=queue(limit)
    print 'Queue created'
    print '1.Enqueue element'
    print '2.Dequeue element'
    print '3.Display element'
    print '4.Quit'
    while True:
        res=raw_input('Enter your choice: ')
        if res=='1':
            element=input('Enter element: ')
            st1.add(element)
        elif res=='2':
            st1.remove()
        elif res=='3':
            st1.display()
        elif res=='4':
            import sys
            sys.exit()
        else:
            print 'Invalid command'
