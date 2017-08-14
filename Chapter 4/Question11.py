class DATE:
    monda=[[1,31],[2,28],[3,31],[4,30],[5,31],[6,30],[7,31],[8,31],[9,30],[10,31],[11,30],[12,31]]
    def __init__(self,month,day):
        a=len(DATE.monda)
        self.month=month
        self.day=day
        while self.month<1 or self.month>12:
            self.month=input('Enter month (1 to 12):')
        while self.day<1 or self.day>DATE.monda[self.month-1][1]:
            self.day=input('Enter day within limit of respective month: ')
    def days_in_month(self):
        return DATE.monda[self.month-1][1]
    def next_day(self):
        if self.day+1<=DATE.monda[self.month-1][1]:
            self.day+=1
        else:
            if self.month<12:
                self.month+=1
                self.day=1
            else:
                self.month=1
                self.day=1
    def __str__(self):
        print str(self.month),'/',str(self.day)
