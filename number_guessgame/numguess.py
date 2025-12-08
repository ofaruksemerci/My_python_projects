import random
hard = 5
easy = 10
def randomnum():
  chosen = random.randint(1,101)
  return chosen


def num_guess_game ():
  known = False
  chosen_num = randomnum()
  print(" WELCOME TO NUMBER GUESS GAME ")
  print(" I AM THİNKİNG OF A NUMBER BETWEEN 1 TO 100 ")
  game_level = input("Choose a game level type hard or easy ").lower()
  if game_level == "hard":
      remaining_guess = hard
  else:
      remaining_guess = easy
  while not known:
    if (remaining_guess == 0 ):
      print("you are out of attemps YOU LOSE ")
      known = True
      
    print(f"You have {remaining_guess} attempts to find the number ")
    gues_num = int(input(" Enter your guess :"))
    
    if (gues_num == chosen_num ):
      print("Congrulations you correctly guessed the number \n")
      known = True
    elif gues_num < chosen_num:
      remaining_guess-=1
      print(" Please try bigger number.")
      
          
    else: 
      remaining_guess-=1
      print(" Please try a smaller number.")
     
      
while True:

  num_guess_game()
  response = input(" play to another gmae type 'y' if you do not want type 'n'  ").lower()
  if response == 'n':
    print("THANKS FOR PLAY")
    break



