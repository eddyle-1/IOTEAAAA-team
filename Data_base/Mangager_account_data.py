#Manager file data order: Name - Password - ID number - Email


def read_data():
    
    try:
        
        file = open('Manager_account_data.txt','r',encoding='utf-8')
        a = file.read()
        
        
        return a.strip().split()
    
    finally: file.close()
    

def write_data(data):
    
    try:
        
        file = open('Manager_account_data.txt','a',encoding='utf-8')
        file.write('\n')
        file.write(data)
    
    finally: file.close()
