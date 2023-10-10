import random
import time
import pyautogui
from tkinter import *
from utils.fancystart import center


def shiijustgotreal():
    global startbutton,WelcomeLabel,Rules,game
    
    game = Tk()
    game.configure(bg='black')
    center(game)
    game.geometry("650x600")
    game.title("OddEven")

    WelcomeLabel = Label(game, text="Welcome To The OddEven Game!", font=("Arial",20,), 
                         width=50,height=5, bg='black', fg='white')
    WelcomeLabel.pack(anchor='n', pady=10,padx=10)
    Rules = Label(game, text='''What is this?
This is a game based on the Odd-Eve hand game except the opponent is a computer. 
How to play OddEven? 
First of all, like cricket the game starts off with a toss! The computer chooses a 
number 1-10 along with odd or eve, so does the player. If the sum of numbers of computer 
and player is odd, then the one who choses odd would win and same for even. After the toss 
they have to choses whether to bat or bowl. An innings will go until both the players choose 
the same number. If this happens, the batsman will be out.''',
                  bg='black', fg='white')
    Rules.pack(anchor='n',pady=15)

    startbutton = Button(game, text="START GAME", bg='green', fg='black', height=5, width=20,
                        font=("Arial",15,), command=enoughtryhardstyling)
    startbutton.pack(anchor='s',pady=15)
    
    game.mainloop()


def enoughtryhardstyling():
    Rules.pack_forget()
    startbutton.pack_forget()
    WelcomeLabel.pack_forget()
    toss()
    

def toss():
    TossLabel = Label(game, width=15,height=5, text="Toss",bg='black',fg='white',
                      font=("Arial",20,)).pack(anchor='n',pady=10)
    player_tossinput = 0
    computertossinput= random.choice(runchoices)
    player_tossinputx2 = 0
    computertossinputx2 = random.choice(oddorevenlist)

def computerbowl():
    player_runs = 0
    balls = 0
    playerrunchoice = int
    computerrunchoice = random.choice(runchoices)
    while computerrunchoice != playerrunchoice:
        playerrunchoice = int
        while playerrunchoice not in runchoices:
            playerrunchoice = int(input("type an integer from 1 to 10\n"))
        computerrunchoice = random.choice(runchoices)
        print(f"computer has chosen {computerrunchoice}")
        if computerrunchoice == playerrunchoice:
            break
        player_runs = player_runs + playerrunchoice
        balls = balls + 1
        print(str(player_runs)+" runs")
        print(str(balls)+" balls")
        time.sleep(2)

    print("You are out!")
    time.sleep(5)
    print("it's time for computer's batting")
    print("Getting things ready")
    time.sleep(5)


    computer_runs = 0
    balls = 0
    playerrunchoice = int
    computerrunchoice = random.choice(runchoices)
    while computerrunchoice != playerrunchoice:
        playerrunchoice = int
        while playerrunchoice not in runchoices:
            playerrunchoice = int(input("type any integer from 1 to 10\n"))
        computerrunchoice = random.choice(runchoices)
        print(f"computer has chosen {computerrunchoice}")
        if computerrunchoice == playerrunchoice:
            break
        computer_runs = computer_runs + computerrunchoice
        balls = balls + 1
        print(str(computer_runs)+" runs")
        print(str(balls)+" balls")
        if computer_runs > player_runs:
            break

        time.sleep(2)
    

    if player_runs > computer_runs:
        print("You won")
        time.sleep(5)
        exit("GAME ENDED")
    elif player_runs < computer_runs:
        print("You lost")
        time.sleep(5)
        exit("GAME ENDED")



