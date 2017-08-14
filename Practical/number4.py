def func(self):
    print 'This function is outside the class'
class classic(object):
    def in_class_song(self):
        print 'This function works inside the class'

rabindra=classic()

rabindra.in_class_song()
setattr(classic,'out_class_song',func)
rabindra.out_class_song()
