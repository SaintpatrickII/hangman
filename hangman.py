import random

possible_words = ['mango', 'pineapple', 'passionfruit', 'peach', 'orange']
# print(possible_words)

# print(random.choice(possible_words))


word = random.choice(possible_words)
# print(word)0
letters = list(word)
print(letters)


def ask_for_input(letter):
    # print(letter)
    print('you have guessed:', letter)
    if not letter.isalpha():
        print(f'{letter} is not a letter, please enter a new letter')
        letter = input()
    else:    
        letter = letter.lower()
    return str(letter)

def check_guess(guess):

    if guess in letters:
        print('good guess')
    else:
        print(f'{guess} is not in the word')
        

    

if __name__ == '__main__':
    print('please input a character:')
    new_guess = ask_for_input(input())
    check_guess(new_guess)