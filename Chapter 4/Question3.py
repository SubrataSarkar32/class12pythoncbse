class FixedDeposit:
    def __init__(self):
        self.Name=''
        self.AccNo=''
        self.TimeP=0
        self.Amount=0.0
    def entdepo(self):
        self.Name=raw_input("Enter depositor's name")
        self.AccNo=raw_input("Enter depositor's Account No.: ")
        self.TimeP=input('Enter 1/3/5 years timeperiod: ')
        self.Amount=float(input('Enter amount deposited; '))
    def withdraw(self):
        time=input('Enter time over since deposited in years; ')
        if time>=self.timeP/(2.0):
            print 'withdraw'
            atg=float(input('Enter amount to withdraw: '))
            if atg<sel.Amount:
                self.Amount-=atg
    def display(self):
        print "Depositor's name",self.Name
        print "Depositor's Account Number",self.AccNo
        print 'Time period of deposited ammount',self.TimeP
        print'Amount deposited',self.Amount
