### IMPORTANT: Remove any print() functions or rename any print functions/variables/string when submitting on CodePost
### The autograder will not run if it detects any print function.

# Helper functions to aid in your implementation. Can edit/remove
class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def get_row_int(self):
        return self.position[1]

    def get_col_int(self):
        return ord(self.position[0]) - 97

    def get_col_char(self):
        return self.position[0]

    def get_moves(self):
        # return a list of positions that this piece can move to
        return None

    def get_opponent_color(self):
        if (self.color == "White"):
            return "Black"
        else:
            return "White"

class Knight(Piece):
    def get_moves(self):
        col_int = self.get_col_int()
        row_int = self.get_row_int()
        rows = 5
        cols = 5
        moves = set()
        if (col_int - 1 >= 0):
            if (row_int + 2 < rows):
                pos = get_position_tuple(get_col_char(col_int - 1), row_int + 2)
                if (not state.game.has_piece_at(pos) or state.game.has_opponent_at(pos, self.get_opponent_color())):
                    moves.add((self.position, pos))
            if (row_int - 2 >= 0):
                pos = get_position_tuple(get_col_char(col_int - 1), row_int - 2)
                if (not state.game.has_piece_at(pos) or state.game.has_opponent_at(pos, self.get_opponent_color())):
                    moves.add((self.position, pos))
        if (col_int - 2 >= 0):
            if (row_int + 1 < rows):
                pos = get_position_tuple(get_col_char(col_int - 2), row_int + 1)
                if (not state.game.has_piece_at(pos) or state.game.has_opponent_at(pos, self.get_opponent_color())):
                    moves.add((self.position, pos))
            if (row_int - 1 >= 0):
                pos = get_position_tuple(get_col_char(col_int - 2), row_int - 1)
                if (not state.game.has_piece_at(pos) or state.game.has_opponent_at(pos, self.get_opponent_color())):
                    moves.add((self.position, pos))
        if (col_int + 1 < cols):
            if (row_int + 2 < rows):
                pos = get_position_tuple(get_col_char(col_int + 1), row_int + 2)
                if (not state.game.has_piece_at(pos) or state.game.has_opponent_at(pos, self.get_opponent_color())):
                    moves.add((self.position, pos))
            if (row_int - 2 >= 0):
                pos = get_position_tuple(get_col_char(col_int + 1), row_int - 2)
                if (not state.game.has_piece_at(pos) or state.game.has_opponent_at(pos, self.get_opponent_color())):
                    moves.add((self.position, pos))
        if (col_int + 2 < cols):
            if (row_int + 1 < rows):
                pos = get_position_tuple(get_col_char(col_int + 2), row_int + 1)
                if (not state.game.has_piece_at(pos) or state.game.has_opponent_at(pos, self.get_opponent_color())):
                    moves.add((self.position, pos))
            if (row_int - 1 >= 0):
                pos = get_position_tuple(get_col_char(col_int + 2), row_int - 1)
                if (not state.game.has_piece_at(pos) or state.game.has_opponent_at(pos, self.get_opponent_color())):
                    moves.add((self.position, pos))
        return moves

class Rook(Piece):
    def get_moves(self):
        moves = set()
        for i in range(self.get_row_int() + 1, 5):
            pos = get_position_tuple(self.get_col_char(), i)
            if state.game.has_piece_at(pos):
                if state.game.has_opponent_at(pos, self.get_opponent_color()):
                    moves.add((self.position, pos))
                break
            moves.add((self.position, pos))
        i = self.get_row_int() - 1
        while i >= 0:
            pos = get_position_tuple(self.get_col_char(), i)
            if state.game.has_piece_at(pos):
                if state.game.has_opponent_at(pos, self.get_opponent_color()):
                    moves.add((self.position, pos))
                break
            moves.add((self.position, pos))
            i -= 1
        for j in range(self.get_col_int() + 1, 5):
            pos = get_position_tuple(get_col_char(j), self.get_row_int())
            if state.game.has_piece_at(pos):
                if state.game.has_opponent_at(pos, self.get_opponent_color()):
                    moves.add((self.position, pos))
                break
            moves.add((self.position, pos))
        j = self.get_col_int() - 1
        while j >= 0:
            pos = get_position_tuple(get_col_char(j), self.get_row_int())
            if state.game.has_piece_at(pos):
                if state.game.has_opponent_at(pos, self.get_opponent_color()):
                    moves.add((self.position, pos))
                break
            moves.add((self.position, pos))
            j -= 1
        return moves

