def queue:
    '''Implementing queue with list'''
    def __init__(self):
        self.L=[]
    def add(self,element):
        self.L+=[element]
    def remove(self):
        i=self.L.pop(0)
        return i
