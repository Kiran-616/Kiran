class Emp:
    def __init__(self,eid,ename,basics):
        self.eid=eid
        self.ename=ename
        self.basics=basics

    def display(self):
        print(f"Employee ID  :{self.eid}")
        print(f"Employee Name:{self.ename}")
        print(f"basic salary:{self.basics}")

e1=Emp(101,"kiran",25000)
e1.display()

        