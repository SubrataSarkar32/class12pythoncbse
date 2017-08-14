class Lischange1:
    '''Insert value'''
    def __init__(self):
        self.L=[]
        a=input('Enter how many numbers are in the list?')
        for i in range(a):
            b=input('Enter a number:')
            self.L+=[b]
    def insertchecv(self):
        val=input('Enter a new value:')
        self.L.sort()
        self.L.append(None)
        n=len(self.L)
        i=0
        P=None
        while i<n:
            if self.L[i]>val:
                P=i
                i=n-1
                break           
            else:
                i=i+1
        
        if P!=None:
           while i>=P:
              self.L[i]=self.L[i-1]
              i=i-1
           self.L[P]=val
        else:
            self.L[n-1]=val
    def display(self):
        print self.L
#----------------main-------
fio=Lischange1()
fio.insertchecv()
fio.display()
