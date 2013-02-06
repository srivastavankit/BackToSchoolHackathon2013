'''
Created on Feb 2, 2013

@author: anduril
'''
#!/usr/bin/python

# Head ends here

'''
Created on Feb 2, 2013

@author: anduril
'''
#!/usr/bin/python

# Head ends here

def checkFreeTurn(board):
    for i in range(len(board)):
        if board[i] == (len(board) - i):
            return i + 1
    return -1
        
def findRightmostSlot(board):
    for i in range(len(board)):
        if board[len(board)- 1 -i] != 0:
            return len(board) - i
        

def capture(board, board_opp):
    a = []
    for i in range(len(board)):        
        if board[i] == 0: a.append(i)
    pos=nos=0   #position of slot with 0, nos refers to number of marbles in the opposite slot.
    for i in a:
        for index in range(i):
            if board[index] == (i - index):
                if board_opp[len(board_opp)-1-i] > nos:
                    pos, nos = index+1, board_opp[len(board_opp)-1-i]
    if nos != 0: return pos
    else: return -1
                     
def chooseNextSlot(mancala, board, mancala_opp, board_opp):
    #check if there exists a hole that leads to a free turn.
    c = checkFreeTurn(board)    
    a = capture(board, board_opp)
    
    if c != -1 : slot = c
    elif a != -1: slot = a
    else: slot = findRightmostSlot(board)
    
    return slot

def printNextMove(player, player1Mancala, player1Marbles, player2Mancala, player2Marbles):
    if player == 1 :
        mancala, board = player1Mancala, player1Marbles
        mancala_opp, board_opp = player2Mancala, player2Marbles
    else :
        mancala, board = player2Mancala, player2Marbles
        mancala_opp, board_opp = player1Mancala, player1Marbles
    
    firstTurn = all(True if k == 4 else False for k in board)
    firstTurn_opp = all(True if k == 4 else False for k in board_opp)
    
    if firstTurn and firstTurn_opp:
        slot = 3
    else:
        slot = chooseNextSlot(mancala, board, mancala_opp, board_opp)
    
    return str(slot)


# Tail starts here
player = input()
mancala1 = input()
mancala1_marbles = [int(i) for i in raw_input().strip().split()]
mancala2 = input()
mancala2_marbles = [int(i) for i in raw_input().strip().split()]
print printNextMove(player, mancala1, mancala1_marbles, mancala2, mancala2_marbles)