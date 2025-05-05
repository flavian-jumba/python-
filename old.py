userName = str(input("Please enter your name:"))


userEmail = str(input("Please enter your email:"))


while  userEmail == '' or userName == '':


    print("Please enter valid cridentials")   

    userName = str(input("Please enter your name:"))

    userEmail = str(input("Please enter your email:"))


print(f"Hello {userName} thanks for signing up, please login to your acount")

name = input("Please enter your name:")

email = input("Please enter your email:")


while userName!= name and userEmail!=email:

    print("Invalid cridentials")

    name = input("Please enter your name:")

    email = input("Please enter your email:")

    
print(f"Welcome Back {userName}")
      