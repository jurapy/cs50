from tictactoe import initial_state, tied, player, actions, result, winner, terminal, utility, minimax

X = 'X'
O = 'O'

board = initial_state()
board[0][0] = X
board[1][0] = O
board[0][1] = X
board[1][1] = O
board[2][0] = X
board[2][1] = O

board[0][2] = O
board[1][2] = X
board[2][2] = O

turn = player(board)

for i in range(3):
    print()
    for j in range(3):
        print(board[i][j],end=' ')

print()

#(actions(board))

print()

# first_actions = actions(board)
# for action in first_actions:
#     rezultat = result(board, action)
#     print(rezultat[0], rezultat[1], rezultat[2], sep='\n')
#     print()


winner(board)

terminal(board)

utility(board)

#action1 = (0, 2)

#result(board, action1)

print(tied(board))

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class Frontier(list):
    def remove(self):
        if len(self) > 0:
            self = self.pop(0)
    
    def contains_state(self, state):
        return any(node.state == state for node in self)

node = Node(1, None, None)

frontier = Frontier()
frontier.append(node)
print(frontier)

print(frontier.contains_state(2))