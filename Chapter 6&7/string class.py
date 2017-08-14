class str(str):
    def __init__(self,string=''):
        str.__init__(self,string)
        self.hval='new string class'
        self.string=string
        if self.string=='':
            self.string=raw_input('Enter your string:')
        
    def __add__(self,string=''):
        self.string+=string
        return __string__(self.string)
    def __mul__(self,num=1):
        self.string=self.string*num
        return __string__(self.string)
    def __str__(self):
        return self.string
#===============main=============
newob=str()
