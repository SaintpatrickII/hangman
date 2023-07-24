import random

possible_words = ['mango', 'pineapple', 'passionfruit', 'peach', 'orange']
# print(possible_words)

# print(random.choice(possible_words))

print(f'please choose a guess')
guess = input()
if guess.isalpha():
    print('good guess')
else:
    print('Oops! That is not a valid input.')
print('you have guessed:', guess)
