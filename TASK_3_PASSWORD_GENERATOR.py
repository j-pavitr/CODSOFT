# This is a random password generator in Python.

import random
#using random module to generate a random password

def genpassword(length):
    # Defining the characters for the password
    
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?/'

    char = lowercase + uppercase + digits + symbols
    passc = ''.join(random.choice(char) for _ in range(length))
    return passc

def main():
    print("Welcome to your simple Password Generator!")

    while True:
        try:
            length = int(input("How long should your password be? "))
            if length < 4:
                print("Let's keep it secure. Use at least 4 characters.")
            else:
                break
        except ValueError:
            print("That's not a number. Try again!")

    passc = genpassword(length)
    print("\nHere's your strong password:", passc)

main()
