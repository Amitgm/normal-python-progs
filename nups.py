import numpy as np

class employee:
    numofemp=0
    def __init__(self,name,last,salary):
        self.name=name
        self.last=last
        self.salary=salary

        employee.numofemp+=1
    def salary_raise(self,salraise):
        self.increase=self.salary*salraise
        return self.increase
    @classmethod
    def amount_increase(cls,amount):
        cls.amtinc=amount
        return cls.amtinc

    @classmethod
    def name_splitter(cls,emp):
        name,last,salary=emp.split('-')
        return cls(name,last,salary)
    
class subemployee(employee):
    
    def __init__(self,name,last,salary,lang):
     super().__init__(name,last,salary)
     self.lang=lang

    @classmethod
    def experience(cls,standard):
     cls.standard=standard
     return cls.standard

     
e1=employee('amit','george',1000)
e2=subemployee('andrew','jack',5000,'python')
e3=subemployee('james','joe',4000,'java')

subemployee.experience(20)
subemployee.amount_increase(50)

print(e2.amtinc)
print(e3.amtinc)

print(e2.standard)
print(e3.standard)




employee.amount_increase(15)

print(e1.amtinc)
print(e2.amtinc)
print(employee.amtinc)

new_emp='jack-john-100'

emp1=employee.name_splitter(new_emp)
print(emp1.last)

