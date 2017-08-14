class circle:
    def __init__(self,radius=0.0,centrex=0.0,centrey=0.0):
        self.radius=radius
        self.centrex=centrex
        self.centrey=centrey
    def area(self):
        import math
        area= math.pi*(self.radius)**2
        return area
    def circumference(self):
        import math
        circumference= 2*math.pi*(self.radius)
        return circumference
