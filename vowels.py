def clean_word(word):
    return word.strip().lower()

def has_vowels_in_order(word):
    vowels = "aeiou"
    previous_vowel_index = -1

    for char in word:
        if char in vowels:
            vowel_index = vowels.index(char)
            if vowel_index <= previous_vowel_index:
                return False
            previous_vowel_index = vowel_index

    return True

with open("dictionary.txt", "r") as data_file:
    print("Find words containing vowels 'aeiou' in that order:")
    for word in data_file:
        word = clean_word(word)
        print(f"Checking word: {word}")
        if len(word) <= 6:
            print(f"Skipping short word: {word}")
            continue
        if has_vowels_in_order(word):
            print(f"Found word: {word}")
#the code writen for this didnt work so i modified it and now it works