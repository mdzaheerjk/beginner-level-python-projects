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
game=(rock,paper,scissors)
computer_select=random.choice(game)
your_select=str(input(f"what do you want to choice rock, paper,scissors\n" ))
print(f"computer chooses{computer_select}")
print(f"your choice  ")
if your_select=="rock":
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif your_select=="paper":
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
     
          
''')
elif your_select=="scissors":
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)     
          
''')
else:
    print("wrong input")
if your_select=="rock" and computer_select==rock:
    print("match draw")
elif your_select=="paper" and computer_select==paper:
    print("match draw")
elif your_select=="scissors" and computer_select==scissors:
    print("match draw")
elif your_select=="rock"  and computer_select==scissors:
    print("you won")
elif your_select=="rock" and computer_select==paper:
    print("you lost")
elif your_select=="paper" and computer_select==rock:
    print("you won")
elif your_select=="paper" and computer_select==scissors:
    print("you lost")
elif your_select=="scissors" and computer_select==rock:
    print("you lost")
elif your_select=="scissors" and computer_select==paper:
    print("you won")