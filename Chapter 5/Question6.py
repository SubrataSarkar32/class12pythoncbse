class Employee:
    def __init__(self,empno,empname,add,dept):
        self.__EMPNO=empno
        self.__EMPNAME=empname
        self.__EMPADD=add
        self.__EMPDEPT=dept
    def __str__(self):
        string='Employee No.:'+str(self.__EMPNO)+'\nEmployee Name:'+\
                str(self.__EMPNAME)+'\nAddress:'+str(self.__EMPADD)+\
                '\nEmployee Dept.:'+str(self.__EMPDEPT)
        return string
class Manager:
    def __init__(self):
        self.Mname=None
        self.D={}
    def readf(self):
        from copy import deepcopy
        ch1='y'
        while ch1=='y':
            self.Mname=raw_input('Enter the name of the manager:')
            emplist=[]
            ch2='y'
            while ch2=='y':
                empno=raw_input('Enter Employee (should not be more than 10 digits:')
                while len(empno)!=10:
                    empno=raw_input('Enter valid Employee Number:')
                empname=raw_input("Enter employes's name:")
                add=raw_input("Enter employes's address:")
                dept=raw_input("Enter employee's deparment:")
                EMP=Employee(empno,empname,add,dept)
                emplist+=[deepcopy(EMP)]
                ch2=raw_input('Do you want to enter more employees under same manager:')
                self.D[self.Mname]=deepcopy(emplist)
            ch1=raw_input('Do you want to add new manager:')
    def display(self):
        Dictionary =self.D
        ManagerList=Dictionary.keys()
        for i in ManagerList:
            print 'Manager:',i
            print 'Employees:'
            for j in Dictionary[i]:
                print j
                print '-'*40

#--------------------main---------------------------
ob=Manager()
ob.readf()
ob.display()