class Bishop(Piece):
    def get_moves(self):
        moves = set()
        i = self.get_row_int()
        j = self.get_col_int()
        count = 0
        plus_stop = False
        minus_stop = False
        while i >= 0:
            if j + count < 5 and (plus_stop == False):
                pos = get_position_tuple(get_col_char(j + count), i)
                if (state.game.has_piece_at(pos)):
                    if not(i == self.get_row_int() and j == self.get_col_int()):
                        plus_stop = True
                    if (state.game.has_opponent_at(pos, self.get_opponent_color())):
                        moves.add((self.position, pos))
                else:
                    if self.position != pos:
                        moves.add((self.position, pos))
            if j - count >= 0 and (minus_stop == False):
                pos = get_position_tuple(get_col_char(j - count), i)
                if (state.game.has_piece_at(pos)):
                    if not(i == self.get_row_int() and j == self.get_col_int()):
                        minus_stop = True
                    if (state.game.has_opponent_at(pos, self.get_opponent_color())):
                        moves.add((self.position, pos))
                else:
                    if self.position != pos:
                        moves.add((self.position, pos))
            i -= 1
            count += 1
        i = self.get_row_int()
        count = 0
        plus_stop = False
        minus_stop = False
        while i < 5:
            if j + count < 5 and (plus_stop == False):
                pos = get_position_tuple(get_col_char(j + count), i)
                if (state.game.has_piece_at(pos)):
                    if not(i == self.get_row_int() and j == self.get_col_int()):
                        plus_stop = True
                    if (state.game.has_opponent_at(pos, self.get_opponent_color())):
                        moves.add((self.position, pos))
                else:
                    if self.position != pos:
                        moves.add((self.position, pos))
            if j - count >= 0 and (minus_stop == False):
                pos = get_position_tuple(get_col_char(j - count), i)
                if (state.game.has_piece_at(pos)):
                    if not(i == self.get_row_int() and j == self.get_col_int()):
                        minus_stop = True
                    if (state.game.has_opponent_at(pos, self.get_opponent_color())):
                        moves.add((self.position, pos))
                else:
                    if self.position != pos:
                        moves.add((self.position, pos))
            i += 1
            count += 1
        return moves

class Queen(Piece):
    def get_moves(self):
        rook = Rook(self.color, self.position)
        bishop = Bishop(self.color, self.position)
        moves = rook.get_moves()
        moves = moves.union(bishop.get_moves())
        return moves

class King(Piece):
    def get_moves(self):
        # include unoccupied positions or positions containing an opponent piece
        moves = set()
        i = self.get_col_int() - 1
        while (i <= self.get_col_int() + 1):
            if (i < 5 and i >= 0):
                j = self.get_row_int() - 1
                while (j <= self.get_row_int() + 1):
                    if (j < 5 and j >= 0):
                        pos = get_position_tuple(get_col_char(i), j)
                        if (not state.game.has_piece_at(pos) or
                                state.game.has_opponent_at(pos, self.get_opponent_color())):
                            moves.add((self.position, pos))
                    j += 1
            i += 1
        return moves

class Pawn(Piece):
    def get_moves(self):
        # if pawn is at the first or last row, it cannot capture other pieces,
        # so only consider moving between rows 1 to 3
        moves = self.get_threatened_pos()
        if (self.color == "White"):
            new_row = self.get_row_int() + 1
            new_pos = get_position_tuple(self.get_col_char(), new_row)
            if (new_row <= 3 and (not state.game.has_piece_at(new_pos))):
                moves.add((self.position, new_pos))
        else:
            new_row = self.get_row_int() - 1
            new_pos = get_position_tuple(self.get_col_char(), new_row)
            if (new_row >= 1 and (not state.game.has_piece_at(new_pos))):
                moves.add((self.position, new_pos))
        return moves

    def get_threatened_pos(self):
        threatened = set()
        if (self.color == "White"):
            new_row = self.get_row_int() + 1
            if (new_row < 5):
                col_1 = self.get_col_int() + 1
                col_2 = self.get_col_int() - 1
                pos_1 = get_position_tuple(get_col_char(col_1), new_row)
                pos_2 = get_position_tuple(get_col_char(col_2), new_row)
                if (col_1 < 5 and state.game.has_opponent_at(pos_1, self.get_opponent_color())):
                    threatened.add((self.position, pos_1))
                if (col_2 >= 0 and state.game.has_opponent_at(pos_2, self.get_opponent_color())):
                    threatened.add((self.position, pos_2))
        else:
            new_row = self.get_row_int() - 1
            if (new_row >= 0):
                col_1 = self.get_col_int() + 1
                col_2 = self.get_col_int() - 1
                pos_1 = get_position_tuple(get_col_char(col_1), new_row)
                pos_2 = get_position_tuple(get_col_char(col_2), new_row)
                if (col_1 < 5 and state.game.has_opponent_at(pos_1, self.get_opponent_color())):
                    threatened.add((self.position, pos_1))
                if (col_2 >= 0 and state.game.has_opponent_at(pos_2, self.get_opponent_color())):
                    threatened.add((self.position, pos_2))
        return threatened

