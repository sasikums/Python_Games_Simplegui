# http://www.codeskulptor.org/#user39_jsVAq9YSFf_1.py
# Text implementation of Rock-Paper-Scissors-Lizard Spock

import random

#Converts name to number
def name_to_number(name):
    if name == "rock":
        number=0
    elif name=="Spock":
        number=1
    elif name=="paper":
        number=2
    elif name=="lizard":
        number=3
    elif name=="scissors":
        number=4
    else:
        number=-1000
    return number

def number_to_name(number):
    if number== 0:
        name="rock"
    elif number==1:
        name="Spock"
    elif number==2:
        name="paper"
    elif number==3:
        name="lizard"
    elif number==4:
        name="scissors"
    else:
        name="AAAA"
    return name

def rpsls(player_input):
    playnum = name_to_number(player_input)
    compnum = random.randint(0,4)
    compname = number_to_name(compnum)
    diff = (compnum-playnum)%5
    
    print "---------------------------------------New Game---------------------------------------"
    print "Player chooses " + player_input
    print "Computer chooses " + compname
    if diff in (1,2):
        print "Computer Wins!"
    elif diff in (3,4):
        print "Player Wins!"
    else:
        print "No Result. Its a Tie!!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



