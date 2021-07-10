# Password generator to generate strong customs passwords. This will create random passwords of different length.

import random
from more_itertools import random_permutation

# actual function which generates the password


def generatePassword(password_length):

    # initialzing the string arrays which contains the possible charecters which can be used in a password.
    small_alphabet = "abcdefghijklmnopqrstuvwxyz"
    capital_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "!@#$%^&*()_+=-[]{/}><"
    numbers = "0123456789"
    alphabet = numbers + small_alphabet + symbols + capital_alphabet
    passwords = []

    # shuffles the alphabet string with random permutation this increases randomization
    ''.join(random_permutation(alphabet))

    # creating a function to create and return the the password.
    for i in password_length:

        password = ""
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]

        passwords.append(password)

    return passwords

# main function which takes the user input for the following parameters:
# number of passwords to be generated
# length of the password aka strength
# prints the password in plain-text form


def main():

    # input from the user about how many passwords to generate

    numPasswords = int(
        input("How many passwords do you want to generate?\nChoose carefully! "))

    print("Generating " + str(numPasswords) + " passwords")

    passwordLengths = []

    # input form the user on the length of the password

    print("Minimum length of password should be 8 digits")

    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        if length < 8:
            length = 8
        passwordLengths.append(length)

    Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print("")
        print("Password #" + str(i+1) + " = " + Password[i])


main()
