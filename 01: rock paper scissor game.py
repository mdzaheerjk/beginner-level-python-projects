import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_over=True
while game_over:
    ascii_list=[rock,paper,scissors]
    user_input=(input("what do you choose : rock,  paper or scissors\n"))
    computer_choice=random.choice(ascii_list)
    if user_input=="rock":
        print(rock)
    elif user_input=="paper":
        print(paper)
    else:
        print(scissors)
    print(computer_choice)

    if user_input=="rock" and computer_choice==rock:
        print(" you choose rock and computer choosed rock :match draw")
    elif user_input=="paper" and computer_choice==paper:
        print("you choose paper and computer choosed paper :match draw")
    elif user_input=="scissors" and computer_choice==scissors:
        print("you choose scissor and computer coosed scissor :match draw")
    elif user_input=="rock" and computer_choice==paper:
        print("you choose rock and computer choosed paper : computer wins")
    elif user_input=="rock" and computer_choice==scissors:
        print("you choose rock computer choosed scissor : you win")
    elif user_input=="paper" and computer_choice==rock:
        print("you choose paper and computer choosed rock :you win")
    elif user_input=="paper" and computer_choice==scissors:
        print("you choose paper and computer choosed scissor :computer wins")
    elif user_input=="scissor" and computer_choice==rock:
        print("you choose scissor and computer choosed rock : computer wins")
    elif user_input=="scissor" and computer_choice==paper:
        print("you choose scissor and computer choosed paper : you win")
    
    user_again_input=input("do you like to play agian type 'yes' or 'no'\n")
    if user_again_input=="no":
        print("thank you")
        game_over=False
        
