'''
Created on Nov 11, 2014

@author: Gabriel
'''
"""make comp win when there is two in a row and block when other player has two in a row some of the time"""
"""make games able to load again and again"""

import random, os, time; os.chdir("C:\\Users\Gabriel\Python_files")
play1_bool = False; play2_bool = False; tie_bool = False
play1_wins = 0; play2_wins = 0; tie_wins = 0
gamelist = []; filelist = []
    
class rows:
    def __init__(self, top_left, top_mid, top_right, mid_left, mid_mid, mid_right, bot_left, bot_mid, bot_right):
        self.top_l = top_left
        self.top_m = top_mid
        self.top_r = top_right
        self.mid_l = mid_left
        self.mid_m = mid_mid
        self.mid_r = mid_right
        self.bot_l = bot_left
        self.bot_m = bot_mid
        self.bot_r = bot_right
        
def Board(top_l, top_m, top_r, mid_l, mid_m, mid_r, bot_l, bot_m, bot_r):
    print("\n")
    print("|     |     |     |")
    print("| " + top_l + " | " + top_m + " | " + top_r + " |")
    print("|     |     |     |")
    print("===================")
    print("|     |     |     |")
    print("| " + mid_l + " | " + mid_m + " | " + mid_r + " |")
    print("|     |     |     |")
    print("===================")
    print("|     |     |     |")
    print("| " + bot_l + " | " + bot_m + " | " + bot_r + " |")
    print("|     |     |     |")

rows.top_l = " 7 "; rows.top_m = " 8 "; rows.top_r = " 9 "
rows.mid_l = " 4 "; rows.mid_m = " 5 "; rows.mid_r = " 6 "
rows.bot_l = " 1 "; rows.bot_m = " 2 "; rows.bot_r = " 3 "

with open("tictactoe.txt", "r") as file: filelist = [line for line in file]         #converting the file into a list

with open("tictactoe.txt", "r") as stats:       #Creating the game name list
    for line in stats:
        if (line.find("Name:") != -1):          #if a line has "Name:" in it, add the name to the list
            gamelist.append(line.split(": ")[1].strip())   
                           
if (len(gamelist) < 5):                         #Filling the remaining spaces with New Game
    for i in range(5 - len(gamelist)):
        gamelist.append("New Game")
                
name_of_game = int(input("(1)" + gamelist[0] + "\n(2)" + gamelist[1] + "\n(3)" + gamelist[2] + "\n(4)" + gamelist[3] + "\n(5)" + gamelist[4] + "\n"))

if (gamelist[name_of_game-1] != "New Game"):             #If the number selected was not New Game
    namepos = filelist.index("Name: " + gamelist[name_of_game-1] + "\n")
    play1_wins = int(filelist[namepos+1].split(": ")[1])
    play2_wins = int(filelist[namepos+2].split(": ")[1])
    tie_wins = int(filelist[namepos+3].split(": ")[1])
    if (filelist[namepos+2].split(": ")[0] == "Computer wins"):
        opponent = "1"
    elif (filelist[namepos+2].split(": ")[0] == "Player 2 wins"):
        opponent = "2"
else:
    create_game = input("What would you like to name your game: ")
    opponent = input("Would like like to play against\n(1)A Computer\n(2)A Friend\n")

while True:            
    if (opponent == "1"):                 #Coin flip
        sec_player = "Computer"
        OK = input("You will be player 1. Press enter to continue.\n")
        break
    elif (opponent == "2"):
        sec_player = "Player 2"
        OK = input("If the coin lands on heads, the youngest player will go first,\nif it lands on tails, the oldest player will go first. Press enter to continue.\n")
        coin = random.sample(["Heads, the youngest player is player 1", "Tails, the oldest player is player 1"], 1)
        print("".join(coin))
        break
    
print("\nType the number on the keypad that cooresponds to the spot you choose")

