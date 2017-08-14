class Lischange:
    '''Insert value position'''
    def __init__(self):
        self.L=[]
        a=input('Enter how many numbers are in the list?')
        for i in range(a):
            b=input('Enter a number:')
            self.L+=[b]
    def insertchec(self):
        p=input('Enter position of new value:')
        p=p-1
        self.L.append(None)
        n=len(self.L)
        v=input('Enter a new value:')
        for j in range(n-1,p,-1):
            self.L[j]=self.L[j-1]
        self.L[p]=v
    def display(self):
        print self.L
    
#----------------main-------
fio=Lischange()
fio.insertchec()
fio.display()
