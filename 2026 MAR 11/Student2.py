class Student:
    def __init__(self,name,id):           #Magic or Constructor method
        self.name=name
        self.id=id
        
    def display(self):                    #Instance method
        print("My name is "+self.name)
        print("My id is "+str(self.id))
        
Stu1 = Student("Kayal",1000)
Stu1.display()

Stu2 = Student("Nilavan",1001)
Stu2.display()