class reversestring:
    '''Reverse string word by word'''
    def __init__(self):
        self.string=raw_input('Enter any string:')
        self.reversestr=''
    def reverse(self):
        j=0
        L=[]
        self.string=self.string+" "
        l=len(self.string)
        for i in range (0,l,1):
            if self.string[i]==" " :        
                L+=[self.string[j:i]]
                j=i+1
        for k in range(l-1,-1,-1):
            if self.string[k]==" " and self.string[j-1]==" ":
                L+=[self.string[k:l]]
                break
        for lg in range(len(L)):    
            length=len(L[lg])
            for a in range(-1,-(length+1),-1):
                b=L[lg][a]
                self.reversestr+=b
            self.reversestr+=' '
        print self.reversestr
