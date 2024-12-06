# Initials Program
def get_initials():
    name = input("Enter your first, middle, and last name: ")
    name_parts = name.split()
    initials = [part[0].upper() + "." for part in name_parts]
    print(" ".join(initials))

get_initials()

# Morse Code Converter
MORSE_CODE = {
    ' ': ' ', ',': '--..--', '.': '.-.-.-', '?': '..--..', '0': '-----', '1': '.----', 
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 
    'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
}

def to_morse_code():
    text = input("Enter a string to convert to Morse code: ").upper()
    morse = ' '.join([MORSE_CODE[char] for char in text if char in MORSE_CODE])
    print(morse)

to_morse_code()

# Alphabetic Telephone Number Translator
def translate_to_phone_number():
    TRANSLATOR = {
        'A': '2', 'B': '2', 'C': '2', 'D': '3', 'E': '3', 'F': '3', 
        'G': '4', 'H': '4', 'I': '4', 'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6', 'P': '7', 'Q': '7', 'R': '7', 
        'S': '7', 'T': '8', 'U': '8', 'V': '8', 'W': '9', 'X': '9', 
        'Y': '9', 'Z': '9'
    }
    phone_number = input("Enter a 10-character phone number (XXX-XXX-XXXX): ").upper()
    translated_number = ''.join(
        [TRANSLATOR[char] if char in TRANSLATOR else char for char in phone_number]
    )
    print(translated_number)

translate_to_phone_number()

# Vowels and Consonants Program
def count_vowels(string):
    vowels = 'AEIOUaeiou'
    return sum(1 for char in string if char in vowels)

def count_consonants(string):
    consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    return sum(1 for char in string if char in consonants)

def main():
    text = input("Enter a string: ")
    num_vowels = count_vowels(text)
    num_consonants = count_consonants(text)
    print(f"Vowels: {num_vowels}")
    print(f"Consonants: {num_consonants}")

main()
