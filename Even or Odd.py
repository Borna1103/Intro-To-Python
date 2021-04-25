#Prompts the user with a number untill they input an even number
def main():
    x=1
    while ((x%2) != 0):
        x = int(input('input a number>'))
        if (x%2) != 0:
            print('enter an even number')
    print('good job!')
        
main()