#Python Security by Borna Hemmaty
#Created 1/20/21
#Last updated 1/20/21
Counter = 0
def menu():
    print('Enter 1 to login')
    print('Enter 2 to see about page')
    print('Enter 3 to end\n--------------')
    choice = int(input())

    if (choice == 1):
        User = input('Enter User ID:\n')
        Password = input('Enter Password:\n')
        Verify = VerifyUser(User, Password)
        if (Verify == False):
            print('--------------\nIncorrect Username or Password\n--------------')
            global Counter
            Counter += 1
            if (Counter == 3):
                print('You have reached the maximum number of tries, Goodbye')
            else:
                menu()
        elif (Verify == True):
            print('--------------\nWelcome!')
    elif (choice == 2):
        print('This website is about security and password management through python.\n--------------')
        menu()
    elif (choice == 3):
        print('Goodbye')
    else:
        print('This choice is invalid!\n--------------')
        menu()    

def VerifyUser(x,y):
        return (x == 'Python' and y == "1193")
menu()