#import a random library and the logo

from random import randint
from logo import logo


#generate a random number from 1-100
def the_number():
    return randint(1,100)

 #check if typed letter for difficulty is correct  
def difficulty(check_level_answer):
    check_level = False
    while check_level== False:
        if check_level_answer == "E" or check_level_answer == "H":
            check_level= True         
        else:
            check_level_answer = input("Choose the correct level: ").upper()
 

#check if guess number is higher or lower from the generated random number
def guess_check(the_number,guess,lives):
    game = True
    while game:    
        if guess > the_number:
            lives = lives -1      
            guess = int(input("Too High. Guess again: "))
        elif guess < the_number:
            lives = lives -1
            guess = int(input("Too Low. Guess again: "))
            
        if guess == the_number:
            return "You win"       
        elif lives == 0:
            print(f"No more lives left. The random number is {the_number}")
            return "You lost" 
        elif lives == 1:
            print(f"You only have {lives} live left.")
        else:
            print(f"You only have {lives} lives left.")


play = True
while play:
#Welcome Message
    print(logo)
    level = input("Choose the level of difficlty. Type 'E' for easy and 'H' for hard : ").upper()
    difficulty(level)
# Choose the dificulty level between easy (10 lives) and hard(5 lives)
#Print the chosen difficulty
    if level == "E":
        lives = 10 
        print("You have 10 attempts to guess the number")            
    elif level == "H":
        lives = 5
    
        print("You have 5 attempts to guess the number")   
    number = the_number()
    print(number)
# guess a number
    guess = int(input("Make a Guess: "))
    print(guess_check(number,guess,lives))
    play_a_again = input("Type 'y' if you want to play again.  ").upper()
    
#ask user if he/she wants to play again
    if play_a_again == "Y":
        continue
    else:
        print("Goodbye. Have a nice day")
        exit()
    