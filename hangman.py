import random

possible_words = ['mango', 'pineapple', 'passionfruit', 'peach', 'orange']


# The hangman class initializes a game of hangman with a specified number of lives and a list of words
# to choose from.
class hangman:
    def __init__(self, num_lives, word_list):

        self.word = random.choice(word_list)

        self.word_guessed = ['*']*len(self.word)

        self.num_letters = len(set(self.word))

        self.num_lives = num_lives

        self.word_list = word_list

        self.list_of_guesses = []
        pass



    def ask_for_input(self):

        """
        The function asks the user for input, checks if the input is a single letter, and then checks if
        the letter has already been guessed.
        """

        letter = input('Please make a Guess: ')
        if not letter.isalpha() or len(letter) != 1:
            print(f'{letter} is not a individual character, please enter a new letter')
            letter = input()
        elif letter in self.list_of_guesses:    
            print(f'you have already tried {letter}!')
        else:
            self.check_guess(letter)
            self.list_of_guesses.append(letter)



    def check_guess(self, guess):

        """
        The function checks if a guessed letter is in a word and updates the game state accordingly.
        
        :param guess: The parameter "guess" is a string that represents the letter that the player is
        guessing

        """

        guess = guess.lower()
        if guess in self.word:
            print(f'good guess {guess} is in the word')
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            print(f'{guess} is not in the word')
            self.num_lives -= 1
            print(f'you have {self.num_lives} left')


def lets_play(word_list):
    """
    The function "lets_play" plays a game of hangman using a given word list.
    
    :param word_list: The `word_list` parameter is a list of words from which the hangman game will
    randomly select a word for the player to guess
    """
    num_lives = 5
    hanging_about = hangman(num_lives=num_lives, word_list=word_list)
    while True:
        if hanging_about.num_lives == 0:
            print('unlucky bozo')
            break
        elif hanging_about.num_letters > 0:
            print(hanging_about.word_guessed)
            hanging_about.ask_for_input()
        else:
            print('well done you win')
            print('the work was', hanging_about.word)
            break


    

if __name__ == '__main__':
    lets_play(possible_words)