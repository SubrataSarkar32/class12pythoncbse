class Student:
    def __init__(self,name='',date='',members='',age=0):
        self.name=name
        self.date=date
        self.members=members
        self.age=age
    def readData(self):
        self.name=raw_input('Enter name: ')
        self.date=raw_input('Enter a date:')
        self.members=raw_input('Enter member name: ')
        self.age=input('Enter age in years: ')
    def display(self):
        print 'Name: ',self.name
        print 'Date:',self.date
        print 'Member name: ',self.members
        print 'Age in years: ',self.age
class PrimaryStudent(Student):
    def __init__(self,activityhours=0):
        Student.__init__(self)
        self.activityhours=activityhours
    def ReadPrimary(self):
        self.readData()
        self.activityhours=input('Enter activity no. of hours: ')
    def DisplayPrimary(self):
        self.display()
        print 'Activity number of hours: ',self.activityhours

class SecondaryStudent(Student):
    def __init__(self,language=''):
        Student.__init__(self)
        self.language=language
    def ReadSecondary(self):
        self.readData()
        self.language=raw_input('Enter language: ')
    def DisplaySecondary(self):
        self.display()
        print 'Language: ',self.language
#main
stu=Student()
stu.readData()
stu.display()
stu1=PrimaryStudent()
stu1.ReadPrimary()
stu1.DisplayPrimary()
stu2=SecondaryStudent()
stu2.ReadSecondary()
stu2.DisplaySecondary()