def computerbat():
    
    computer_runs = 0
    balls = 0
    playerrunchoice = int
    computerrunchoice = random.choice(runchoices)
    while computerrunchoice != playerrunchoice:
        playerrunchoice = int
        while playerrunchoice not in runchoices:
            playerrunchoice = int(input("type any integer from 1 to 10\n"))
        computerrunchoice = random.choice(runchoices)
        print(f"computer has chosen {computerrunchoice}")
        if computerrunchoice == playerrunchoice:
            break 

        computer_runs = computer_runs + computerrunchoice
        balls = balls + 1
        print(str(computer_runs)+" runs")
        print(str(balls)+" balls")
        
        time.sleep(2)

    print("Computer is out!")
    time.sleep(5)
    print("it's time for your batting")
    print("getting things ready")

    
    player_runs = 0
    balls = 0
    playerrunchoice = int
    computerrunchoice = random.choice(runchoices)
    while computerrunchoice != playerrunchoice:
        playerrunchoice = int
        while playerrunchoice not in runchoices:
            playerrunchoice = int(input("type an integer from 1 to 10\n"))
        computerrunchoice = random.choice(runchoices)
        print(f"computer has chosen {computerrunchoice}")
        if computerrunchoice == playerrunchoice:
            break 
        player_runs = player_runs + playerrunchoice
        balls = balls + 1
        print(str(player_runs)+" runs")
        print(str(balls)+" balls")
        
        if player_runs > computer_runs:
            break 
        time.sleep(2)
    

    if player_runs > computer_runs:
        print("You Win!")
        time.sleep(5)
        exit("GAME ENDED")
    elif computer_runs > player_runs:
        print("You Lost")
        time.sleep(5)
        exit("GAME ENDED")



def playerbowl():
    
    computer_runs = 0
    balls = 0
    playerrunchoice = int
    computerrunchoice = random.choice(runchoices)
    while computerrunchoice != playerrunchoice:
        playerrunchoice = int
        while playerrunchoice not in runchoices:
            playerrunchoice = int(input("type any integer from 1 to 10\n"))
        computerrunchoice = random.choice(runchoices)
        print(f"computer has chosen {computerrunchoice}")
        if computerrunchoice == playerrunchoice:
            break 

        computer_runs = computer_runs + computerrunchoice
        balls = balls + 1
        print(str(computer_runs)+" runs")
        print(str(balls)+" balls")
        
        time.sleep(2)

    print("Computer is out!")
    time.sleep(5)
    print("it's time for your batting")
    print("getting things ready")

    
    player_runs = 0
    balls = 0
    playerrunchoice = int
    computerrunchoice = random.choice(runchoices)
    while computerrunchoice != playerrunchoice:
        playerrunchoice = int
        while playerrunchoice not in runchoices:
            playerrunchoice = int(input("type an integer from 1 to 10\n"))
        computerrunchoice = random.choice(runchoices)
        print(f"computer has chosen {computerrunchoice}")
        if computerrunchoice == playerrunchoice:
            break 
        player_runs = player_runs + playerrunchoice
        balls = balls + 1
        print(str(player_runs)+" runs")
        print(str(balls)+" balls")
        
        if player_runs > computer_runs:
            break 
        time.sleep(2)
    

    if player_runs > computer_runs:
        print("You Win!")
        time.sleep(5)
        exit("GAME ENDED")
    elif computer_runs > player_runs:
        print("You Lost")
        time.sleep(5)
        exit("GAME ENDED")


