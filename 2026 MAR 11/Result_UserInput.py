class Student:    
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def setMarks(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def calcTotal(self):
        return self.m1+self.m2+self.m3
    def calcAvg(self):
        return self.calcTotal()/3
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
        print("----------------")
        print("ID No: "+str(self.id))
        print("Name : "+self.name)
        print("Sub 1: "+str(self.m1))
        print("Sub 2: "+str(self.m2))
        print("Sub 3: "+str(self.m3))
        print("Total : "+str(self.calcTotal()))
        print("Average : "+str(self.calcAvg()))
        print("Grade : "+self.getGrade())
        print("----------------")
      
id=int(input("ID :"))
name=input("Name :")
m1=int(input("Sub 1: "))
m2=int(input("Sub 2: "))
m3=int(input("Sub 3: "))
      
Stu=Student(id,name)
Stu.setMarks(m1,m2,m3)
Stu.display()