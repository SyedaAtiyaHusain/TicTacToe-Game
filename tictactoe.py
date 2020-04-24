"""
Developed By: Syeda Atiya Husain
Requirement: Python version 3 or later
"""
from functions import *                                                     #importing necessary functions present in functions.py module.
play=1    
while(play):        
    board='| 1 | 2 | 3 |\n-------------\n| 4 | 5 | 6 |\n-------------\n| 7 | 8 | 9 |'
    print("WELCOME TO TIC TAC TOE GAME")
    print(board)
    print("Do you want to play:\nEnter 1 to start the game:-\nEnter 0 to Quit the game:-")
    n=int(input())                                                          #to check whether user wants to play or not
    if n==1:
        m1=input("player 1 choose your markup x/o:-")                       #to ask for the markup from the player1            
        m2="o" if m1=='x' else "x"
        print("Player 1 markup {}".format(m1))
        print("Player 2 markup {}".format(m2))
        turn=1
        pattern="| {} | {} | {} |\n-------------\n| {} | {} | {} |\n-------------\n| {} | {} | {} |"
        s1,s2,s3,s4,s5,s6,s7,s8,s9=' ',' ',' ',' ',' ',' ',' ',' ',' '
        turn_count=0
        while(True):
            if turn==1:                                                     #if it is turn of player 1
                p1=input("Turn of player1:-")
                turn_count+=1
                turn=0
                s1,s2,s3,s4,s5,s6,s7,s8,s9=markup(s1,s2,s3,s4,s5,s6,s7,s8,s9,p1,m1) #to place the markup in                                                                                             the board
                print(pattern.format(s1,s2,s3,s4,s5,s6,s7,s8,s9))                         
                if(check_win(s1,s2,s3,s4,s5,s6,s7,s8,s9)):                  #to check does the player1 won the                                                                                   match after his turn or not
                    print("Player1 has Won the game")
                    break
                elif turn_count==9:                                         #to check tie in game
                    print("Tie!!")
                    break
            else:
                p2=input("Turn of player2:-")                               #if it is turn of player 2
                turn=1
                turn_count+=1
                s1,s2,s3,s4,s5,s6,s7,s8,s9=markup(s1,s2,s3,s4,s5,s6,s7,s8,s9,p2,m2) #to place the markup in                                                                                            the board
                print(pattern.format(s1,s2,s3,s4,s5,s6,s7,s8,s9))
                if(check_win(s1,s2,s3,s4,s5,s6,s7,s8,s9)):                  #to check does the player1 won the                                                                                  match after his turn or not
                    print("Player2 has Won the game!!!!")
                    break
                elif turn_count==9:                                         #to check tie in game
                    print("Tie!!!")
                    break
        play=int(input("Want to play again?\nEnter 1 to start:-\nEnter 0 to quit:-")) #to ask if the players want                                                                                          to play again
    else:
        print("Game closed successfully!!!!")                                      
        play=0                                                              #to stop the game
