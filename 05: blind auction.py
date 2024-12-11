print('''                         
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
''')
data={}
def winner():
    winner_name=""
    maximum_amount=0
    for bids in data:
        amount_of_bidders=data[bids]
        if amount_of_bidders>maximum_amount:
            maximum_amount=amount_of_bidders
            winner_name=bids
    print(f"the winner is {winner_name} with amount of $ {maximum_amount}")
    
game_over=True
while game_over:
    name=input("enter your name\n").lower()
    bid=int(input("what is your bid $\n"))
    data[name]=bid
    left=input("are there any bidders left type 'yes' or 'no'\n").lower()
    if left=="yes":
        print("\n"*100)
    elif left=="no":
        print("\n"*100)
        winner()
        game_over=False
    
