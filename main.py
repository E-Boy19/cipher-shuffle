import random

from os.path import join, exists
from os import makedirs

consonants = "bcdfghjklmnpqrstvwxz"
vowels = "aeiouy"   # y sounds like vowel

consonants_list = list(consonants)
vowels_list = list(vowels)

makedirs(join('data'), exist_ok=True)

filepath = join('data', 'data.data')

shuffled_consonants_list = consonants_list.copy()
random.shuffle(shuffled_consonants_list)
shuffled_vowels_list = vowels_list.copy()
random.shuffle(shuffled_vowels_list)

if not exists(filepath):
    with open(filepath, 'wb') as f:
        consonants_data = ''.join(shuffled_consonants_list)
        vowels_data = ''.join(shuffled_vowels_list)

        data = f'{vowels_data}|{consonants_data}'
        data = data.encode()

        f.write(data)

with open(filepath, 'rb') as f:
    data = f.read()
    data = data.decode()

    vowels_data, consonants_data = data.split('|')

    shuffled_consonants_list = list(consonants_data)
    shuffled_vowels_list = list(vowels_data)
    

def main():
    while True:
        original_message = input("Enter the text (or q to quit): ")
        translated_message = ""

        if original_message.lower() == 'q':
            break

        for char in original_message:
            caps = False
            if char.isupper():
                caps = True
                char = char.lower()

            if char in consonants_list:
                index = consonants_list.index(char)
                if caps:
                    translated_message += shuffled_consonants_list[index].upper()
                else:
                    translated_message += shuffled_consonants_list[index]
            elif char in vowels_list:
                index = vowels_list.index(char)
                if caps:
                    translated_message += shuffled_vowels_list[index].upper()
                else:
                    translated_message += shuffled_vowels_list[index]
            else:
                translated_message += char

        print(f'Translation : {translated_message}')


if __name__ == '__main__':
    main()
    input('Press enter to quit')
