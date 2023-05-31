def create():
    print("Create account below.")
    global username
    global password
    username = input("Please enter a username : ")
    password = input("Please enter a password : ")

    username = username.upper()
    return username,password

def login(user,pass_):
    print("Login to your created account below.")
    checkUser=input("\nPlease enter your created username->")
    checkPass=input("Please enter your created password->")
    checkUser=checkUser.upper()

    if user==checkUser and pass_==checkPass:
        print("\nLogin successful.")
    else:
        print("\nInvalid request.")




create()
login(username,password)