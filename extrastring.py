# Vowels and Consonants from File
def count_vowels(string):
    vowels = 'AEIOUaeiou'
    return sum(1 for char in string if char in vowels)

def count_consonants(string):
    consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    return sum(1 for char in string if char in consonants)

def main():
    file_name = 'completeshakespear.txt'
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
        num_vowels = count_vowels(text)
        num_consonants = count_consonants(text)
        print(f"Vowels: {num_vowels}")
        print(f"Consonants: {num_consonants}")
    except FileNotFoundError:
        print(f"File {file_name} not found.")

main()

# Palindrome Finder
def is_palindrome(word):
    return word == word[::-1]

def find_palindromes(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read().lower()
        words = text.split()
        palindromes = [word for word in words if is_palindrome(word)]
        print(f"Number of palindromes: {len(palindromes)}")
        print("Palindromes found:")
        for palindrome in palindromes:
            print(palindrome)
    except FileNotFoundError:
        print(f"File {file_name} not found.")

find_palindromes('warandpeace.txt')


import random

# Encrypt and Decrypt Program
def encrypt_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
        key = random.randint(13, 255)
        encrypted_text = ''.join(chr((ord(char) + key) % 256) for char in text)
        encrypted_file = file_name.replace('.txt', '.enc')
        with open(encrypted_file, 'w', encoding='utf-8') as enc_file:
            enc_file.write(f"{key}\n{encrypted_text}")
        print(f"File encrypted as {encrypted_file} with key {key}.")
    except FileNotFoundError:
        print(f"File {file_name} not found.")

def decrypt_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        key = int(lines[0].strip())
        encrypted_text = ''.join(lines[1:])
        decrypted_text = ''.join(chr((ord(char) - key) % 256) for char in encrypted_text)
        decrypted_file = file_name.replace('.enc', '_decrypted.txt')
        with open(decrypted_file, 'w', encoding='utf-8') as dec_file:
            dec_file.write(decrypted_text)
        print(f"File decrypted as {decrypted_file}.")
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except ValueError:
        print("Invalid encryption key or file format.")

def main():
    while True:
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            file_name = input("Enter the file name to encrypt: ")
            encrypt_file(file_name)
        elif choice == '2':
            file_name = input("Enter the file name to decrypt: ")
            decrypt_file(file_name)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

main()
