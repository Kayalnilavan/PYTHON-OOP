class Student:  
    def __init__(self):
        self.id=1001
        self.name="Kayal"
    def setMarks(self):
        self.m1=86
        self.m2=79
        self.m3=92
    def calcTotal(self):
        total=self.m1+self.m2+self.m3
        return total
    def calcAvg(self):
        avg=self.calcTotal()/3
        return avg
    def getGrade(self):
        avg=self.calcAvg()
        if avg>=100:
            grade="A"
        elif avg >=65:
            grade="B"
        elif avg>=55:
            grade="C"
        elif avg>=45:
            grade="S"
        else:
            grade="W"
        return grade
    def display(self):
        self.setMarks()
        print("ID : "+str(self.id))
        print("Name : "+self.name)
        print("Sub 1: "+str(self.m1))
        print("Sub 2: "+str(self.m2))
        print("Sub 3: "+str(self.m3))
        print("Total : "+str(self.calcTotal()))
        print("Average : "+str(self.calcAvg()))
        print("Grade : "+self.getGrade())
        
Stu=Student()
Stu.display()