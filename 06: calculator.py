logo=''' 
_____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|'''
def addition(num1,num2):
    return num1+num2
def substraction (num1,num2):
    return num1-num2
def multiplication (num1,num2):
    return num1*num2
def division (num1,num2):
    if num2==0:
        return "cannot divide by zero"
    return num1/num2
operations={
    "+":addition,
    "-":substraction,
    "*":multiplication,
    "/":division
}
def calculator():
    should_continue=True
    while should_continue:
        print(logo)
        num1=float(input("enter the first number:\n"))
        while should_continue:
            for operators in operations:
                print(operators)
            picking_operator=input("pick the operator:\n")
            if picking_operator  not in ('+','-','*','/'):
                print("you selected wrong operator")
                should_continue=False
            num2=float(input("enter the next number:\n"))
            selected_operator=operations[picking_operator]
            answer=selected_operator(num1,num2)
            print(f"{num1}{picking_operator}{num2}={answer}")
            user_input=input(f"type 'y' to continue calculation with {answer} or type 'n' to start the new calculation or type 'o' end the calculation here only: \n")
            if user_input=="y":
                num1=answer
            elif user_input=="n":
                print("\n"*100)
                calculator()
            elif user_input=="o":
                print("thank you")
                should_continue=False
calculator()

