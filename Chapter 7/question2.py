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
    def push(self,element):
        if self.pos<self.limit-1:
            self.pos+=1
            self.L[self.pos]=element
        else:
            print 'OVERFLOW!!'
    def pop(self):
        if self.pos!=-1:
            print 'Element removed is ',self.L[self.pos]
            self.pos-=1
            return self.L[self.pos+1]
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
text=raw_input('Enter a line of text: ')
length=len(text)
stack1=stack(length)
for ele in text:
    stack1.push(ele)
string=''
for i in range(length):
    k=stack1.pop()
    stri=k*2
    string+=stri
print string
