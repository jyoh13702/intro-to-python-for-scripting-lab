def check_letter():
    letter = input("Enter a letter (a-z or A-Z): ")
    if not letter.isalpha() or len(letter) != 1:
        print("Invalid input. Please enter a single letter from A-Z.")
        return
    letter_lower = letter.lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    if letter_lower in vowels:
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")
# Call the function
check_letter()


def check_voting_eligibility():
    Voting_Age = 18
    Age = input("Please enter your age: ")
    while True:    
        try: 
            age = int(Age)
            if age < 0:
                print("Age cannot be negative.")
            elif age >= Voting_Age:
                print("You are eligible to vote.")
            else:
                print("You are not eligible to vote.")
            break
        except ValueError:
            print("Input a valid age.")
        break
# Call the function
check_voting_eligibility()