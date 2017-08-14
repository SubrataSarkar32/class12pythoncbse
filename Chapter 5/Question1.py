class publication:
    def __init__(self,title='',price=0.0):
        self.title=title
        self.price=price
        
    def getdata(self):
        self.title=raw_input('Enter the title: ')
        self.price=float(input('Enter price: '))

    def putdata(self):
        print 'Details of the selected publication: '
        print 'Title of publication is ',self.title        
        print 'Price of publication is ',self.price

class book(publication):
    def __init__(self,pagecount=0):
        publication.__init__(self)
        self.pagecount=pagecount
    def getdata(self):
        publication.getdata(self)
        self.pagecount=int(input('Enter page count: '))

    def putdata(self):
        publication.putdata(self)                
        print 'Pagecount of publication is ',self.pagecount

class tape(publication):
    def __init__(self,ptinmin=0.0):
        publication.__init__(self)
        self.ptinmin=ptinmin
    def getdata(self):
        publication.getdata(self)
        import math
        self.ptinmin=float(input('Enter play time in minutes: '))
        while (self.ptinmin-math.floor(self.ptinmin))>0.60:
            self.ptinmin=float(input('Enter proper time: '))

    def putdata(self):
        publication.putdata(self)                
        print 'Play time in minutes of publication is ',self.ptinmin
#main
c=publication()
c.getdata()
c.putdata()
a=book()
a.getdata()
a.putdata()
b=tape()
b.getdata()
b.putdata()

