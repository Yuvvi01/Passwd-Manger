# Password generator to generate strong customs passwords. This will create random passwords of different length.

import random

# actual function which generates the password


def generatePassword(password_length):
    # initialzing the string arrays which contains the possible charecters which can be used in a password.
    small_alphabet = "abcdefghijklmnopqrstuvwxyz"
    capital_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "!@#$%^&*()_+=-[]{;}:~`>/<"
    alphabet = symbols + small_alphabet + capital_alphabet
    passwords = []

# creating a function to create and return the the password.
    for i in password_length:

        password = ""
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]

        password = replaceWithNumber(password)
        passwords.append(password)

    return passwords

# function which replaces the words in the generated password and replaces them which


def replaceWithNumber(pass_world):

    # generates and appends random numbers and returns it.

    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pass_world)//2)
        pass_world = pass_world[0:replace_index] + \
            str(random.randrange(10)) + pass_world[replace_index+1:]
        return pass_world


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
