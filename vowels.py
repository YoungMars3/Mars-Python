# Open the file
with open("dictionary.txt", "r") as data_file:

    def clean_word(word):
        """Return word in lowercase stripped of whitespace."""
        return word.strip().lower()

    def get_vowels_in_word(word):
        """Return vowels in string word, including repeats."""
        vowel_str = "aeiou"
        vowels_in_word = [char for char in word if char in vowel_str]
        return ''.join(vowels_in_word)

    # Main program
    print("Find words containing vowels 'aeiou' in that order:")
    for word in data_file:
        word = clean_word(word)
        vowel_str = get_vowels_in_word(word) 
        if vowel_str == 'aeiou':
            print(word)
        