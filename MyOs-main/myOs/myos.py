import os 
import pyttsx3
# ====================================================================================================================================
# assistent app()
def assis_app():
    pyttsx3.speak("what can i do for u ")
    user_task1=input()

    if (('open'in user_task1)or ('run' in user_task1))and(("chrome" in user_task1)or('google chrome'in user_task1)):
        os.system("chrome")
    elif (('open'in user_task1)or ('run' in user_task1))and(("notepad" in user_task1)or('file'in user_task1)):
        os.system("notepad")
    elif (('open'in user_task1)or ('run' in user_task1))and(("vlc" in user_task1)or('video player'in user_task1)):
        os.system("vlc")
    elif(('play'in user_task1)or ('run' in user_task1))and(("song" in user_task1)or('music'in user_task1)):
        pyttsx3.speak(" baaaapu bapu sehat ke liye tu to hanikarak he hu to thodi daya to kar hu nahnhe balak he  ")
    else:
        print("enter correct sentence only music and open app is avilable ")

# "=============================================================================================================================="
#Implementation of Two Player Tic-Tac-Toe game in Python.

''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now we'll write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

# if __name__ == "__main__":
#     game()


# "======================================================================================================================"
# file app
def file_app():
    fd = "GFG.txt"

    # popen() is similar to open() 
    file = open(fd, 'w') 
    print('please write somthing ')
    a=input()
    file.write(a) 
    file.close() 
    file = open(fd, 'r') 
    text = file.read() 
    print(text) 

    # popen() provides a pipe/gateway and accesses the file directly 
    file = os.popen(fd, 'w') 
    file.write("Hello") 
    # File not closed, shown in next function. 




#========================================================================================================================
def image_app():
    print("this is google image pls type what image u want to search ")
    a=input(":-")
    os.system("chrome")



# =======================================================================================================================
def home_page():
    print("====================================================================================================")
    print(" press 1 to open a software and do task \n press 2 to open an assistent and talk with assistent \n press 3 for exit from myos app")
    
    print("====================================================================================================")
    a=int(input("::"))
    if a==1:
        a=input('press 1 for play game and \npress 2 for open any software\npress 3 for create file and save task')
        a=int(a)
        if a ==1:

            print(game())
        elif a==2:
            print("print 1 for open google search image \n press 2 for  open any software ")
            a=input()
            a=int(a)
            if a==1:
                print(image_app())
            elif a==2:
                print(softmenu())
        elif a==3:
            print(file_app())

    elif a==2:
        print(assis_app())
    elif a==3:
        for i in range(10):
            print("thanks to use our app buddy")
        print(exit())
# def open_software(self,name,value):
#     a=input('')
def softmenu():
    softlist=['chrome','notepad','paint']
    print(softlist)
    print('enter name of the software u want to open from the list')
    soft_value=input("::-")
    if soft_value not in softlist:
        print('you enter a wrong value pls rewrite it ')
    else:
        os.system(soft_value)

def mainrun():
    
    home_page()
    

mainrun()
# main()


