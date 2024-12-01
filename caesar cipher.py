print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88  
''')
alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def caesar(encode_or_decode,text_message,shift_number):
    if encode_or_decode=="decode":
        shift_number*=-1
    result=""
    for letters in text_message:
        if letters not in alphabets:
            result+=letters
        else:
            if letters in alphabets:
                shift_index_number=(alphabets.index(letters)+shift_number)%len(alphabets)
                result+=alphabets[shift_index_number]
            else:
                result+=letters
    print(f"your {encode_or_decode}d result is {result}")
    
game_over=True
while game_over:
    user_input=input("type 'encode' to encrypt or type 'decode' to decrypt\n").lower()
    message=input("enter your message\n").lower()
    shift=int(input("enter the shift number\n"))
    caesar(encode_or_decode=user_input,text_message=message,shift_number=shift)
    start_again=input("type 'yes' if you want to go again or type 'no':\n").lower()
    if start_again=="no":
        print("good bye")
        game_over=False
