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

def calculate_dog_years():
    user_input = input("Input the dog's age: ")
    try:
        human_Age = int(user_input)
        if human_Age < 0:
            print("Age cannot be a negative number.")
            return
        if human_Age <= 2:
            dog_Years = human_Age * 10
        else: 
            dog_Years = 20 + (human_Age - 2) * 7
        print(f"The dog's age in dog years is {dog_Years}.")
    except ValueError:
        print("Please input a valid age.")
# Call the function
calculate_dog_years()

def weather_advice():
    is_cold = input("Is it cold out? (yes/no): ").strip().lower()
    is_raining = input("Is it raining out? (yes/no): ").strip().lower()
    is_cold = (is_cold == 'yes')
    is_raining = (is_raining == 'yes')
    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    elif is_cold and not is_raining:
        print("Wear a warm coat.")
    elif not is_cold and is_raining:
        print("Carry an umbrella.")
    else: # not is_cold and not is_raining
        print("Wear light clothing.")
# Call the function
weather_advice()