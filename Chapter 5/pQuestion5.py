class wordsearch:
    '''Search word in string'''
    def __init__(self):
        self.n=raw_input('Enter a string:')
        
    def search(word):
        mg=word
        g=0
        h=0
        if mg in self.n:
            for i in range (0,len(self.n),1):
                for j in range(0,len(mg),1):            
                    if mg[j]==self.n[i+j]:
                        g+=1
                if g==len(mg):
                        for k in range(i):
                            if self.n[k]==" ":
                                i-=1
                        print 'Index is ',i
                        break
                g=0
        else:
            print "Word is not in string"
