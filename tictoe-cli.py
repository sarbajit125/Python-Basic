# Playing tic-toe game
import random


def willing():
    print("Want to quit Y or N")
    ans = input()
    if ans.upper() == 'N':
        return user_input(theboard,user_marker)
    else:
        print("Thank you for playing the game")


def print_board(theboard):
    print(theboard['top-l'] + ' | ' + theboard['top-m'] + ' | ' + theboard['top-r'])
    print('+-+-+-+-+')
    print(theboard['mid-l'] + ' | ' + theboard['mid-m'] + ' | ' + theboard['mid-r'])
    print('+-+-+-+-+')
    print(theboard['low-l'] + ' | ' + theboard['low-m'] + ' | ' + theboard['low-r'])


def boardplay(theboard, marker, marker_pos):
    if theboard[marker_pos] == ' ':
        theboard[marker_pos] = marker
        print_board(theboard)
        if rules(theboard):
            print("You have won the game")
            return 0
        Compplay(theboard)
    else:
        print(f"{marker_pos} is already filled choose a new one")
        user_input(theboard,user_marker)


def user_input(theboard, user_marker):
    print("lIST OF POSITION AVAILABLE TO FILLUP:")
    keys = [key for key in theboard.keys()]
    print(keys)
    print("Enter position name ")
    while True:
        user_marker_pos = input()
        if user_marker_pos in keys:
            print("Value to be entered in ", user_marker_pos)
            break
        print("entered position not in board, Fill once again ")
    boardplay(theboard, user_marker, user_marker_pos)


def rules(theboard):
    if theboard['top-l'] == theboard['top-m'] == theboard['top-r'] == 'x' or theboard['top-l'] == theboard['top-m'] == theboard['top-r'] == '0':
        return True
    elif theboard['mid-l'] == theboard['mid-m'] == theboard['mid-r'] == 'x' or theboard['mid-l'] == theboard['mid-m'] == theboard['mid-r'] == '0':
        return True
    elif theboard['low-l'] == theboard['low-m'] == theboard['low-r'] == 'x' or theboard['low-l'] == theboard['low-m'] == theboard['low-r'] == '0':
        return True
    elif theboard['top-l'] == theboard['mid-l'] == theboard['low-l'] == 'x' or theboard['top-l'] == theboard['mid-l'] == theboard['low-l'] == '0':
        return True
    elif theboard['top-m'] == theboard['mid-m'] == theboard['low-m'] == 'x' or theboard['top-m'] == theboard['mid-m'] == theboard['low-m'] == '0':
        return True
    elif theboard['top-r'] == theboard['mid-r'] == theboard['low-r'] == 'x' or theboard['top-r'] == theboard['mid-r'] == theboard['low-r'] == '0':
        return True
    elif theboard['top-l'] == theboard['mid-m'] == theboard['low-r'] == 'x' or theboard['top-l'] == theboard['mid-m'] == theboard['low-r'] == '0':
        return True
    elif theboard['top-r'] == theboard['mid-m'] == theboard['low-l'] == 'x' or theboard['top-r'] == theboard['mid-m'] == theboard['low-l'] == '0':
        return True


def Compplay(theboard):
    key = [item for item in theboard.keys()]
    while True:
        comp_choice = random.choice(key)
        if theboard[comp_choice] == ' ':
            theboard[comp_choice] = comp_marker
            break
    print("After Computer's Move:")
    print_board(theboard)
    if rules(theboard):
        print("Computer has won the game")
    willing()


print("TIC-TAC GAME".center(20,'-'))
theboard = {
    'top-l': ' ', "top-m": " ", "top-r": " ",
    "mid-l": " ", "mid-m": " ", "mid-r": " ",
    "low-l": " ", "low-m": " ", "low-r": " ",
}

print("Choose 'x' or '0'")
mark = str(input())
if mark == 'x':
    print("Player1:x and Computer:0")
    comp_marker = '0'
    user_marker = 'x'
    turns = 0
    user_input(theboard, user_marker)
else:
    print("Player1:0 and Computer:x")
    comp_marker = 'x'
    user_marker = '0'
    turns = 0
    user_input(theboard, user_marker)
