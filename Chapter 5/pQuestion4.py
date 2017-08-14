class Lisdelete1:
    '''Delete position'''
    def __init__(self):
        self.L=[]
        a=input('Enter how many numbers are in the list?')
        for i in range(a):
            b=input('Enter a number:')
            self.L+=[b]
    def delete(self):
         P=input('Enter position of value to delete')
         n=len(self.L)
         if P-1<n:
             self.L[P-1]=None
             while P-1<n-1:
                 self.L[P-1]=self.L[P]
                 P=P+1
             self.L.pop(n-1)
         else:
             print 'This index is out of range'
    def display(self):
        print self.L
                
