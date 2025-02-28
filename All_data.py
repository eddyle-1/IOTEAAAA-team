import Student_account_data


class Person:
    
    def __init__(self,name,id):
        self.obj = []
        self.name = name
        self.id = id
        
        
        
class Student(Person):
    
    def __init__(self,name,id,gender):
        super().__init__(name,id)
        self.gender = gender
        self.studentinfo = []
        self.studentinfo.append(self.gender)
        self.studentinfo.append(self.name)
        self.studentinfo.append(self.id)


    def output(self):

        print(self.studentinfo)
    
class Manager(Person):
    
    def __init__(self,name,id):
        super().__init__(name,id)
        self.manager = []
        self.manager.append(self.namelist)
        self.manager.append(self.id)
        
        
    def output(self):
        return self.manager

data = Student_account_data.get_data()
studentlist = [Student(name,id,number) for name,id,number in data]


for std in studentlist:
    std.output()











'''num = int(input())

a = [None]*num #a = [None,None,None,...num times]

for k in range(0,num):
    n = input('Enter name: ')
    i = input('Enter id: ')
    g = input('Enter gender: ')
    a[k] = Student(n,i,g)

print()
    
for i in range(0,num):
    a[i].output()
'''