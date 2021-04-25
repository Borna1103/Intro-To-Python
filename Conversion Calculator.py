#Conversion Calculator by Borna Hemmaty
#Created on 1/16/21
#Last Edit 1/16/21 10:28pm

#Conversion for Fahrenheit to Celsius
def temperature():
    Fahrenheit = int(input('Input Fahrenheit Temperature:'))
    print(((9 * Fahrenheit / 5) + 32), 'Ⅽ')

#Conversion for Miles per Hour to Meters per Seconds
def speed():
    Miles = int(input('Input Miles/Hour:'))
    print(Miles*1609.34/60, 'Meters/Second')

#main function to use both functions
def main():
    Choose = int(input('Enter 1 to convert Fahrenheit to Celsius\nEnter 2 to convert miles per hour to meters per seconds:\n---------------------------------\n'))
    if (Choose == 1):
        temperature()
    elif (Choose == 2):
        speed()
    #if 1 and 2 do not work then main is called again
    else:
        print('That character is invalid')
        main()

#use of function 
main()