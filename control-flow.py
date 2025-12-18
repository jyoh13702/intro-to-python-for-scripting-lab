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
    else:
        print("Wear light clothing.")
# Call the function
weather_advice()

def determine_season():
    month_str = input("Enter the month of the year (Jan - Dec): ")
    day_str = input("Enter the day of the month: ")
    try:
        day = int(day_str)
        month_map = {
            'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
            'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
            'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
        }
        month = month_map[month_str.capitalize()]
        season = ""
        if (month == 12 and day >= 21) or (month == 3 and day <= 19) or (month < 3 and day < 31):
            season = "Winter"
        elif (month == 3 and day >= 20) or (month == 6 and day <= 20) or (month < 6 and day < 31):
            season = "Spring"
        elif (month == 6 and day >= 21) or (month <= 9 and day <= 21):
            season = "Summer"
        elif (month == 9 and day >= 22) or (month <= 12 and day <= 20):
            season = "Fall"
        else:
            print(f"Error: Invalid date entered: {month_str} {day_str}")
            return
        print(f"{month_str.capitalize()} {day_str} is in {season}.")

    except ValueError:
        print("Error: Invalid day input. Please enter a number.")
    except KeyError:
        print("Error: Invalid month input. Please use a three-character abbreviation (Jan - Dec).")
# Call the function
determine_season()