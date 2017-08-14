class Account:
    def __init__(self,custn,accno,opba):
        self.custn=custn
        self.accno=accno
        self.opba=opba
        self.aopen=opba
class Current(Account):
    def __init__(self):
        custname=raw_input('Enter customer name: ')
        accno=input('Enter customer account number: ')
        opba=input('Enter customer open balance: ')
        Account.__init__(self,custname,accno,opba)
        self.minba=input('Enter minimum required balance: ')
    def deposit(self,deposit=0):
        self.opba+=deposit
    def check(self):
        if self.opba<self.minba:
            print 'Imposing penalty','Low balance!'
            self.opba=self.opba-(self.minba-self.opba)
            return True
        else:
            return False
    def withdraw(self,withdraw):
        k=self.check()
        if k:
            print 'Withdraw not possible'
        else:
            if self.opba-withdraw>=self.minba:
                self.opba-=withdraw
                print 'Withdrawn',withdraw
            else:
                print 'After withdrawal your balance is below minimum balance\
 so you are imposable for penalty.'
                self.opba-=withdraw
                print 'Withdrawn',withdraw
                l=self.check()
    def display(self):
        print 'Here is your acount details:'
        print 'Customer name: ',self.custn
        print 'Acccount No.: ',self.accno
        print 'Current Balance: ',self.opba
        print 'Open Balance: ',self.aopen
        print 'Set minimum required balance: ',self.minba
class Savings(Account):
    def __init__(self):
        custname=raw_input('Enter customer name: ')
        accno=input('Enter customer acount number: ')
        opba=float(input('Enter customer open balance: '))
        Account.__init__(self,custname,accno,opba)
        self.cir=input('Enter compound interest rate: ')
    def deposit(self,deposit=0):
        self.opba+=deposit        
    def interest(self):
        time=input('Enter time of interest:')
        
        self.opba=(self.opba)*((1+self.cir/100.0)**time)
    def withdraw(self,withdraw):
            if self.opba-withdraw>=0:
                self.opba-=withdraw
                print 'Withdrawn',withdraw
            else:
                print 'Withdraw not possible'
    def display(self):
        print 'Here is your acount details:'
        print 'Customer name: ',self.custn
        print 'Acccount No.: ',self.accno
        print 'Current Balance: ',self.opba
        print 'Open Balance: ',self.aopen
        print 'Set compound interest (annual): ',self.cir
#main
a=Current()
a.deposit()
a.check()
bac=input('Enter amount to withdraw')
a.withdraw(bac)
a.display()
b=Savings()
b.deposit()
b.interest()
b.display()
bac=input('Enter amount to withdraw')
b.withdraw(bac)
b.display()


