class Lisdelete:
    '''Delete value'''
    def __init__(self):
        self.L=[]
        a=input('Enter how many numbers are in the list?')
        for i in range(a):
            b=input('Enter a number:')
            self.L+=[b]
    def delete(self):
         val=input('Enter a value to delete:')
         self.L.sort()
         n=len(self.L)
         i=0
         P=None
         while i<n:
             if self.L[i]==val:
                 P=i
             i=i+1
         if P!=None:
            self.L[P]=None
            while P<n-1:
               self.L[P]=self.L[P+1]
               P=P+1
            self.L.pop(n-1)
         else:
            print 'Entered value is not present in list'
    def display(self):
        print self.L
                
