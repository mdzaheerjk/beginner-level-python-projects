import random
lives=6
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
''')
word_list=[
"Apple",
"Train",
"Chair",
"Horse",
"Pizza",
"Rocket",
"Laptop",
"Tunnel",
"Python",
"Jungle"
]
ascii=['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
 '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========''']
computer_choice=random.choice(word_list).lower()
print(computer_choice)
place_holder=""
for i in range(0,len(computer_choice)):
    place_holder+="_"
print(place_holder)
letter_guess=[]
game_over=True
while game_over: 
    user_guess=input("guess a letter\n").lower()
    display=""
    if user_guess not in computer_choice:
        lives-=1
        print(f"you guessed {user_guess} which is not in the list you lost one life")
    print(f'''*****************{lives}/6*******************''')
    if user_guess in letter_guess:
        print(f"you guessed {user_guess} which you alreday guessed")
    for letters in computer_choice:
        if user_guess==letters:
            display+=letters
            letter_guess.append(user_guess)
        elif letters in letter_guess:
            display+=letters
        else:
            display+="_"
    if "_" not in display:
        print("you won!")
        game_over=False
    elif lives==0:
        print("you lost!")
        game_over=False
                
    print(display)
    print(ascii[lives])

        
    
