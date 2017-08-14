class Calculator:
    def __init__(self,value=0.0):
        self.num=float(value)
        print self.__str__()
    def __add__(self,y):
        self.num=self.num+y
        return Calculator(self.num)
    def __sub__(self,y):
        self.num=self.num-y
        return Calculator(self.num)
    def __mul__(self,y):
        self.num=self.num*y
        return Calculator(self.num)
    def __div__(self,y):
        self.num=self.num/y
        return Calculator(self.num)
    def __mod__(self,y):
        self.num=self.num%y
        return Calculator(self.num)
    def __pow__(self,y):
        self.num=self.num**y
        return Calculator(self.num)
    def __lt__(self,y):
        self.num=self.num<y
        return Calculator(self.num)
    def __gt__(self,y):
        self.num=self.num>y
        return Calculator(self.num)
    def __le__(self,y):
        self.num=self.num<=y
        return Calculator(self.num)
    def __ge__(self,y):
        self.num=self.num>=y
        return Calculator(self.num)
    def __eq__(self,y):
        self.num=self.num==y
        return Calculator(self.num)
    def __ne__(self,y):
        self.num=self.num!=y
        return Calculator(self.num)
    def __str__(self):
        return str(self.num)
