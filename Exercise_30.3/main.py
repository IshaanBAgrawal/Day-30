import pandas

nato_phonetics = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic = {row.letter: row.code for (index, row) in nato_phonetics.iterrows()}
game_is_on = True
while game_is_on:
    try:
        user_word = input("What is the word whose NATO Phonetic characters you want?: ").upper()
        user_word_list = [char for char in user_word if char != ' ']
        nato_phonetic_words_of_letters = [nato_phonetic[char] for char in user_word_list]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(f"Here is your NATO phonetic form of {user_word}: \n{nato_phonetic_words_of_letters}")
        game_is_on = False
