class Batsmen:
    def __init__(self):
        self.fname=''
        self.lname=''
        self.numbf=0
        self.nunbs=0
        self.runsmade=0
    def inputup(self):
        self.fname=raw_input("Player's first name: ")
        self.lname=raw_input("Player's last name: ")
        self.numbf=input('Number of fours: ')
        self.nunbs=input('Number of sixes: ')
        self.runsmade=input('Runs taken: ')
        
    def infup(self):
        update=0
        whlie update>=0 or update<7:
            update=int(input('Enter runs made in this ball:'))
            if update==4:
                self.numbf+=1
                self.runsmade+=4
            elif update==6:
                self.numbf+=1
                self.runsmade+=6
            else:
                self.runsmade+=update
    def display(self):
        print "Player's first name ",self.fname
        print "Player's last name ",self.lname
        print 'Number of fours ',self.numbf
        print 'Number of sixes ',self.nunbs
        print 'Runs taken ',self.runsmade
