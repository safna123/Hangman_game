#Step 1
import hangman_words
import hangman_art
import random
from replit import clear
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
# creating a empty list
display = []
for length in range(0,len(chosen_word)):
  display.append("_")
#Track the lives of the user
lives = 7
repeat_check = []
#Getting the input from user
endGame = False
while not endGame:
  guess = input("Guess the letter: ").lower()
  clear()
  for num,name in enumerate(chosen_word):
    if guess == name:
      display[num] = name
  if guess in repeat_check:
    print(f"You entered the same letter {guess} again. Try some other options.")
  else:
    if guess not in chosen_word:
      print(f"The letter {guess} is not in the word. You lose a life")
      lives -=1
      print(hangman_art.stages[lives])
    if "_" not in display:
      endGame = True
      print("You Win!\n Game Over")
    elif lives == 0:
      endGame = True
      print("You lose :(\n Game Over")
    else:
      print(display)
  repeat_check.append(guess)      
print(f"Correct word is {chosen_word} \nYou have {lives} lives left out")

