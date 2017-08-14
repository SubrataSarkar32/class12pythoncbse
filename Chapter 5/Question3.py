class Person:
    def __init__(self):
        self.name=raw_input('Enter name: ')
        self.phone=input('enter phone number: ')
    def display(self):
        print 'Name of person: ',self.name
        print 'Phone of person: ',self.phone
    def __del__(self):
        print self.name,' destroyed'

class Spouse(Person):
    def __init__(self):
        Person.__init__(self)
        self.spouseName=raw_input("Enter spouse's name: ")
    def display(self):
        Person.display(self)
        print 'Spouse name: ',self.spouseName

#main
stu=Person()
stu.display()
stu1=Spouse()
stu1.display()
