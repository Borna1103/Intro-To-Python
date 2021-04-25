#Borna Hemmaty
#Created on 1/20/21
#Last edited on 1/30/21
def cipher(x):
    message = ''
    for letter in x:
        message += chr(ord(x[0])+ord(letter))
    return message

def decipher(y):
    message2 = ''
    for letter2 in y:
        message2 += chr(ord(letter2) - int(ord(y[0])/2))
    return message2

def main():
    string = input('Input a message to cipher it>')
    result1 = cipher(string)
    result2 = decipher(result1)
    print(result1)
    print(result2)

main()
