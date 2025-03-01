import Student_account_data
import Manager_account_data



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
        
        self.studentinfo.append(self.name)
        self.studentinfo.append(self.id)
        self.studentinfo.append(self.gender)


    def output(self):
        print(self.studentinfo)



class Manager(Person):
    
    def __init__(self,name,password,id,email):
        super().__init__(name,id)
        self.password = password
        self.email = email
        self.manager = []
        self.manager.append(self.name)
        self.manager.append(self.password)
        self.manager.append(self.id)
        self.manager.append(self.email)
        
    def output(self):
        print(self.manager)







if __name__ == '__main__': #Doan ma nay chi chay khi file nay duoc chay truc tiep, khong chay khi file nay duoc import vao file khac
    
    data = Student_account_data.read_data()
    mana_data = Manager_account_data.read_data()
    
    manager = Manager(mana_data[0],mana_data[1],mana_data[2],mana_data[3])
    studentlist = [Student(name,id,gender) for name,id,gender in data]

    for std in studentlist: std.output()
    manager.output()











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