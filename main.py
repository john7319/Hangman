
import random
from turtle import clear


from hangman_art import hang_man_arty
print(hang_man_arty)
from hangman_art import HANGMANPICS
from words import words_list
chosen_word = list(random.choice(words_list))
chosen_word_len = len(chosen_word)
# print(chosen_word)
lives = 6
display = []
for _ in range(chosen_word_len):
    display.append("_")
print(display)


end_of_game = False
while not end_of_game:
    guess = input("write down a letter you think is in the word").lower()
    clear()
    if guess in display:
        print(f"you've already guessed {guess},PLEASE TRY AGAIN")
    for position in range(chosen_word_len):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]

    if guess not in chosen_word:
        print(f"{guess} is what you guessed, and is not in the chosen word. So you lose a life. PLEASE TRY AGAIN")
        lives-= 1
        if lives == 0:
            print("You Lost\n",HANGMANPICS[6])
            print(chosen_word)
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

    # print(HANGMANPICS[lives])