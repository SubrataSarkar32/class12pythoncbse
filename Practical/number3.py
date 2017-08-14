class ADMISSION:
    def __init__(self):
        self.__AD_NO=0
        self.__NAME=''
        self.__CLASS=''
        self.__FEES=float()
    def Read_Data(self):
        while self.__AD_NO<10 or self.__AD_NO>2000:
            self.__AD_NO=input('Enter AD_NO between 10 to 2000:')
        self.__NAME=raw_input('Name :')
        self.__CLASS=raw_input('Class :')
        self.__FEES=input('Fees :')
    def Display(self):
        print 'AD_NO is ',self.__AD_NO
        print 'Name is ',self.__NAME
        print 'Class ',self.__CLASS
        print 'Fees ',self.__FEES
    def GetADNO(self):
        return self.__AD_NO
    @staticmethod
    def Draw_Nos(stu1,stu2,stu3):        
        import random
        c1=1
        while c1!=3:            
            draw=random.randint(10,2000)
            if draw==stu1.GetADNO():
                print"Draw no.{}".format(c1)
                print '-------------'
                stu1.Display()
                c1+=1
            elif draw==stu2.GetADNO():
                print"Draw no.{}".format(c1)
                print '-------------'
                stu2.Display()
                c1+=1
            elif draw==stu3.GetADNO():
                print"Draw no.{}".format(c1)
                print '-------------'
                stu3.Display()
                c1+=1
stu1=ADMISSION()
stu1.Read_Data()
stu2=ADMISSION()
stu2.Read_Data()
stu3=ADMISSION()
stu3.Read_Data()
ADMISSION.Draw_Nos(stu1,stu2,stu3)

