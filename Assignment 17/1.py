# class:student
class Student:
    def __init__(self,):
        self.studentID = 0
        self.name=" "
        self.age=0
        self.percentage=0.0
    def Accept(self):
        self.studentID= int(input("enter student ID:"))
        self.name=input("enter name:")
        self.age=int(input("enter age:"))
        self.percentage= float(input("enter percentage:"))

    def Display(self):
        print("Student ID:",self.studentID)
        print("name:",self.name)
        print("age:",self.age)
        print("percentage:",self.percentage)

    def CalculateRank(self):
        if self.percentage >=75:
            return "Distinction"
        elif self.percentage >=60:
            return "First class"
        elif self.percentage >= 50:
            return "Second Class"
        else:
            return "Fail"
    
        
    

s1 = Student()
s1.Accept()
s1.Display()
print("Rank:",s1.CalculateRank())


    