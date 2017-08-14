class Applicant:
    def __init__(self):
        self.__ANo=long()
        self.__Name=''
        self.__Agg=0.0
        self.__Gradeoftype=''
    def GradeMe(self):
        if self.__Agg>=80:
            self.__Gradeoftype='A'
        elif self.__Agg<80 and self.__Agg>=65:
            self.__Gradeoftype='B'
        elif self.__Agg<65 and self.__Agg>=50:
            self.__Gradeoftype='C'
        elif self.__Agg<50:
            self.__Gradeoftype='D'
    def ENTER(self):
        self.__ANo=raw_input("Addmission Number: ")
        self.__Name=raw_input("Name: ")
        self.__Agg=float(input('Aggregate Marks: '))
        self.GradeMe()
    def RESULT(self):
        print "Addmission Number ",self.__ANo
        print "Name ",self.__Name
        print "Aggregate Marks ",self.__Agg
        print "Graade of type ",self.__Gradeoftype
