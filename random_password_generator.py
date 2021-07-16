# imports used for random function
import random
# import used to collect all letters, digits and special characters
import string

print("Hello! Welcome to the Random Password Generator!\n\n")

# while loop used to ask for a valid password count
while True:
        password_count = int(input("Enter the number of Passwords you want to create: "))
        if (password_count > 0):
            break
        else:
            print("Invalid password count! try again.")
            continue
print()

# for loop used to ask the same questions for the inputted number of passwords needed
for i in range(password_count):
    
    print("Password #", i+1)
    
    # while loop used to ask for a valid password length
    while True:
        password_length = int(input("Enter the Length of the Password: "))
        if (password_length > 0):
            break
        else:
            print("Invalid password length! try again.")
            continue

    # varibales used to find all letters, digits, and special characters
    letters = string.ascii_letters
    numbers = string.digits
    punctuation = string.punctuation

    # variables used to calculate all various combinations of characters
    all_characters = letters + numbers + punctuation
    letters_and_numbers = letters + numbers
    letters_and_punctuation = letters + punctuation
    numbers_and_punctuation = numbers + punctuation

    # while loop used to ask what characters are allowed and to generate a random password
    while True:

        # variables made to determine what characters are allowed
        letters_allowed = input("Are letters allowed (Y/N)? ").upper()
        numbers_allowed = input("Are numbers allowed (Y/N)? ").upper()
        punctuation_allowed = input("Are Symbols allowed (Y/N)? ").upper()
        print()

        # condiitonal statements used to determine how to form the randomized passwords
        if (letters_allowed == "Y" and numbers_allowed == "Y" and punctuation_allowed == "Y"):
            randomized_password = random.sample(all_characters , password_length)
            break
        elif (letters_allowed == "Y" and numbers_allowed == "Y" and punctuation_allowed == "N"):
            randomized_password = random.sample(letters_and_numbers , password_length)
            break
        elif (letters_allowed == "Y" and numbers_allowed == "N" and punctuation_allowed == "Y"):
            randomized_password = random.sample(letters_and_punctuation , password_length)
            break
        elif (letters_allowed == "N" and numbers_allowed == "Y" and punctuation_allowed == "Y"):
            randomized_password = random.sample(numbers_and_punctuation , password_length)
            break
        elif (letters_allowed == "Y" and numbers_allowed == "N" and punctuation_allowed == "N"):
            randomized_password = random.sample(letters , password_length)
            break
        elif (letters_allowed == "N" and numbers_allowed == "Y" and punctuation_allowed == "N"):
            randomized_password = random.sample(numbers , password_length)
            break
        elif (letters_allowed == "N" and numbers_allowed == "N" and punctuation_allowed == "Y"):
            randomized_password = random.sample(punctuation , password_length)
            break
        else:
            print("Password is empty! Try again")
            continue

    password = "".join(randomized_password)

    # prints password and increases count for the "for loop"
    print("Password #", i+1 , "is" , password)
    print()
    i+= 1

print("Thank you for using the Random Password Generator! Stay safe!")