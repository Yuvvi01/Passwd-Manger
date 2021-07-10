# hashing passwords in whirlpool and SHA512
import hashlib
import sys
import codecs


def SHA512_hash(input_password):
    # returns resultant SHA512 hash
    result = hashlib.sha512(input_password.encode('utf-8')).hexdigest()
    print(result)


def SHA384_hash(input_password):
    # returns resultant SHA384 hash
    result = hashlib.sha384(input_password.encode('utf-8')).hexdigest()
    print(result)


def compare_hashes(input_password, input_hashes):
    input_password.encode('utf-8')
    input_hashes.encode('utf-8')

    if (input_hashes == SHA512_hash(input_password) or input_hashes == SHA384_hash(input_password)):
        print("The given password and hash match both SHA512 and SHA384 cryptographical algorithms.")
    elif (input_hashes == SHA512_hash(input_password) and input_hashes != SHA384_hash(input_password)):
        print(
            "The given password matches the SHA512 algorithm but not the SHA384 algorithm.")
    elif (input_hashes == SHA384_hash(input_password) and input_hashes != SHA512_hash(input_password)):
        print(
            "The given password matches the SHA384 algorithm but not the SHA512 algorithm.")
    else:
        print("The password ans hashes do not match. Please recheck.")


def input_password():
    password = str(input("ENTER YOUR PASSWORD: \n"))
    password.encode("utf-8")
    return password


def input_hashes():
    return str(input("ENTER YOUR PASSWORD: \n"))


def main():
    print("|                PASSWORD HASHER AND CHECKER            |")
    print("| A TOOL TO CHECK SHA512 AND SHA382 HASHES OF PASSWORDS |")
    print("|                  CREATED BY AGNI DATTA                |")
    print("")
    print(" Please enter\n1 for just finding hashes of your passwords.\n2 for comparing and finding hashes of your passwords.")
    options = int(input())

    if (options == 1):
        password = input_password()
        print("SHA512 HASH: ")
        SHA512_hash(password)
        print("SHA384 HASH: ")
        SHA384_hash(password)
        print("\r")
    elif (options == 2):
        password = input_password()
        hashes = input_hashes()
        compare_hashes(password, hashes)
    else:
        print(" You entered an incorrect option. Please try again.")


main()