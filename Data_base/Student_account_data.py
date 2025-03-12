def read_data():
    try:
        
        file = open('Student_account_data.txt','r',encoding='utf-8')
        a = file.readlines()
        
        for i in range(0,len(a)):
            a[i] = a[i].strip().split()
        
        return a
    
    
    finally: file.close()
    

def write_data(data):
    
    try:
        
        file = open('Student_account_data.txt','a',encoding='utf-8')
        file.write('\n')
        file.write(data)
        
    finally: file.close()