def playerbat():
    
    player_runs = 0
    balls = 0
    playerrunchoice = int
    computerrunchoice = random.choice(runchoices)
    while computerrunchoice != playerrunchoice:
        playerrunchoice = int
        while playerrunchoice not in runchoices:
            playerrunchoice = int(input("type an integer from 1 to 10\n"))
        computerrunchoice = random.choice(runchoices)
        print(f"computer has chosen {computerrunchoice}")
        if computerrunchoice == playerrunchoice:
            break
        player_runs = player_runs + playerrunchoice
        balls = balls + 1
        print(str(player_runs)+" runs")
        print(str(balls)+" balls")
        
        time.sleep(2)

    print("You are out!")
    time.sleep(5)
    print("it's time for computer's batting")
    print("Getting things ready")
    time.sleep(5)
 
    
    computer_runs = 0
    balls = 0
    playerrunchoice = int
    computerrunchoice = random.choice(runchoices)
    while computerrunchoice != playerrunchoice:
        playerrunchoice = int
        while playerrunchoice not in runchoices:
            playerrunchoice = int(input("type any integer from 1 to 10\n"))
        computerrunchoice = random.choice(runchoices)
        print(f"computer has chosen {computerrunchoice}")
        if computerrunchoice == playerrunchoice:
            break
        computer_runs = computer_runs + computerrunchoice
        balls = balls + 1
        print(str(computer_runs)+" runs")
        print(str(balls)+" balls")
       
        if computer_runs > player_runs:
            break 
        time.sleep(2)
    

    if player_runs > computer_runs:
        print("You won")
        time.sleep(5)
        exit("GAME ENDED")
    elif player_runs < computer_runs:
        print("You lost")
        time.sleep(5)
        exit("GAME ENDED")


# print("WELCOME TO Cricket 2.0 \n -Added summaries \n -Bug fixes")
# matchname = input("Type a word or scentence that you want to use as the title for this match: ")


runchoices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rulesorstart = ["rules", "start"]
start = ["start"]
oddorevenlist = ['odd', 'even']
tosswinchoices = ['bat', 'bowl']
computertossinput = int
tossinput = int
You = int
Computer = int


 
# inputrulesorstart = str(input("type rules for rules \ntype start to start\n"))
# while inputrulesorstart not in rulesorstart:
#     inputrulesorstart = str(input("type rules for rules \ntype start to start\n"))
# if inputrulesorstart == "rules":


#     print('''Rules of the game \n
# In this game you have to type a number for toss and so computer would. 
# You choose either even or odd. If the sum or your choice and computer's run
# choice is odd and you choose odd you win in the same way if it is even and  
# you choose even you win and you get a chance to choose batting or bowling 
# well if the computer won the toss (you choosed even and outcome is odd or  
# you choosed odd and outcome is even) then computer would get a chance to choose 
# if you are batting you have to type numbers from 1 to 10 and so computer has to 
# if you are choosing a number different to computer's in a specific chance 
# you score runs and they get added to your total runs if you get the same number 
# as computer's then you would be out and the same thing is with bowling its just  
# that computer would be batting and not you when your bowling is going on.\n\n''')
#     afterrules = input("type start to start\n")
#     while afterrules not in start:
#         afterrules = input("type start to start\n")
#     if afterrules == "start":
#         pass

# elif inputrulesorstart == "start":
#     pass

 

# tossinput = int(input("type any integer from 1 to 10: "))
# while tossinput not in runchoices:
#     tossinput = int(input("type any integer from 1 to 10: "))
# oddoreven = input("choose odd or even: ")
# while oddoreven not in oddorevenlist:
#     oddoreven = input("choose odd or even: ")

# computertossinput = int(random.choice(runchoices))
# print(f"{computertossinput} is chosen by the computer")
# sumtoss = int(tossinput+computertossinput)
# print(f"{sumtoss} is the sum of toss")
# sumresult = str

# if sumtoss % 2 == 1:
#         sumresult = "odd"
# elif sumtoss % 2 == 0:
#         sumresult = "even"

# if sumresult == oddoreven:
#     print("You won the toss")
#     batorball = input("choose bat or bowl: ")
#     while batorball not in tosswinchoices:
#             batorball = input("choose bat or bowl: ")
#     else:
#             print(f"you choose {batorball}")
#     if batorball == "bat":
#             playerbat()
#     if batorball == "bowl":
#         playerbowl()                                       
        
# else:
#     print("You lost the toss")
#     computerwinchoice = random.choice(tosswinchoices)
#     print(f"computer has chosen to {computerwinchoice}")
#     if computerwinchoice == "bat":
#         computerbat()                                                           
#     elif computerwinchoice == "bowl":
#         computerbowl()  
                                                         
