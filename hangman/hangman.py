import random
from hangman_words import words
from hangman_art import hangman_stages,logo

lives = 6

print(logo)

chosen_word = random.choice(words)



placeholder=""
word_length = len(chosen_word)
for i in range(word_length):
  placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
  print(f"********************{lives}/6 LIVES LEFT ********************")
  guess = input("Make your guess: ").lower()

  if guess in correct_letters:
    print(f"you have already guessed {guess}")

  display =""

  for letter in chosen_word :
    if letter == guess:
      display +=letter
      correct_letters.append(guess)
    elif letter in correct_letters:
      display +=letter
    
  
    else:
        display += "_"

    
  print(display)

  if guess not in chosen_word:
    lives -=1
    print(f"you guessed {guess} and thats not in word ,you lose a life! ")
    if lives ==0:
      game_over =True
      print(f"********************ıt was {chosen_word }!you lose********************")
 
  if "_"not in display:
    game_over = True
    print("********************you win******************** ")
  
  print(hangman_stages[lives])