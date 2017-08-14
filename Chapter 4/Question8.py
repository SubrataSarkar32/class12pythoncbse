class ticbooth:
    price=2.50
    people=0
    totmoney=0.0
    def __init__(self):
        self.totmoney=float(input('Enter the amount if paid else 0:'))
        ticbooth.people+=1
        if self.totmoney==2.50:
            ticbooth.totmoney+=2.50
    @staticmethod
    def reset():
        ticbooth.people=0
        ticbooth.totmoney=0.0

    def dis(self):
        print 'Number of people ',ticbooth.people,'amount paid ',ticbooth.totmoney
    def distics(self):
        print 'Number of people who paid money',ticbooth.totmoney/2.50
