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

    def get_threatened_pos(self):
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
    #New Piece to be implemented
    pass

class Game:
    def __init__(self, gameboard):
        self.gameboard = gameboard

    def has_opponent_at(self, pos, opponent):
        return self.gameboard[pos][1] == opponent

class State:
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
    global game
    game = Game(gameboard)

    move = (None, None)
    return move #Format to be returned (('a', 0), ('b', 3))
