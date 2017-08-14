def func():
    print 'This function is outside the class'
class classic(object):
    def in_class_song(self):
        print 'This function works inside the class'

rabindra=classic()
rabindra.out_class_song=func
rabindra.in_class_song()
rabindra.out_class_song()
