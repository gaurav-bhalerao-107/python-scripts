class Employee:     # base class
    company="google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):  # child class 
     # will contain all the attributes of Employee
     # company="youtube"  
    language="python"

    def getLanguage(self):
        print(f"The language is {self.language}")  

    def showDetails(self):
        print("This is an programmer")   # overwriting can be done here 


e=Employee()
e.showDetails()
p=Programmer()
p.showDetails()
print(p.company)       
