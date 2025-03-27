#Dictionary containing user info
userdata = {"therealchacha":1234, "swampout":1111, "indiejones":2222,}
#input asking for age
actAge = int(input("Enter age: "))
#function that asks for age 
def ObtainAge(age):
    if age < 18:
        return "Access not granted"
    else:
        return "Access granted"
print(ObtainAge(actAge))
#input to take in account info
accountDetails = input("Do you have an account? Type Y for yes and N for no.")
accountDetails = accountDetails.lower()
#function that creates account
def accountAccess(acc):
    if acc == "N":
        return "Create account"
        usrName = input("Create username: ")
        passWord = input("Create passWord: ")
        userdata.update({usrName:passWord})
        return userdata
    else:
        return "site in progress"
print(accountAccess(accountDetails))
#simple account required 18 or aboved