class Game:
    def __init__(self, gamemboard, parent, depth, color):
        self.gameboard = gamemboard
        self.parent = parent
        self.depth = depth
        self.own_set = dict()
        self.opponent_set = dict()
        for key in gamemboard:
            if gamemboard[key][1] == color:
                self.own_set[key] = gamemboard[key]
            else:
                self.opponent_set[key] = gamemboard[key]

    def has_piece_at(self, pos):
        return (pos in self.gameboard)

    def has_opponent_at(self, pos, opponent_color):
        return self.has_piece_at(pos) and self.gameboard[pos][1] == opponent_color

    def is_terminal(self):
        king_pos = None
        for pos in self.opponent_set:
            if (self.opponent_set[pos][0] == "King"):
                return False
            else:
                return True

class State:
    def __init__(self, game):
        self.game = game

    def result(self, action):
        pass

    def is_terminal(self):
        return self.game.is_terminal()

    def utility(self, player):
        pass

def get_col_int(col_char):
    return ord(col_char) - 97

def get_col_char(col_int):
    return chr(col_int + 97)

def get_position_tuple(col_char, row):
    return (col_char, int(row))

#Implement your minimax with alpha-beta pruning algorithm here.
def ab():
    own_pieces = state.game.own_set
    # get all possible moves
    moves = set()
    for pos in own_pieces:
        piece = None
        type = own_pieces[pos][0]
        color = own_pieces[pos][1]
        if (type == "King"):
            piece = King(color, pos)
        elif (type == "Queen"):
            piece = Queen(color, pos)
        elif (type == "Rook"):
            piece = Rook(color, pos)
        elif (type == "Bishop"):
            piece = Bishop(color, pos)
        elif (type == "Knight"):
            piece = Knight(color, pos)
        else:
            piece = Pawn(color, pos)
        moves = moves.union(piece.get_moves())
    return list(moves)[0]



### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# Chess Pieces: King, Queen, Knight, Bishop, Rook (First letter capitalized)
# Colours: White, Black (First Letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)

# Parameters:
# gameboard: Dictionary of positions (Key) to the tuple of piece type and its colour (Value). This represents the current pieces left on the board.
# Key: position is a tuple with the x-axis in String format and the y-axis in integer format.
# Value: tuple of piece type and piece colour with both values being in String format. Note that the first letter for both type and colour are capitalized as well.
# gameboard example: {('a', 0) : ('Queen', 'White'), ('d', 10) : ('Knight', 'Black'), ('g', 25) : ('Rook', 'White')}
#
# Return value:
# move: A tuple containing the starting position of the piece being moved to the new position for the piece. x-axis in String format and y-axis in integer format.
# move example: (('a', 0), ('b', 3))

def studentAgent(gameboard):
    # You can code in here but you cannot remove this function, change its parameter or change the return type
    game = Game(gameboard, None, 0, "White")
    global state
    state = State(game)

    move = ab()
    return move #Format to be returned (('a', 0), ('b', 3))

# studentAgent({('a',0):('Rook','White'), ('a',4):('Rook','Black'), ('a',1):('Pawn','White'), ('a',3):('Pawn','Black'),
#               ('b',0):('Knight','White'), ('b',4):('Knight','Black'), ('b',1):('Pawn','White'), ('b',3):('Pawn','Black'),
#               ('c',0):('Bishop','White'), ('c',4):('Bishop','Black'), ('c',1):('Pawn','White'), ('c',3):('Pawn','Black'),
#               ('d',0):('Queen','White'), ('d',4):('Queen','Black'), ('d',1):('Pawn','White'), ('d',3):('Pawn','Black'),
#               ('e',0):('King','White'), ('e',4):('King','Black'), ('e',1):('Pawn','White'), ('e',3):('Pawn','Black')})