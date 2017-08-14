class concatatlast:
    '''Concatenate centre word at last'''
    def __init__(self):
        self.string=raw_input('Enter a string: ')
        self.cocatenated=''
    def concatenatel(self):
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
            length1=len(L[lg])
            P=length1/2
            K=list(L[lg])
            I=K.pop(P)
            K+=I
            for a in range(0,length1,1):
                b=K[a]
                self.concatenated+=b
            self.concatenated+=' '
        print self.concatenated
