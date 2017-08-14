class Calculator:
    def __init__(self,value=0.0):
        self.num=float(value)
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
    def __str__(self):
        print str(self.num)
