from sy_marks import SYMarks
from ty_marks import TYMarks

class Student:
    def __init__(self, roll,name,sy_obj,ty_obj):
        self.roll=roll
        self.name=name
        self.sy=sy_obj
        self.ty=ty_obj
    
    def calculate_grade(self):
        total=self.sy.comp+self.ty.theory+self.ty.practial
        avg = total/3


        if avg >=70:
            grade="A"
        elif avg >=60:
            grade="B"
        elif avg >=50:
            grade="C"
        elif avg >=40:
            grade="Pass Class"
        else:
            grade="Fail"
        
        return avg, grade
    
    def display(self):
        print("\n----Student Result-----")
        print("Roll No:",self.roll)
        print("Name :", self.name)
        self.sy.display()
        self.ty.display()
        avg , grade=self.calculate_grade()

        print("Average Marks:",avg)
        print("Grade  :",grade)

if __name__ == "__main__":
    sy=SYMarks(comp=65,maths=70,electronics=60)
    ty=TYMarks(theory=75,practial=80)

    s= Student(roll=101,name="kiran", sy_obj=sy, ty_obj=ty)
    
    
    s.display()

        


        
    
