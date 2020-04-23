def markup(s1,s2,s3,s4,s5,s6,s7,s8,s9,t,m1):
    if t=='1':
        s1=m1
    elif t=='2':
        s2=m1
        
    elif t=='3':
        s3=m1
       
    elif t=='4':
        s4=m1
        
    elif t=='5':
        s5=m1
        
    elif t=='6':
        s6=m1
      
    elif t=='7':
        s7=m1
       
    elif t=='8':
        s8=m1
        
    elif t=='9':
        s9=m1

    return(s1,s2,s3,s4,s5,s6,s7,s8,s9)

def check_win(s1,s2,s3,s4,s5,s6,s7,s8,s9):
    if s1=='x' and s2=='x' and s3=='x' or s1=='o' and s2=='o' and s3=='o' :
        return True
    elif s4=='x' and s5=='x' and s6=='x' or s4=='o' and s5=='o' and s6=='o' :
        return True
    elif s7=='x' and s8=='x' and s9=='x' or s7=='o' and s8=='o' and s9=='o' :
        return True
    elif s1=='x' and s4=='x' and s7=='x' or s1=='o' and s4=='o' and s7=='o' :
        return True
    elif s2=='x' and s5=='x' and s8=='x' or s2=='o' and s5=='o' and s8=='o' :
        return True
    elif s3=='x' and s6=='x' and s9=='x' or s3=='o' and s6=='o' and s9=='o' :
        return True
    elif s1=='x' and s5=='x' and s9=='x' or s1=='o' and s5=='o' and s9=='o' :
        return True
    elif s3=='x' and s5=='x' and s7=='x' or s3=='o' and s5=='o' and s7=='o' :
        return True
play=1    
while(play):        
    board='| 1 | 2 | 3 |\n-------------\n| 4 | 5 | 6 |\n-------------\n| 7 | 8 | 9 |'
    print("WELCOME TO TIC TAC TOE GAME")
    print(board)
    print("Do you want to play:\nEnter 1 to start the game:-\nEnter 0 to Quit the game:-")
    n=int(input())
    if n==1:
        m1=input("player 1 choose your markup x/o:-")
        m2="o" if m1=='x' else "x"
        print("Player 1 markup {}".format(m1))
        print("Player 2 markup {}".format(m2))
        turn=1
        pattern="| {} | {} | {} |\n-------------\n| {} | {} | {} |\n-------------\n| {} | {} | {} |"
        s1,s2,s3,s4,s5,s6,s7,s8,s9=' ',' ',' ',' ',' ',' ',' ',' ',' '
        turn_count=0
        while(True):
            if turn==1:
                p1=input("Turn of player1:-")
                turn_count+=1
                turn=0
                s1,s2,s3,s4,s5,s6,s7,s8,s9=markup(s1,s2,s3,s4,s5,s6,s7,s8,s9,p1,m1)
                print(pattern.format(s1,s2,s3,s4,s5,s6,s7,s8,s9))
                if(check_win(s1,s2,s3,s4,s5,s6,s7,s8,s9)):
                    print("Player1 has Won the game")
                    break
                elif turn_count==9:
                    print("Tie!!")
                    break
            else:
                p2=input("Turn of player2:-")
                turn=1
                turn_count+=1
                s1,s2,s3,s4,s5,s6,s7,s8,s9=markup(s1,s2,s3,s4,s5,s6,s7,s8,s9,p2,m2)
                print(pattern.format(s1,s2,s3,s4,s5,s6,s7,s8,s9))
                if(check_win(s1,s2,s3,s4,s5,s6,s7,s8,s9)):
                    print("Player2 has Won the game!!!!")
                    break
                elif turn_count==9:
                    print("Tie!!!")
                    break
        play=int(input("Want to play again?\nEnter 1 to start:-\nEnter 0 to quit:-"))
    else:
        print("Game closed successfully!!!!")
        play=0