while True:                                                 #game mechanics
    while True:
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        user = input("Player 1's turn, X:  ")

        if (user == "7" and rows.top_l == " 7 "):
            rows.top_l = " X "; break
        elif (user == "8" and rows.top_m == " 8 "):
            rows.top_m = " X "; break
        elif (user == "9" and rows.top_r == " 9 "):
            rows.top_r = " X "; break
        elif (user == "4" and rows.mid_l == " 4 "):
            rows.mid_l = " X "; break
        elif (user == "5" and rows.mid_m == " 5 "):
            rows.mid_m = " X "; break
        elif (user == "6" and rows.mid_r == " 6 "):
            rows.mid_r = " X "; break
        elif (user == "1" and rows.bot_l == " 1 "):
            rows.bot_l = " X "; break
        elif (user == "2" and rows.bot_m == " 2 "):
            rows.bot_m = " X "; break
        elif (user == "3" and rows.bot_r == " 3 "):
            rows.bot_r = " X "; break
        else:
            print("You cant go there. Try again")

    #player 1 win conditions
    if (rows.top_l == " X " and rows.top_m == " X " and rows.top_r == " X "):
        play1_bool = True
        rows.top_l = "(X)"; rows.top_m = "(X)"; rows.top_r = "(X)"
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
    elif (rows.mid_l == " X " and rows.mid_m == " X " and rows.mid_r == " X "):
        play1_bool = True
        rows.mid_l = "(X)"; rows.mid_m = "(X)"; rows.mid_r = "(X)"
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
    elif (rows.bot_l == " X " and rows.bot_m == " X " and rows.bot_r == " X "):
        play1_bool = True
        rows.bot_l = "(X)"; rows.bot_m = "(X)"; rows.bot_r = "(X)"
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
    elif (rows.top_l == " X " and rows.mid_l == " X " and rows.bot_l == " X "):
        play1_bool = True
        rows.top_l = "(X)"; rows.mid_l = "(X)"; rows.bot_l = "(X)"
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
    elif (rows.top_m == " X " and rows.mid_m == " X " and rows.bot_m == " X "):
        play1_bool = True
        rows.top_m = "(X)"; rows.mid_m = "(X)"; rows.bot_m = "(X)"
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
    elif (rows.top_r == " X " and rows.mid_r == " X " and rows.bot_r == " X "):
        play1_bool = True
        rows.top_r = "(X)"; rows.mid_r = "(X)"; rows.bot_r = "(X)"
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
    elif (rows.top_l == " X " and rows.mid_m == " X " and rows.bot_r == " X "):
        play1_bool = True
        rows.top_l = "(X)"; rows.mid_m = "(X)"; rows.bot_r = "(X)"
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
    elif (rows.top_r == " X " and rows.mid_m == " X " and rows.bot_l == " X "):
        play1_bool = True
        rows.top_r = "(X)"; rows.mid_m = "(X)"; rows.bot_l = "(X)"
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
        
    #tie conditions
    if (rows.top_l != " 7 " and rows.top_m != " 8 " and rows.top_r != " 9 " and
        rows.mid_l != " 4 " and rows.mid_m != " 5 " and rows.mid_r != " 6 " and
        rows.bot_l != " 1 " and rows.bot_m != " 2 " and rows.bot_r != " 3 "):
        tie_bool = True
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
        
    Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        
    if (opponent == "1"):                         #Computer code
        print("The computers turn, O")
        time.sleep(2)
        
        while True:
            comp = str(random.randint(1, 9))
            if (comp == "7" and rows.top_l == " 7 "):
                rows.top_l = " O "; break
            elif (comp == "8" and rows.top_m == " 8 "):
                rows.top_m = " O "; break
            elif (comp == "9" and rows.top_r == " 9 "):
                rows.top_r = " O "; break
            elif (comp == "4" and rows.mid_l == " 4 "):
                rows.mid_l = " O "; break
            elif (comp == "5" and rows.mid_m == " 5 "):
                rows.mid_m = " O "; break
            elif (comp == "6" and rows.mid_r == " 6 "):
                rows.mid_r = " O "; break
            elif (comp == "1" and rows.bot_l == " 1 "):
                rows.bot_l = " O "; break
            elif (comp == "2" and rows.bot_m == " 2 "):
                rows.bot_m = " O "; break
            elif (comp == "3" and rows.bot_r == " 3 "):
                rows.bot_r = " O "; break
                
    elif (opponent == "2"):                   #Second player
            
        while True:
            Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
            
            user = input("Player 2's turn, O:  ")
            if (user == "7" and rows.top_l == " 7 "):
                rows.top_l = " O "; break
            elif (user == "8" and rows.top_m == " 8 "):
                rows.top_m = " O "; break
            elif (user == "9" and rows.top_r == " 9 "):
                rows.top_r = " O "; break
            elif (user == "4" and rows.mid_l == " 4 "):
                rows.mid_l = " O "; break
            elif (user == "5" and rows.mid_m == " 5 "):
                rows.mid_m = " O "; break
            elif (user == "6" and rows.mid_r == " 6 "):
                rows.mid_r = " O "; break
            elif (user == "1" and rows.bot_l == " 1 "):
                rows.bot_l = " O "; break
            elif (user == "2" and rows.bot_m == " 2 "):
                rows.bot_m = " O "; break
            elif (user == "3" and rows.bot_r == " 3 "):
                rows.bot_r = " O "; break
            else:
                print("You cant go there. Try again")
          
    #player 2 win conditions  
    if (rows.top_l == " O " and rows.top_m == " O " and rows.top_r == " O "):
        play2_bool = True
        rows.top_l = "(O)"; rows.top_m = "(O)"; rows.top_r = "(O)"
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
    elif (rows.mid_l == " O " and rows.mid_m == " O " and rows.mid_r == " O "):
        play2_bool = True
        rows.mid_l = "(O)"; rows.mid_m = "(O)"; rows.mid_r = "(O)"
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
    elif (rows.bot_l == " O " and rows.bot_m == " O " and rows.bot_r == " O "):
        play2_bool = True
        rows.bot_l = "(O)"; rows.bot_m = "(O)"; rows.bot_r = "(O)"
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
    elif (rows.top_l == " O " and rows.mid_l == " O " and rows.bot_l == " O "):
        play2_bool = True
        rows.top_l = "(O)"; rows.mid_l = "(O)"; rows.bot_l = "(O)"
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
    elif (rows.top_m == " O " and rows.mid_m == " O " and rows.bot_m == " O "):
        play2_bool = True
        rows.top_m = "(O)"; rows.mid_m = "(O)"; rows.bot_m = "(O)"
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
    elif (rows.top_r == " O " and rows.mid_r == " O " and rows.bot_r == " O "):
        play2_bool = True
        rows.top_r = "(O)"; rows.mid_r = "(O)"; rows.bot_r = "(O)"
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
    elif (rows.top_l == " O " and rows.mid_m == " O " and rows.bot_r == " O "):
        play2_bool = True
        rows.top_l = "(O)"; rows.mid_m = "(O)"; rows.bot_r = "(O)"
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
    elif (rows.top_r == " O " and rows.mid_m == " O " and rows.bot_l == " O "):
        play2_bool = True
        rows.top_r = "(O)"; rows.mid_m = "(O)"; rows.bot_l = "(O)"
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
        
    #tie conditions
    if (rows.top_l != " 7 " and rows.top_m != " 8 " and rows.top_r != " 9 " and
        rows.mid_l != " 4 " and rows.mid_m != " 5 " and rows.mid_r != " 6 " and
        rows.bot_l != " 1 " and rows.bot_m != " 2 " and rows.bot_r != " 3 "):
        tie_bool = True
        Board(rows.top_l, rows.top_m, rows.top_r, rows.mid_l, rows.mid_m, rows.mid_r, rows.bot_l, rows.bot_m, rows.bot_r)
        break
            
if (play1_bool == True): 
    print("PLAYER 1 WINS!!")
    play1_wins+=1
elif (play2_bool == True):
    print(sec_player.upper() + " WINS!!")
    play2_wins+=1
elif (tie_bool == True):
    print("IT'S A TIE!!")
    tie_wins+=1
    
if (gamelist[name_of_game - 1] != "New Game"):                #if person did not choose New Game
    filelist[namepos + 1] = "Player 1 wins: " + str(play1_wins)
    filelist[namepos + 2] = sec_player + " wins: " + str(play2_wins)
    filelist[namepos + 3] = "Ties: " + str(tie_wins)
    with open("tictactoe.txt", "w") as stats:
        print((elemt for elemt in filelist), file=stats)
else:                                                       #if person chose new game
    with open("tictactoe.txt", "a") as stats:
        print("Name: " + create_game + "\nPlayer 1 wins: " + str(play1_wins) + "\n" + sec_player + " wins: " + str(play2_wins) + "\nTies: " + str(tie_wins) + "\n", file=stats)
    
