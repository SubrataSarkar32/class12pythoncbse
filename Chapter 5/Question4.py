class Person:
    def __init__(self):
        self.name=raw_input('Enter name: ')
        self.phone=input('enter phone number: ')
    def display(self):
        print 'Name of person: ',self.name
        print 'Phone of person: ',self.phone
    def __del__(self):
        print self.name,' destroyed'
class Clerk(Person):
    def __init__(self):
        Person.__init__(self)
        self.qualification=raw_input("Enter qualification: ")
        self.experience=raw_input("Enter experience: ")
    def display(self):
        Person.display(self)
        print 'Qualification: ',self.qualification
        print 'Experience: ',self.experience

class Officer(Person):
    def __init__(self):
        Person.__init__(self)
        self.qualification=raw_input("Enter qualification: ")
        self.experience=raw_input("Enter experience: ")
    def display(self):
        Person.display(self)
        print 'Qualification: ',self.qualification
        print 'Experience: ',self.experience
#main
stu=Person()
stu.display()
stu1=Clerk()
stu1.display()
stu2=Officer()
stu2.display()

