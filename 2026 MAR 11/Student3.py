class Student:
    def __init__(self,fname,lname,id):       #Constructor with Parameter
        self.fname=fname
        self.lname=lname
        self.id=id  
        
    def getFullname(self):                   #Return method
        return self.fname+self.lname
        
    def display(self):                       #Instance method    
        print("My id is "+str(self.id))
        print("My full name is "+self.getFullname())
        
Stu1 = Student("Kayal","Nilavan",1000)
Stu1.display()