HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random

word_list = ["ardvark","baboon","camel"]
chosen_word = list(random.choice(word_list))
chosen_word_len = len(chosen_word)
lives = 6
display = []
for _ in range(chosen_word_len):
    display.append("_")
print(display)


end_of_game = False
while not end_of_game:
    guess = input("write down a letter you think is in the word").lower()
    for position in range(chosen_word_len):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]
    if guess not in chosen_word:
        lives-= 1
        if lives == 0:
            print("you lose\n",HANGMANPICS[6])
            end_of_game = True
        elif lives == 1:
            print(HANGMANPICS[5])
        elif lives == 2:
            print(HANGMANPICS[4])
        elif lives == 3:
            print(HANGMANPICS[3])
        elif lives == 4:
            print(HANGMANPICS[2])
        elif lives == 5:
            print(HANGMANPICS[1])
        elif lives == 6:
            print(HANGMANPICS[0])



    print(display)


    if "_" not in display:
        end_of_game = True
        print("YOU WIN")