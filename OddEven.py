import random
import time

summaryopen = open("summaryfile.txt", 'a')

def computerbowl():
    specify = summaryopen.write("player is batting \n")
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
        line3 = summaryopen.write(f"runs [{player_runs}] balls[{balls}] \n")
        time.sleep(2)

    print("You are out!")
    time.sleep(5)
    print("it's time for computer's batting")
    print("Getting things ready")
    time.sleep(5)

    specify2 = summaryopen.write("computer is batting \n") 
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
        line4 = summaryopen.write(f"runs [{computer_runs} balls [{balls}] \n#2")
        if computer_runs > player_runs:
            break

        time.sleep(2)
    summaryopen.close()

    if player_runs > computer_runs:
        print("You won")
        time.sleep(5)
        exit("GAME ENDED")
    elif player_runs < computer_runs:
        print("You lost")
        time.sleep(5)
        exit("GAME ENDED")



def computerbat():
    specify = summaryopen.write("computer is batting \n")
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
        line3 = summaryopen.write(f"runs [{computer_runs}] balls [{balls}] \n ")
        time.sleep(2)

    print("Computer is out!")
    time.sleep(5)
    print("it's time for your batting")
    print("getting things ready")

    specify2 = summaryopen.write("player is batting \n")
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
        line4 = summaryopen.write(f"runs [{player_runs}] balls [{balls}] \n")
        if player_runs > computer_runs:
            break 
        time.sleep(2)
    summaryopen.close()

    if player_runs > computer_runs:
        print("You Win!")
        time.sleep(5)
        exit("GAME ENDED")
    elif computer_runs > player_runs:
        print("You Lost")
        time.sleep(5)
        exit("GAME ENDED")



def playerbowl():
    specify = summaryopen.write("computer is batting \n")
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
        line3 = summaryopen.write(f"runs [{computer_runs}] balls [{balls}] \n ")
        time.sleep(2)

    print("Computer is out!")
    time.sleep(5)
    print("it's time for your batting")
    print("getting things ready")

    specify2 = summaryopen.write("player is batting \n")
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
        line4 = summaryopen.write(f"runs [{player_runs}] balls [{balls}] \n")
        if player_runs > computer_runs:
            break 
        time.sleep(2)
    summaryopen.close()

    if player_runs > computer_runs:
        print("You Win!")
        time.sleep(5)
        exit("GAME ENDED")
    elif computer_runs > player_runs:
        print("You Lost")
        time.sleep(5)
        exit("GAME ENDED")


def playerbat():
    specify = summaryopen.write("player is batting \n")
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
        line3 = summaryopen.write(f"runs [{player_runs}] balls[{balls}] \n")
        time.sleep(2)

    print("You are out!")
    time.sleep(5)
    print("it's time for computer's batting")
    print("Getting things ready")
    time.sleep(5)
 
    specify2 = summaryopen.write("computer is batting \n")
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
        line4 = summaryopen.write(f"runs [{computer_runs} balls [{balls}] \n")
        if computer_runs > player_runs:
            break 
        time.sleep(2)
    summaryopen.close()

    if player_runs > computer_runs:
        print("You won")
        time.sleep(5)
        exit("GAME ENDED")
    elif player_runs < computer_runs:
        print("You lost")
        time.sleep(5)
        exit("GAME ENDED")


print("WELCOME TO Cricket 2.0 \n -Added summaries \n -Bug fixes")
matchname = input("Type a word or scentence that you want to use as the title for this match: ")
line2 = summaryopen.write(f"     match: {matchname} \n \n")

runchoices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rulesorstart = ["rules", "start"]
start = ["start"]
oddorevenlist = ['odd', 'even']
tosswinchoices = ['bat', 'bowl']
computertossinput = int
tossinput = int
You = int
Computer = int


 
inputrulesorstart = str(input("type rules for rules \ntype start to start\n"))
while inputrulesorstart not in rulesorstart:
    inputrulesorstart = str(input("type rules for rules \ntype start to start\n"))
if inputrulesorstart == "rules":


    print('''Rules of the game \n
In this game you have to type a number for toss and so computer would. 
You choose either even or odd. If the sum or your choice and computer's run
choice is odd and you choose odd you win in the same way if it is even and  
you choose even you win and you get a chance to choose batting or bowling 
well if the computer won the toss (you choosed even and outcome is odd or  
you choosed odd and outcome is even) then computer would get a chance to choose 
if you are batting you have to type numbers from 1 to 10 and so computer has to 
if you are choosing a number different to computer's in a specific chance 
you score runs and they get added to your total runs if you get the same number 
as computer's then you would be out and the same thing is with bowling its just  
that computer would be batting and not you when your bowling is going on.\n\n''')
    afterrules = input("type start to start\n")
    while afterrules not in start:
        afterrules = input("type start to start\n")
    if afterrules == "start":
        pass

elif inputrulesorstart == "start":
    pass

 

tossinput = int(input("type any integer from 1 to 10: "))
while tossinput not in runchoices:
    tossinput = int(input("type any integer from 1 to 10: "))
oddoreven = input("choose odd or even: ")
while oddoreven not in oddorevenlist:
    oddoreven = input("choose odd or even: ")

computertossinput = int(random.choice(runchoices))
print(f"{computertossinput} is chosen by the computer")
sumtoss = int(tossinput+computertossinput)
print(f"{sumtoss} is the sum of toss")
sumresult = str

if sumtoss % 2 == 1:
        sumresult = "odd"
elif sumtoss % 2 == 0:
        sumresult = "even"

if sumresult == oddoreven:
    print("You won the toss")
    batorball = input("choose bat or bowl: ")
    while batorball not in tosswinchoices:
            batorball = input("choose bat or bowl: ")
    else:
            print(f"you choose {batorball}")
    if batorball == "bat":
            playerbat()
    if batorball == "bowl":
        playerbowl()                                       
        
else:
    print("You lost the toss")
    computerwinchoice = random.choice(tosswinchoices)
    print(f"computer has chosen to {computerwinchoice}")
    if computerwinchoice == "bat":
        computerbat()                                                           
    elif computerwinchoice == "bowl":
        computerbowl()  
                                                         
