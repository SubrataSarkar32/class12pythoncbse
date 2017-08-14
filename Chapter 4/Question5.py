class Bowler:
    def __init__(self):
        self.fname=''
        self.lname=''
        self.oversbowled=0
        self.noofmaidenovers=0
        self.runsgiven=0
        self.wicketstaken=0
    def inputup(self):
        self.fname=raw_input("Player's first name: ")
        self.lname=raw_input("Player's last name: ")
        self.oversbowled=input('Number of over bowled: ')
        self.noofmaidenovers=input('Number of maiden over bowled: ')
        self.runsgiven=input('Runs given: ')
        self.wicketstaken=input('Wickets taken: ')
    def infup(self):
        self.oversbowled=input('Number of over bowled: ')
        self.noofmaidenovers=input('Number of maiden over bowled: ')
        self.runsgiven=input('Runs given: ')
        self.wicketstaken=input('Wickets taken: ')
    def display(self):
        print "Player's first name ",self.fname
        print "Player's last name ",self.lname
        print 'Number of over bowled ',self.oversbowled
        print 'Number of maiden over bowled ',self.noofmaidenovers
        print 'Runs given ',self.runsgiven
        print 'Wickets taken ',self.wicketstaken
