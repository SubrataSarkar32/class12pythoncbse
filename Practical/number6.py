from types import MethodType
def func(self):
    print 'This is ',self.name
    print 'This function is outside the class'
class classic(object):
    def __init__(self,name):
        self.name=name
    def in_class_song(self):
        print 'This function works inside the class'

rabindra=classic('Rabindranath')
rabindra.out_class_song=MethodType(func,rabindra)
rabindra.in_class_song()
rabindra.out_class_song()
