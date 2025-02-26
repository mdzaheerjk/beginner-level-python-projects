import random
letters_2=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
symbols_2=["!","@","#","$","%","&","*"]
numbers_2=[1,2,3,4,5,6,7,8,9,0,]
passoword=[]
print("welcome to the pypassowrd generator")
lettres=int(input("how many letters you would like in your passoword\n"))
symbols=int(input("how many symbols you would like in your passoword\n"))
numbers=int(input("how many numbers you would like in your passoword\n"))
for i in range(0,lettres):
    passoword+=random.choice(letters_2)
for j in range(0,symbols):
    passoword+=random.choice(symbols_2)
for k in range(0,numbers):
    passoword+=str(random.choice(numbers_2))
print(passoword)
random.shuffle(passoword)
print(passoword)
shuffled="".join(passoword)
print(shuffled

