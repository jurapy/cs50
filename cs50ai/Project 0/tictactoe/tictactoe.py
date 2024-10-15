"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def tied(board):
    count = 0
    for row in board:
        for position in row:
            if position != EMPTY:
                count += 1
    if count == 9 and not winner(board):
        return True
    else:
        return False

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    counter = 0
    for row in board:
        for position in row:
            if position != EMPTY:
                counter += 1
    if counter == 9:
        return 1
    elif counter == 0 or counter % 2 == 0:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    
    for row in range(len(board)):
        for position in range(len(board)):
            if board[row][position] == EMPTY:
                possible_actions.add((row,position))
    if len(possible_actions) == 0:
        return 2
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise NotImplementedError
    row, position = action
    if not 0 <= row < 3 or not 0 <= position < 3:
        raise Exception('Out-of-bounds move')
    if board[row][position] != EMPTY:
        raise Exception('Posistion already taken!')
    else:
        new_board = copy.deepcopy(board)
        if player(board) == O:
            new_board[row][position] = O
        elif player(board) == X:
            new_board[row][position] = X
    return new_board

def winner(board):

    # rows and cols
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]
    
    # diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if tied(board) or winner(board) == X or winner(board) == O:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    current_player = player(board)
    
    if terminal(board):
        return None
    
    if current_player == X:
        value, move = max_value(board)
    else:
        value, move = min_value(board)
    
    return move

def max_value(board):
    if terminal(board):
        return utility(board), None
    
    v = float('-inf')
    best_action = None
    
    for action in actions(board):
        new_board = result(board, action)
        min_val, _ = min_value(new_board)
        if min_val > v:
            v = min_val
            best_action = action
    
    return v, best_action

def min_value(board):
    if terminal(board):
        return utility(board), None
    
    v = float('inf')
    best_action = None
    
    for action in actions(board):
        new_board = result(board, action)
        max_val, _ = max_value(new_board)
        if max_val < v:
            v = max_val
            best_action = action
    
    return v, best_action
