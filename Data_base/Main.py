import Student_account_data, Manager_account_data
import All_data

manager_data = Manager_account_data.read_data()
data = Student_account_data.read_data()

studentlist = [All_data.Student(name,int(id),gender) for name,id,gender in data]
manager = All_data.Manager(manager_data[0],manager_data[1],manager_data[2],manager_data[3])

manager.output()
print()
for i in studentlist:
    i.output()
