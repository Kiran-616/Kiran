# distance class
class Distance:
    def __init__(self,km,m,cm):
        self.km=km
        self.m=m
        self.cm=cm
        print(f"Distance object {self . km} km {self.m}m{self.cm} cm destroyed")
    
    def __add__(self,other):
        total_cm = self.cm + other.cm
        total_m = self.m + other.m+total_cm // 100
        total_km= self.km + other.km+total_m//1000
        total_m=total_m % 1000
         
        return Distance(total_km,total_m,total_cm)
    def display(self):
        print(f"{self.km} km{self.m}m{self.cm} cm")

d1=Distance(2,500,75)
d2=Distance(1,800,50)
d3=d1+d2
d3.display()