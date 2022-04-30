import random

number_of_games = 0
current_score = 0
sum = 0
print("1) Roll Dice")
print("2) Leave game")
dice = 0
choice=input('Enter your choice')

    
while True:    
    while True:
        dice = random.randint(1, 6)
        if choice == '1':
         print("you have rolled a",dice)
        current_score += dice
        print("your current score is",current_score)
        number_of_games += 1
          

        if choice == '2':
         print("Goodbye")
        break

    if number_of_games == 3:
        print("your final score is", current_score)
        break
      
if current_score == 18:
    print("You won the game with the highest score")

if current_score>12 :
    print("You scored a high score")
      
if current_score<12 or current_score == 12:
    print("You didn't score as high and should play again")
     
   

