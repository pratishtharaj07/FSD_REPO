#assignment 4:- while loop

#program 4

c_password = "python123"
while True:
    password=input("enter the password: ")
    if password==c_password:
        print ("correct password")
        break
    else:
        print("try again")
