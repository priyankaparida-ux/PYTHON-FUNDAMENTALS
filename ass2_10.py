# NUMBER GUESSING GAME
def game(a,b = 30):
    if(a>b):
        print("Too high")
    elif(a<b):
        print("Too low")
    else:
        print("Correct")
a = int(input("Enter the number : "))
game(a,b=30)