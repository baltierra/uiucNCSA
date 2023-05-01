import json
from datetime import datetime

# Function to replace vowels with their corresponding order number in alphabetical sequence
def replace_vowels_with_order_numbers(s):
    vowel_order = {'a': '1', 'e': '5', 'i': '9', 'o': '15', 'u': '21'}
    replaced_string = ''.join([vowel_order[char.lower()] if char.lower() in vowel_order else char for char in s])
    return replaced_string

# Function to count consonants in a string
def count_consonants(s):
    vowels = "aeiou"
    consonant_count = sum([1 for char in s.lower() if char.isalpha() and char not in vowels])
    return consonant_count

# Function to count vowels in a string
def count_vowels(s):
    vowels = "aeiou"
    vowel_count = sum([1 for char in s.lower() if char.isalpha() and char in vowels])
    return vowel_count

# Function to validate the input string
def is_valid_input(s):
    return all(char.isalpha() or char.isspace() for char in s)

# Function to process the input string and print the resulting string and consonant count
def process_input(input_string, data):
    replaced_string = replace_vowels_with_order_numbers(input_string)
    consonant_count = count_consonants(input_string)
    vowel_count = count_vowels(input_string)
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")

    print("\nResulting string:", replaced_string)
    print("Total number of consonants:", consonant_count, "\n")

    normalized_string = input_string.lower()
    if normalized_string in data:
        data[normalized_string]['times_used'] += 1
    else:
        data[normalized_string] = {
            "string": input_string,
            "length": len(input_string),
            "vowels_number": vowel_count,
            "consonant_numbers": consonant_count,
            "last_time_used": current_time,
            "times_used": 1
        }

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

# Main function to control program flow
def main():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    initial_string = "National Center for Supercomputing Applications"
    process_input(initial_string, data)

    while True:
        menu_option = input("Do you want to continue? (y/n): ").lower()
        if menu_option == 'y':
            user_string = input("\nEnter a new string: ")
            while not is_valid_input(user_string):
                print("Invalid input. Please enter a string containing only letters.")
                user_string = input("\nEnter a new string: ")
            process_input(user_string, data)
        elif menu_option == 'n':
            print("\nThank you for using the program. Goodbye!")
            break
        else:
            print("\nInvalid input. Please enter 'y' or 'n'.")

# Entry point of the program
if __name__ == "__main__":
    main()
