class HOUSING:
    def __init__(self):
        self.__REG_NO=0
        self.__NAME=''
        self.__TYPE=''
        self.__COST=0.0
    def Read_Data(self):
        while not(self.__REG_NO>=10 and self.__REG_No<=1000):
            self.__REG_NO=input('Enter registraton number betwee 10-1000: ')
        self.__NAME=raw_input('Enter name: ')
        self.__TYPE=raw_input('Enter house type: ')
        self.__COST=float(input('Enter cost: '))
    def Display(self):
        print 'Registration number ',self.__REG_NO
        print 'Name: ',self.__NAME
        print 'House type: ',self.__TYPE
        print 'Cost: ',self.__COST
    def Draw_Nos(self,list1):
        if len(list1)==10:
            c=0
            for i in range(10):
               if self.__name__=='HOUSING':
                   c+=1
            if c==10:
                import random
                c1=2
                while c1!=2:
                    print 'raw No.',i
                    print '-----------'
                    draw=random.randint(10,1000)
                    if draw==self.__REG_NO:
                        self.Display()
                        c1+=1
                    else:
                        for i in range(10):
                            x=list1[i]
                            if draw==x._HOUSING__REG_NO:
                                x.Display()
                                c1+=1
                                break
                    
            
