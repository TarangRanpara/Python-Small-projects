#Global scope
table = {
    
    '1':'1','2':'2','3':'3',
    '4':'4','5':'5','6':'6',
    '7':'7','8':'8','9':'9'
}

#for preventing repeatative same enteries
used_stack = []

#players
player_1 = 'x'
player_2 = 'O'

#for storing, who won
result = None

def show_table():
    global table
    
    print('\n\n')
    print(table['1'],'\t|\t',table['2'],'\t|\t',table['3'])
    print(''.rjust(34,'*'))
    print(table['4'],'\t|\t',table['5'],'\t|\t',table['6'])
    print(''.rjust(34,'*'))
    print(table['7'],'\t|\t',table['8'],'\t|\t',table['9'])
    
def player_move(move,sign):
    global table
    global used_stack
    
    used_stack.append(move)
    table[move] = sign
    
def win_the_game():
    global table
    
    if (
        (table['1']==table['2']==table['3']) or (table['4']==table['5']==table['6']) or (table['7']==table['8']==table['9']) or
        (table['1']==table['4']==table['7']) or (table['2']==table['5']==table['8']) or (table['3']==table['6']==table['9']) or
        (table['1']==table['5']==table['9']) or (table['3']==table['5']==table['7']) ):
        return True
    else:
        return False

def taking_turns(turn):
    print("\nNow it's Turn of,  ",turn)
    choice = input("Enter your choice:")

    while not (choice.isdecimal() and choice in table and (choice not in used_stack)):
        choice = input("\nEnter your choice properly:")
        
    player_move(choice,turn)

print("player 1: 'X'\nplayer 2: 'O'")
for i in range(0,9):
    if i%2==0:
        turn = player_1
        show_table()
        taking_turns(turn)
        
        if win_the_game() == True:
            result = turn
            break
    else:
        turn = player_2
        show_table()
        taking_turns(turn)

        if win_the_game() == True:
            result = turn
            break

print('\n\n',result,"Won the game!")
