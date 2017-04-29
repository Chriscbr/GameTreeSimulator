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
            self.board = [TTTGameState.EMPTY for x in range(0, 9)]
        else:
            self.board = board

        if to_move is None:
            self.to_move = TTTGameState.ALLY
        else:
            self.to_move = to_move

    # returns if current board state is valid
    def is_valid_state(self):

        # self.to_move is valid
        if not (self.to_move == TTTGameState.ALLY
                or self.to_move == TTTGameState.ENEMY):
            return False

        # self.board is valid size
        if len(self.board) != 9:
            return False

        total_x = 0
        total_o = 0

        # values in self.board are valid
        for i in range(0, 9):
            val = self.board[i]
            if not (val == TTTGameState.EMPTY or val == TTTGameState.X
                    or val == TTTGameState.O):
                return False
            if val == TTTGameState.X:
                total_x += 1
            if val == TTTGameState.O:
                total_o += 1

        # number of X's and O's placed is valid
        if self.to_move == TTTGameState.ALLY and total_x - total_o != 0:
            return False
        if self.to_move == TTTGameState.ENEMY and total_x - total_o != 1:
            return False

        return True

    # return whether current state is a finished game
    def is_goal_state(self):
        return self.is_win_state() or self.is_loss_state()

    # returns whether current state is a win for the player
    def is_win_state(self):
        if not self.is_valid_state():
            return False

        combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                        [0, 3, 6], [1, 4, 7], [2, 5, 8],
                        [0, 4, 8], [2, 4, 6]]

        for combo in combinations:
            total = 0
            for num in combo:
                if self.board[num] == TTTGameState.X:
                    total += 1
            if total == 3:
                return True
        return False

    # returns whether current state is a loss for the player
    def is_loss_state(self):
        if not self.is_valid_state():
            return False

        combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                        [0, 3, 6], [1, 4, 7], [2, 5, 8],
                        [0, 4, 8], [2, 4, 6]]

        for combo in combinations:
            total = 0
            for num in combo:
                if self.board[num] == TTTGameState.O:
                    total += 1
            if total == 3:
                return True
        return False

    # returns a new board, replacing value in current board with new value
    def replace_with(self, x, val):
        new_state = copy.deepcopy(self)
        new_state.board[x] = val
        return new_state

    # returns a list of all states that can follow from the current state
    def get_next_states(self):
        new_states = []
        to_place = (TTTGameState.X if self.to_move == TTTGameState.ALLY
                    else TTTGameState.O)
        next_move = (TTTGameState.ENEMY if self.to_move == TTTGameState.ALLY
                     else TTTGameState.ALLY)
        for i in range(0, 9):
            if self.board[i] is TTTGameState.EMPTY:
                new_state = self.replace_with(i, to_place)
                new_state.to_move = next_move
                new_states.append(new_state)
        return new_states

    def __repr__(self):
        return ('TTTGameState({b}, {tm})'
                .format(b=self.board, tm=self.to_move))

    def __str__(self):
        def val(x):
            if x == TTTGameState.X:
                return 'X'
            elif x == TTTGameState.O:
                return 'O'
            else:
                return '-'

        values = [val(mark) for mark in self.board]
        to_move = 'X' if self.to_move == TTTGameState.EMPTY else 'O'
        return ('[{v[0]} {v[1]} {v[2]}]\n'
                '[{v[3]} {v[4]} {v[5]}] ({tm} to move)\n'
                '[{v[6]} {v[7]} {v[8]}]'.format(v=values, tm=to_move))

    def __eq__(self, other):
            return self.board == other.board and self.to_move == other.to_move
