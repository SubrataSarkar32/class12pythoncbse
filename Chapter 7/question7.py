class city:
    def __init__(self,pin='',name=''):
        self.pin=pin
        self.name=name
    def __str__(self):
        return '[PIN:'+str(self.pin)+' City name:'+str(self.name)+']'
class stack:
    '''Implementing stack with list'''
    from copy import deepcopy
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
        if self.pos!=-1:
            print 'Element removed is ',self.L[self.pos]
            self.pos-=1
        else:
            print 'UNDERFLOW!!'
    def display(self):
        if self.pos==self.limit-1:
            print 'Stack is empty'
        for i in range(self.pos,-1,-1):
            print self.L[i],
        print
        print '#'*30
    def __len__(self):
        return len(self.L)
    def __str__(self):
        print self.L
        print self.pos,self.limit
        return str(self.L)
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
    print '5.Display list'
    print '4.Quit'
    while True:
        res=raw_input('Enter your choice: ')
        if res=='1':
            pin1=raw_input('Enter city\'s PIN: ')
            cityn1=raw_input('Enter city\'s name: ')
            element=city(pin1,cityn1)
            st1.add(element)
        elif res=='2':
            st1.remove()
        elif res=='3':
            st1.display()
        elif res=='4':
            import sys
            sys.exit()
        elif res=='5':
            print st1
        else:
            print 'Invalid command'
