class Admission:
    def __init__(self):
        self.__AD_NO=0
        self.__Name=''
        self.__fees=0.0
        self.__classs=''
    def display(self):
        print "Addmission number",self.__AD_NO
        print "Name ",self.__Name
        print"Class ",self.__classs
        print "Fees ",self.__fees
    def GetADNO(self):
        return self.__AD_NO
    def Read_data(self):
        while self.__AD_NO<10 or self.__AD_NO>2000:
            self.__AD_NO=input('Enter Admission number between10-15 ')
        self.__Name=raw_input('Name ')
        self.__classs=raw_input('Class ')
        self.__fees=input('Fees ')
    def Draw_Nos(self,stu2,stu3):
        import random
        for i in range(2):
            print"Draw no.{}".format(i+1)
            print '-------------'
            draw=random.randint(10,2000)
            if draw==self.GetADNO():
                self.display()
            elif draw==stu2.GetADNO():
                stu2.display()
            elif draw==stu3.GetADNO():
                stu3.display()
                
