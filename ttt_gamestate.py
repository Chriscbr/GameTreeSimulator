import copy


class TTTGameState:
    """Class that represents a Tic-Tac-Toe (TTT) game state.

    Contains methods for determining whether the current state is valid,
    and creating a list of all possible game states that can follow.

    Constant variables EMPTY, X, and O represent the fundamental states
    for each position of a TTT board, and ALLY and ENEMY represent
    which player is to move next (ALLY = X, ENEMY = O)."""

    EMPTY = 0
    X = 1
    O = 2

    ALLY = 0
    ENEMY = 1

    def __init__(self, board=None, to_move=None):
        if board is None:
            self.board = [[TTTGameState.EMPTY for x in range(0, 3)]
                          for x in range(0, 3)]
        else:
            self.board = board

        if to_move is None:
            self.to_move = TTTGameState.ALLY
        else:
            self.to_move = to_move

    # returns if current board state is valid
    # doesn't check if state is specifically "reachable" through gameplay
    def is_valid_state(self):
        if not (self.to_move == TTTGameState.ALLY
                or self.to_move == TTTGameState.ENEMY):
            return False
        if len(self.board) != 3:
            return False
        for i in range(0, 3):
            if len(self.board[i]) != 3:
                return False
            for j in range(0, 3):
                val = self.board[i][j]
                if not (val == TTTGameState.EMPTY or val == TTTGameState.X
                        or val == TTTGameState.O):
                    return False
        return True

    # return whether current state is a finished game
    def is_goal_state(self):
        combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8]
                        [0, 3, 6], [1, 4, 7], [2, 5, 8],
                        [0, 4, 8], [2, 4, 6]]
        # check X's
        for combo in combinations:
            total = 0
            for num in combo:
                if self.board[num] == TTTGameState.X:
                    total += 1
            if total == 3:
                return True
        # check O's
        for combo in combinations:
            total = 0
            for num in combo:
                if self.board[num] == TTTGameState.O:
                    total += 1
            if total == 3:
                return True

        return False

    # returns a new board, replacing value in current board with new value
    def replace_with(self, x, y, val):
        new_state = copy.deepcopy(self)
        new_state.board[x][y] = val
        return new_state

    # returns a list of all states that can follow from the current state
    def get_next_states(self):
        new_states = []
        if self.to_move is TTTGameState.ALLY:
            to_place = TTTGameState.X
        else:
            to_place = TTTGameState.O
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] is TTTGameState.EMPTY:
                    new_state = self.replace_with(i, j, to_place)
                    new_states.append(new_state)
        return new_states

    def __repr__(self):
        return 'ttt_gamestate.TTTGameState({b}, {tm})'\
            .format(b=self.board, tm=self.to_move)

    def __str__(self):
        def val(x):
            return '-' if x == TTTGameState.EMPTY else x

        values = [val(mark) for row in self.board for mark in row]
        to_move = 'X' if self.to_move == TTTGameState.EMPTY else 'O'
        return '[{v[0]} {v[1]} {v[2]}]\n' \
               '[{v[3]} {v[4]} {v[5]}] ({tm} to move)\n' \
               '[{v[6]} {v[7]} {v[8]}]'.format(v=values, tm=to_move)

    def __eq__(self, other):
            return self.board == other.board and self.to_move == other.to_move
