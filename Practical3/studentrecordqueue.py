class Student:
    def __init__(self,name,classs,section,rollno):
        self.name=name
        self.classs=classs
        self.section=section
        self.rollno=rollno
    def __str__(self):
        string='Student Name:'+str(self.name)+'\nS\
tudent Class:'+str(self.classs)+'\nStudent Section:'+\
str(self.section)+'\nStudent Roll No.:'+str(self.rollno)
        return string

class queue:
    '''Implementing queue with list'''    
    def __init__(self,limit):
        self.L=[]
        self.limit=limit
        self.fp=-1
        self.rp=0
        for i in range(self.limit):
            self.L+=[None]
        
    def insert(self,element):
        if self.fp+1<self.limit:
            self.fp+=1
            self.L[self.fp]=element
        else:
           print 'OVERFLOW!!'
            
    def delete(self):
        if self.rp<=self.fp:
            print 'Element removed ',self.L[self.rp]
            self.rp+=1
            if self.rp==self.limit:
                self.fp=-1
                self.rp=0
        else:
            print 'UNDERFLOW!!'

    def display(self):
        for j in range(self.rp,self.fp+1):
            print self.L[j]
            print '-'*30
        if self.fp<self.rp:
            print 'Queue is empty',
        print
        print '#'*30

#--------------------------main----------------------------------
while True:
    print 'Creating new record dataset'
    limit=input('''Enter number of student's record you want to store:''')
    st1=queue(limit)
    while True:
        
        print '1.Enqueue student'
        print '2.Dequeue student'
        print '3.Display record'
        print '4.Create new record dataset'
        print '5.Quit'
        res=raw_input('Enter your choice: ')
        if res=='1':
            rollno=input("Enter roll no: ")
            name=raw_input("Enter name: ")
            classs=raw_input("Enter class: ")
            section=raw_input("Enter section: ")
            stu=Student(name,classs,section,rollno)
            from copy import deepcopy
            st1.insert(deepcopy(stu))
        elif res=='2':
            st1.delete()
        elif res=='3':
            st1.display()
        elif res=='4':
            break
        elif res=='5':
            import sys
            sys.exit()
        else:
            print 'Invalid command'
