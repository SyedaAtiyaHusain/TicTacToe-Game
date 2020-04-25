def markup(s1,s2,s3,s4,s5,s6,s7,s8,s9,t,m1):
    
    """
    This function is defined to mark the markup which has choosen by the user 
    at user's desired position condition provided that the desired position should be empty.
    """
    
    if t=='1':
        if s1==" ":
            s1=m1
        else:
            print("Already marked at this position.You have wasted your turn.")
    elif t=='2':
        if s2==" ":
            s2=m1
        else:
            print("Already marked at this position.You have wasted your turn.")   
    elif t=='3':
        if s3==" ":
            s3=m1
        else:
            print("Already marked at this position.You have wasted your turn.")   
    elif t=='4':
        if s4==" ":
            s4=m1
        else:
            print("Already marked at this position.You have wasted your turn.")       
    elif t=='5':
        if s5==" ":
            s5=m1
        else:
            print("Already marked at this position.You have wasted your turn.")
    elif t=='6':
        if s6==" ":
            s6=m1
        else:
            print("Already marked at this position.You have wasted your turn.")   
    elif t=='7':
        if s7==" ":
            s7=m1
        else:
            print("Already marked at this position.You have wasted your turn.")
    elif t=='8':
        if s8==" ":
            s8=m1
        else:
            print("Already marked at this position.You have wasted your turn.")
    elif t=='9':
        if s9==" ":
            s9=m1
        else:
            print("Already marked at this position.You have wasted your turn.")
    return(s1,s2,s3,s4,s5,s6,s7,s8,s9)

def check_win(s1,s2,s3,s4,s5,s6,s7,s8,s9):
    
    """
    This function is defined to check which player has win the match.
    This function is called after every turn of the player to keep a check at every turn of the player and if at any point,
    it found to get any winning condition true then it will return True for that particular player 
    """
    
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
