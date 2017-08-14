class Time:
    '''returns approx time'''
    def __init__(self):
        self.seconds=0.0
    def settime(self):
        self.seconds=input('Enter time in seconds: ')
    def convert_to_minutes(self):
        minute=0.0
        second=0.0
        minute=self.seconds//60.0
        second==self.seconds-(minute*60)
        ms=str(minute)+';'+str(second)
        return ms
    def convert_to_hour(self):
        minute=0.0
        second=0.0
        hour=0.0
        minute=self.seconds//60.0
        second==self.seconds-(minute*60)
        hour=minute//60.0
        minute==minute-(hour*60)
        hms=str(hour)+':'+str(minute)+';'+str(second)
        return hms
