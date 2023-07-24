import random

possible_words = ['mango', 'pineapple', 'passionfruit', 'peach', 'orange']
# print(possible_words)

# print(random.choice(possible_words))


word = random.choice(possible_words)
# print(word)0
letters = list(word)
print(letters)

class hangman:
    def __init__(self, word, word_guessed, num_letters, num_lives, word_list, list_of_guesses):
        self.word = word
        self.word_guessed = word_guessed
        self.num_letters = num_letters
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = list_of_guesses
        pass



    def ask_for_input(self, letter):
        print('you have guessed:', letter)
        if not letter.isalpha():
            print(f'{letter} is not a letter, please enter a new letter')
            letter = input()
        else:    
            letter = letter.lower()
        return str(letter)


    def check_guess(self, guess):

        if guess in letters:
            print('good guess')
        else:
            print(f'{guess} is not in the word')
            

    

if __name__ == '__main__':
    print('please input a character:')
    hanging_about = hangman(word=random.choice(possible_words), word_guessed=['*']*len(word), num_letters=len(set(word)), num_lives=5, word_list=possible_words, list_of_guesses=[])
    new_guess = hanging_about.ask_for_input(input())
    hanging_about.check_guess(new_guess)