class matrix:
    def __init__(self):
        self.row=input('Enter rows in matrix: ')
        self.coloumns=input('Enter coloumns in matrix: ')
        self.L=[]
        for i in range(self.row):
            self.l1=[]
            for j in range(self.coloumns):
                print 'Enter element of ',i+1,'th row and ',j+1,'th coloumn:'
                k=input()
                self.l1+=[k]
            self.L+=[self.l1]
        
    def display(self):
        for i in range(self.row):
            for j in range(self.coloumns):
                print 'Enter element of ',i+1,'th row and ',j+1,'th coloumn:'\
                      ,self.L[i][j]
    def __str__(self):
        k=''
        for i in range(self.row):
            for j in range(self.coloumns):
                k+= str(self.L[i][j])+'    '
            k+='\n'
        return k
#-------------------------main------------------------
while True:
    print 'Creating new matrix'
    mat1=matrix()
    while True:
        
        print '1.Display matrix with row and coloumn'
        print '2.Print matrix'
        print '3.Quit'
        res=raw_input('Enter your choice: ')
        if res=='1':
            mat1.display()
        elif res=='2':
            print mat1
        elif res=='3':
            import sys
            sys.exit()
        else:
            print 'Invalid command'
   
