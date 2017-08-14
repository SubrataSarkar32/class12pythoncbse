class stack:
    '''Implementing stack with list'''
    def __init__(self,limit,L=[],pos=-1):
        self.L=L
        if len(self.L)==0:
            for i in range(limit):
                self.L+=[None]
            self.pos=pos
            self.limit=limit
        else:
            self.limit=limit
            self.pos=pos
    def add(self,element):
        if self.pos<self.limit-1:
            self.pos+=1
            self.L[self.pos]=element
        else:
            print 'OVERFLOW!!'
    def remove(self):
        if self.pos>-1:
            i=self.L[self.pos]
            self.pos-=1
            return i
        else:
            print 'UNDERFLOW!!'
    def display(self):
        if self.pos==-1:
            print 'UNDERFLOW!!'
        else:
            print 'Printing Stack:'
            for j in range(self.pos,-1,-1):
                print self.L[j],
            print
            print '-------------'
    def __len__(self):
        return len(self.L)
#--------------------------main----------------------------------
while True:
    g=[]
    print 'Creating new stack'
    limit=input('Enter number of blocks you want in stack:')
    st1=stack(limit)
    print 'Stack created'
    print '1.PUSH element'
    print '2.POP element'
    print '3.Display element'
    print '4.Save stack'
    print '5.Call stack'
    print '6.Quit'
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
            saved=[st1,st1.pos]
            from copy import deepcopy
            g.append(deepcopy(saved))
        elif res=='5':
            print 'Saved stacks are:'
            for hu in range(len(g)):
                print hu+1,'th stack is :'
                print g[hu][0].display(),'Length of stack:',len(g[hu][0]),'saved \
pointer:',g[hu][0].pos
            print '****'
            op=input('Enter index of stack to call: ')
            if op<len(g) and op>0:
                L=g[op-1][0]
                st1=stack(len(L),L,g[op-1][1])
        elif res=='6':
            import sys
            sys.exit()
        else:
            print 'Invalid command'
            
        
