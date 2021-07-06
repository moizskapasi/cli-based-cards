"""
This module contains the code that makes a memory game. It uses the cards from the
cards.py module along with other methods.

Author: Moiz Shabbir Kapasi
"""

import cards #Importing the cards.py module
import time #Importing the time module for time elapsed

def make_flippable (card):
    """
    This function takes in a card tuple and returns a list with two elements, the False boolean
    value and the card tuple. This helps for the program to decide whether the card is face-up
    or face-down.
    """
    flippable = [False,card]
    return flippable

def is_match(card_1, card_2):
    """
    This function takes in two flippable cards. First it checks if both cards are turned face-up,
    only then checks if the two crads are the same. If the two crads are the same, it returns the
    boolean value True or else it will return the boolean value False
    """
    if card_1[0] == True and card_2[0] == True:
        if card_1[1][3] == card_2[1][3]:
            return True
    else:
        return False

def select_cards (number,deck):
    """
    This function returns a list of flippables from a deck of flippable cards according to the
    number of cards needed by the player. It first checks if the number of cards is not odd and
    not more than the cards available in a deck. Then it takes half of the number of unique cards
    and appends two copies of that card in the list.
    """
    if number%2 != 0 or number > 104:
        raise ValueError
    number=int(number/2)
    board=[]
    for i in range(number):
        board.append(deck[i].copy())
        board.append(deck[i].copy())
    return board

def make_board(row,column,deck):
    """
    This function takes in parameters for number of rows and columns and a flippable deck.
    It uses select_cards function to get a list of cards for the board. Then it uses nested for loops
    to convert that list and returns a 2D list for the board with the rows as the frist degree.
    """
    total_cards = row*column
    board_list = select_cards(total_cards,deck)
    cards.shuffle(board_list)
    board = []
    x=0
    for i in range(row):
        temp = []
        for j in range(column):
            temp.append(board_list[x])
            x+=1
        board.append(temp)
    return board

def remove_cards (board,row,column):
    """
    This is a helper function that replaces a card in the board with 0.
    """
    board[row-1][column-1] = 0

def make_faceup(board,row,column):
    """
    This a helper function changes the cards boolean value to True so that it is printed face-up.
    It raises a ValueError if it is already face-up.
    """
    if board[row-1][column-1] == "  " or board[row-1][column-1][0] == True:
        raise ValueError
    else:
        board[row-1][column-1][0] = True

def make_facedown(board,row,column):
    """
    This a helper function changes the cards boolean value to False so that it is printed
    face-down. It raises a ValueError if it is already face-down.
    """
    if board[row-1][column-1] == "  " or board[row-1][column-1][0] == False:
        raise ValueError
    else:
        board[row-1][column-1][0] = False

def print_board(board,row,column):
    """
    This function uses nested loops to traverse and print the 2D list, while using if statements
    to print face-down, empty space or the short hand (face-up)
    """
    for i in range(row):
        print("")
        for j in range(column):
            if board[i][j] == 0:
                print("  ",end="\t")
            elif board[i][j][0] == False:
                print("[-]",end="\t")
            else:
                print(board[i][j][1][3],end="\t")
        print("")

def make_move(board):
    """
    This function asks the player to enter the row and column number of their selected card.
    It will use try and except to make sure the input is right and then returns the row and column
    as a tuple.
    """
    try:
        print("")
        user_row = int(input("Please enter the row of your selected card: "))
        print("")
        user_column = int(input("Please enter the column of your selected card: "))
        print("")
        x=board[user_row-1][user_column-1]
    except ValueError:
        return make_move(board)
    except IndexError:
        return make_move(board)
    else:
        return user_row,user_column

def main():
    """
    This is the main function that handles how the game is played using all the functions
    defined. It also uses try and except to make sure the games doesn't run into an unknown
    error. This function uses counters to make sure the score is tallied, the timer is used and
    the game ends when the board is clear.
    """
    tic=time.perf_counter()
    score=0   
    try:
        row = int(input("Enter the number of rows you want: "))
        print("")
        column = int(input("Enter the number of columns you want: "))
        print("")
    except:
        print("Wrong input!!\nBye!")
        exit()
    count=row*column
    deck=cards.make_deck()
    cards.shuffle(deck)
    new_deck=[]
    for card in deck:
        new_deck.append(make_flippable(card))
    try:
        board=make_board(row,column,new_deck)
    except ValueError:
        print("You chose odd number of cards  or there are not enouugh cards in the deck.")
        exit()
    while count > 0:
        toc=time.perf_counter()
        print("Time Elapsed:",round(toc-tic,2))
        print("Score: %d"%(score))
        print("")
        print_board(board,row,column)
        print("")
        user_row_1,user_column_1 = make_move(board)
        print("")
        card_1=board[user_row_1-1][user_column_1-1]
        try:
            make_faceup(board,user_row_1,user_column_1)
        except ValueError:
            print("Wrong input!")
            exit()
        print("")
        print_board(board,row,column)
        print("")
        user_row_2,user_column_2 = make_move(board)
        print("")
        card_2=board[user_row_2-1][user_column_2-1]
        try:
            make_faceup(board,user_row_2,user_column_2)
        except ValueError:
            print("Wrong input!")
            exit()
        print("")
        print_board(board,row,column)
        print("")
        if is_match(card_1,card_2) == True:
            remove_cards(board,user_row_1,user_column_1)
            remove_cards(board,user_row_2,user_column_2)
            count-=2
            score +=1
        else:
            try:
                make_facedown(board,user_row_1,user_column_1)
                make_facedown(board,user_row_2,user_column_2)
            except ValueError:
                print("Wrong input!")
                exit()
        print("----------------------------------------------------------------------------------------------")
        print("")
    toc=time.perf_counter()
    print("Time Elapsed:",round(toc-tic,2))
    print("Score: %d"%(score))
    print("Game Over")

if __name__=="__main__": #Name guard for the main function to test the game
    main()
    input()
