import random


#Game Board...
def disp_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[7]+'|'+board[8]+'|'+board[9])
#test_board=['#','X','O','X','O','X','O','X','O','X']
#disp_board(test_board)


#function for player marker (X or O)...
def choose_marker():
    marker=''
    while not (marker=='X' or marker=='O'):
        marker=input("Player1:Do you want to be 'X' or 'O'?").upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
#mark=choose_marker()
#print(mark)


#function to assign player's marker (X or O) on the game board...
def pos(board,pos,marker):
    board[pos]=marker
#pos(test_board,4,'#')
#disp_board(test_board)


#function to check for win pattern...
def check(board,marker):
    if (board[1]==board[2]==board[3]==marker):
        return True
    elif (board[4]==board[5]==board[6]==marker):
        return True 
    elif (board[7]==board[8]==board[9]==marker):
        return True
    elif (board[1]==board[5]==board[9]==marker):
        return True
    elif (board[3]==board[5]==board[7]==marker):
        return True
    elif (board[1]==board[4]==board[7]==marker):
        return True
    elif (board[2]==board[5]==board[8]==marker):
        return True
    elif (board[3]==board[6]==board[9]==marker):
        return True
    else:
        return False
#print(check(test_board,'X'))

def checkdraw(board):
    """Check if game is draw"""
    if not ' ' in board:
        return True
    return False

#function to determine which player will start the game...
def first():
    if random.randint(0,1)==0:
        return 'Player1'
    else:
        return 'Player2'
def emp_space(board,pos):
    return board[pos]!='X' or board[pos]!='O'
def full_space(board):
    for i in range(1,10):
        if emp_space(board,i):
            return False
    return True


#function to seek position of player's marker...
def choose_pos(board):
    pos=0
    while pos not in [1,2,3,4,5,6,7,8,9] or not emp_space(board,pos):
        pos=int(input("Choose where you want to place your marker in range [1-9]"))
    return pos


#function to play again...
def play_again():
    pa=''
    while not (pa=='Y' or pa=='N'):
        pa= input("Do you want to play again?Y/N").upper();
    if pa=='Y':
        return True
    else:
        return False


#Ready function---main part...
def ready():
    pa=''
    while not (pa=='Y' or pa=='N'):
        pa= input("Are you ready to play?Y/N").upper();
    if pa=='Y':
        return True
    else:
        return False
print("Welcome to the Tic Tac Toe!!! Yeah this is my first game on Python ;)")
game=True
while True:
    gameboard=[' ']*10
    Sample=['0','1','2','3','4','5','6','7','8','9']
    player1_mk,player2_mk=choose_marker()
    
    turn=first()
    print(turn+' will start the game')
    st=ready()
    while st:
        if checkdraw(gameboard[1:]):
            print("Game Drawn")
            break
        if turn=='Player1':
            #Player 1's turn...
            print("Here's your sample board:")
            disp_board(Sample)
            print("Your game board...")
            disp_board(gameboard)
            mk_pos=choose_pos(gameboard)
            pos(gameboard,mk_pos,player1_mk)
            if check(gameboard,player1_mk):
                disp_board(gameboard)
                print("Congratulations "+turn+" has won the game!!!")
                st=False
            else:
                if full_space(gameboard):
                    disp_board(gameboard)
                    print("It's a draw!!!")
                    break
                else:
                    turn='Player2'
        if turn=='Player2':
            #Player 2's turn...
            print("Here's your sample board:")
            disp_board(Sample)
            print("Your game board...")
            disp_board(gameboard)
            mk_pos=choose_pos(gameboard)
            pos(gameboard,mk_pos,player2_mk)
            if check(gameboard,player2_mk):
                disp_board(gameboard)
                print("Congratulations player 2 has won the game!!!")
                st=False
            else:
                if not ' ' in gameboard :
                    disp_board(gameboard)
                    print("It's a draw!!!")
                    break
                else:
                    turn='Player1'
    if not play_again():
        break
