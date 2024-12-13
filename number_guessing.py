import random

logo='''  
                                                               $$\     $$\                                                                    $$\                           
                                                               $$ |    $$ |                                                                   $$ |                          
 $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\            $$$$$$\   $$$$$$$\   $$$$$$\                   $$$$$$$\  $$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$  __$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|           \_$$  _|  $$  __$$\ $$  __$$\                  $$  __$$\ $$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ /  $$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\               $$ |    $$ |  $$ |$$$$$$$$ |                 $$ |  $$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\              $$ |$$\ $$ |  $$ |$$   ____|                 $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$$ |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |             \$$$$  |$$ |  $$ |\$$$$$$$\                  $$ |  $$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |      
 \____$$ | \______/  \_______|\_______/ \_______/               \____/ \__|  \__| \_______|                 \__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|      
$$\   $$ |                                                                                                                                                                                
\$$$$$$  |                                                                                                                                                                                
 \______/  '''

def game_begin():
    run_again=True
    while run_again:
        game_over=True
        print(logo)
        print("welcome to the Number Guessing Game")
        print("i am thinking a number between 1 and 100")
        computer_guess = random.randint(1, 100)
        user_difficulty = str(input("Choose a difficulty . Type 'easy' or 'hard':\n ")).lower()

        if user_difficulty=="easy":
            lives=10
            while game_over:
                print(f"you have {lives} attempts remaining to guess the number")
                user_guess = int(input("make a guess :\n"))
                if user_guess<computer_guess:
                    print("too low")
                elif user_guess>computer_guess:
                    print("too high")


                if computer_guess==user_guess:
                    print(f"you got it! the answer was {computer_guess}")
                    game_over=False
                    run_again=False
                elif lives==1:
                    print("you run out of guesses :")
                    game_over=False
                    run_again=False
                elif computer_guess!=user_guess:
                    lives-=1
        elif user_difficulty=="hard":
            lives=5
            while game_over:
                print(f"you have {lives} attempts remaining to guess the number")
                user_guess = int(input("make a guess :\n"))
                if user_guess < computer_guess:
                    print("too low")
                elif user_guess > computer_guess:
                    print("too high")

                if computer_guess == user_guess:
                    print(f"you got it! the answer was {computer_guess}")
                    game_over = False
                    run_again=False
                elif lives == 1:
                    print("you run out of guesses :")
                    game_over = False
                    run_again=False
                elif computer_guess != user_guess:
                    lives -= 1
        else:
            print("you selected wrong dificulty level")
        user_input = str(input("want to play again type 'yes' or 'no'\n")).lower()
        if user_input == "no":
            print("thank you")
            run_again = False
        elif user_input == "yes":
            print("\n"*100)
            game_begin()
game_begin()







