"""pig latin is an interesting python game. If a user inputs a word that starts with
a vowel, the program appends 'way' to the word. If the word starts with a consonant,
the program removes the consonants preceeding the first vowel, appends the consonants
to the end of the word and adds 'ay' at the end. Lets have fun with pig latin """
word = input("Enter a word: ")
vowels = ['a','e','i','o','u']
def translate(word):
    if len(word)>0 and word.isalpha():
        word.lower()
        if word[0] in vowels:
            word = word+'way'
            return word
        else:
            word.lower()
            for letter in word:
                if letter in vowels:
                    vowel_index = word.index(letter)
                    break
            word = word[vowel_index:]+word[:vowel_index]+'ay'
            return word
    else:
        print("Enter a correct word")
print(translate(word))

        
