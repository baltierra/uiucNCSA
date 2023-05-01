# Replace vowels with their corresponding order number in alphabetical sequence
def replace_vowels(s):
    vowel_order = {'a': '1', 'e': '5', 'i': '9', 'o': '15', 'u': '21'}
    replaced_string = ''.join([vowel_order[char.lower()] if char.lower() in vowel_order else char for char in s])
    return replaced_string


# Count consonants in a string
def count_consonants(s):
    vowels = "aeiou"
    consonant_count = sum([1 for char in s.lower() if char.isalpha() and char not in vowels])
    return consonant_count


# Main function to control program flow
def main():
    print("************************************")
    print("*      VOWELS/NUMBER SWAPPER       *")
    print("************************************\n")
    
    print("This program takes the string \"National Center for Supercomputing Applications,\"")
    print("replace the vowels for its order number in alphabetical sequence, and count the")
    print("consonants, displaying the result on screen.")
    
    initial_string = "National Center for Supercomputing Applications"
    print(f"\nResulting string: {replace_vowels(initial_string)}")
    print(f"Total number of consonants: {count_consonants(initial_string)}")


# Entry point of the program
if __name__ == "__main__":
    main()
