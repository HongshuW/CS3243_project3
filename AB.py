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
        return None

    def get_threatened_pos(self):
        # return a list of positions occupied by opponents that are threatened by this piece
        return None

    def get_opponent_color(self):
        if (self.color == "White"):
            return "Black"
        else:
            return "White"

class Knight(Piece):
    pass
        
class Rook(Piece):
    pass

class Bishop(Piece):
    pass
        
class Queen(Piece):
    pass
        
class King(Piece):
    pass
        
class Pawn(Piece):
    def get_moves(self):
        # if pawn is at the first or last row, it cannot capture other pieces,
        # so only consider moving between rows 1 to 3
        if (self.color == "White"):
            new_row = self.get_row_int() + 1
            new_pos = get_position_tuple(self.get_col_char(), new_row)
            if (new_row <= 3 and (not state.game.has_piece_at(new_pos))):
                return list(new_pos)
        else:
            new_row = self.get_row_int() - 1
            new_pos = get_position_tuple(self.get_col_char(), new_row)
            if (new_row >= 1 and (not state.game.has_piece_at(new_pos))):
                return list(new_pos)
        return None

    def get_threatened_pos(self):
        threatened = list()
        if (self.color == "White"):
            new_row = self.get_row_int() + 1
            if (new_row < 5):
                col_1 = self.get_col_int() + 1
                col_2 = self.get_col_int() - 1
                pos_1 = get_position_tuple(get_col_char(col_1), new_row)
                pos_2 = get_position_tuple(get_col_char(col_2), new_row)
                if (col_1 < 5 and state.game.has_opponent_at(pos_1, self.get_opponent_color())):
                    threatened.append(pos_1)
                if (col_2 >= 0 and state.game.has_opponent_at(pos_2, self.get_opponent_color())):
                    threatened.append(pos_2)
        else:
            new_row = self.get_row_int() - 1
            if (new_row >= 0):
                col_1 = self.get_col_int() + 1
                col_2 = self.get_col_int() - 1
                pos_1 = get_position_tuple(get_col_char(col_1), new_row)
                pos_2 = get_position_tuple(get_col_char(col_2), new_row)
                if (col_1 < 5 and state.game.has_opponent_at(pos_1, self.get_opponent_color())):
                    threatened.append(pos_1)
                if (col_2 >= 0 and state.game.has_opponent_at(pos_2, self.get_opponent_color())):
                    threatened.append(pos_2)
        return threatened

class Game:
    def __init__(self, gamemboard, parent, depth):
        self.gameboard = gamemboard
        self.parent = parent
        self.depth = depth

    def has_piece_at(self, pos):
        return (pos in self.gameboard)

    def has_opponent_at(self, pos, opponent_color):
        return self.has_piece_at(pos) and self.gameboard[pos][1] == opponent_color

class State:
    def __init__(self, game, to_move):
        self.game = game
        self.to_move = to_move

    def actions(self):
        pass

    def result(self, action):
        pass

    def is_terminal(self):
        pass

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
    pass



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
    game = Game(gameboard, None, 0)
    global state
    state = State(game, "White")

    move = ab()
    return move #Format to be returned (('a', 0), ('b', 3))
