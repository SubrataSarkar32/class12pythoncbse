class Book:
    def __init__(self):
        self.BookNumber=0
        self.BookName=''
        self.Author=''
        self.Publisher=''
        self.Price=0.0
        self.noofcopies=0
        self.noofcopiesissued=0
    def entbook(self):
        self.BookNumber=input('Enter book number: ')
        self.BookName=raw_input('Enter book name: ')
        self.Author=raw_input('Enter Author name: ')
        self.Publisher=raw_input('Enter Publisher name: ')
        self.Price=float(input('Enter price of book: '))
        self.noofcopies=input('Enter number of copies: ')
        self.noofcopiesissued=input('Enter number of copies issued: ')
    def issuebook(self):
        if self.noofcopies-self.noofcopiesissued>=1:
            self.noofcopies+=1
    def returnbook(self):
        self.noofcopiesissued-=1
    def display(self):
        print 'Book number',self.BookNumber
        print 'Book name',self.BookName
        print 'Author name',self.Author
        print 'Publisher name',self.Publisher
        print 'Price of book',self.Price
        print 'Number of copies',self.noofcopies
        print 'Number of copies issued',self.noofcopiesissued
    
