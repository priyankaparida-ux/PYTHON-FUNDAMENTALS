# login system
username = input("Enter username : ")
password = input("Enter password : ")
if(username == "admin" and password == "pass"):
    print("Log in sucessful")
else:
    if (username != "admin"):
        print("Wrong username")
    else:
        print("Wrong password")
