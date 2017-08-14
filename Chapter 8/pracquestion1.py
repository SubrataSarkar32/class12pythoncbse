class modifile:
    def __init__(self,inputfilen):
        self.fh=open(inputfilen,'r+')
        self.change()
        self.fh.close()

    def change(self):
        while True:
            position=self.fh.tell()
            recs=self.fh.readline()
            if recs.find('Akshar')!=-1:
                recs=recs.replace('Akshar','Akshra')
                self.fh.seek(position)
                self.fh.write(recs)
                break

a=modifile('Marks.det')
