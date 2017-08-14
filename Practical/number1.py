class ITEMS:
    def __init__(self):
        self.Icode=0
        self.Item=None
        self.Price=0
        self.Qty=0
        self.Discount=0
        self.QtyP=0
        self.TotalPrice=0
        self.NetPrice=0
        
    def inputen(self):
        self.Icode=input('Enter Item code:')
        self.Item=raw_input('Enter Item name:')
        self.Price=input('Enter price:')
        self.Qty=input('Enter quantity in stock:')
    def CalDisc(self):
            if self.QtyP<=10:
                self.Discount=0
            elif self.QtyP>11 and self.QtyP<20:
                self.Discount=15
            elif self.QtyP>20:
                self.Discount=20
    def CalNetPrice(self):
            self.TotalPrice= float(self.Price*self.QtyP)
            self.NetPrice=self.TotalPrice-(self.TotalPrice*(self.Discount/100.0))
    def Buy(self):
            while self.QtyP==0 or self.QtyP>self.Qty:
                self.QtyP=input('Enter quantity to be purchased:')
            self.CalDisc()
            self.CalNetPrice()
            self.Qty=self.Qty-self.QtyP
    def show(self):
            print 'Item code is ',self.Icode
            print 'Item name is ',self.Item
            print 'Item has price ',self.Price
            print 'Total item available ',self.Qty
            print 'Discount on item ',self.Discount
            print 'Items purchased ',self.QtyP
            print 'Total price of item ',self.TotalPrice
            print 'Net Price of items ',self.NetPrice

a=ITEMS()
a.inputen()
a.Buy()
a.show()
