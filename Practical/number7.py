class Calculator:
    def __init__(self,value=0.0):
        self.num=float(value)
    def __add__(self,y):
        num=self.num+y
        return num,y
    def __sub__(self,y):
        num=self.num-y
        return num,y
    def __mul__(self,y):
        num=self.num*y
        return num,y
    def __div__(self,y):
        num=self.num/y
        return num,y
    def __mod__(self,y):
        num=self.num%y
        return num,y
    def __pow__(self,y):
        num=self.num**y
        return num,y
    def __lt__(self,y):
        if (self.num<y)==False:
            self.num=y
        num=self.num
        return num,self.num<y
    def __gt__(self,y):
        if (self.num>y)==False:
            self.num=y
        num=self.num
        return num,self.num>y
    def __le__(self,y):
        if (self.num<=y)==False:
            self.num=y
        num=self.num
        return num,self.num<=y
    def __ge__(self,y):
        if (self.num>=y)==False:
            self.num=y
        num=self.num
        return num,self.num>=y
    def __eq__(self,y):
        if (self.num==y)==False:
            self.num=y
        num=self.num
        return num,self.num==y
    def __ne__(self,y):
        if (self.num!=y)==False:
            self.num=y
        num=self.num
        return num,self.num!=y
    def __str__(self):
        return str(self.num)

h=Calculator(10)
print h+1
print h-1
print h*2
print h/2
print h%6
print h**2
print h<45
print h>45
print h<=8
print h>=10
print h==45
print h!=45
print h
