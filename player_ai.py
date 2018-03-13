import copy

class PlayerAI():

    __slots__ = ["colour", "piecesOnBoard"]

    def __init__(self, colour):
        self.colour = colour
        self.piecesOnBoard = 0

def generate_all_moves(board, isWhite):
    if isWhite:
        colour = "W"
    else:
        colour = "B"
    possibleBoards = []

    for i in board.pos.keys():
        if board.pos[i] == "X":
            boardCopy = copy.deepcopy(board)
            boardCopy.pos[i] = colour

            if boardCopy.isMill(i, colour):
                if isWhite:
                    boardCopy.wasMillW = True
                else:
                    boardCopy.wasMillB = True
                possibleBoards = removePiece(boardCopy, possibleBoards, not isWhite)
            else:
                possibleBoards.append(boardCopy)

    return possibleBoards

def generate_all_moves_phase2(board, isWhite):
    if isWhite:
        colour = "W"
    else:
        colour = "B"
    possibleBoards = []

    for i in board.pos.keys():
        if board.pos[i] == colour:
            adjLocations = board.adjacent_positions(i)
            for location in adjLocations:
                if board.pos[location] == "X":
                    boardCopy = copy.deepcopy(board)
                    boardCopy.pos[i] = "X"
                    boardCopy.pos[location] = colour

                    if boardCopy.isMill(location, colour):
                        if isWhite:
                            boardCopy.wasMillW = True
                        else:
                            boardCopy.wasMillB = True
                        possibleBoards = removePiece(boardCopy, possibleBoards, not isWhite)
                    else:
                        possibleBoards.append(boardCopy)

    return possibleBoards

def blocked_from_position(board, pos):
    adjPositions = board.adjacent_positions(pos)
    countW, countB = 0, 0
    for adj_pos in adjPositions:
        if board.pos[adj_pos] == "W":
            countW += 1
        elif board.pos[adj_pos] == "B":
            countB += 1
    if countW > countB:
        return 1
    elif countW < countB:
        return 2
    else:
        return 3

def blocked_mills(board):
    counterBlockedW, counterBlockedB = 0, 0
    for i in range(1, 8, 2):
        block = blocked_from_position(board, ('O' + str(i)))
        if block == 1:
            counterBlockedW += 1
        elif block == 2:
            counterBlockedB += 1
        block = blocked_from_position(board, ('M' + str(i)))
        if block == 1:
            counterBlockedW += 1
        elif block == 2:
            counterBlockedB += 1
        block = blocked_from_position(board, ('I' + str(i)))
        if block == 1:
            counterBlockedW += 1
        elif block == 2:
            counterBlockedB += 1
    return counterBlockedW, counterBlockedB

def board_line_check(board, pos, colour):
    counter = 0
    if board.pos[pos] == colour:
        counter += 1
    adjLocations = board.adjacent_positions(pos)
    for adj_loc in adjLocations:
        if adj_loc[0] == pos[0]:
            if board.pos[adj_loc] == colour:
                counter += 1
    return counter

def board_diff_check(board, pos, colour):
    counter = 0
    if board.pos[pos] == colour:
        counter += 1
    adjLocations = board.adjacent_positions(pos)
    for adj_loc in adjLocations:
        if adj_loc[0] != pos[0]:
            if board.pos[adj_loc] == colour:
                counter += 1
    return counter

def get_number_of_open_morrises(board, colour):
    counter = 0
    for i in range(0, 7, 2):
        if board_line_check(board, "O" + str(i), colour) == 2:
            counter += 1
        if board_line_check(board, "M" + str(i), colour) == 2:
            counter += 1
        if board_diff_check(board, "O" + str(i), colour) == 2:
            counter += 1
        if board_line_check(board, "I" + str(i), colour) == 2:
            counter += 1
    return counter

def get_number_of_three_piece_configurations(board, colour):
    counter = 0
    for i in range(1, 8, 2):
        if board_line_check(board, "O" + str(i), colour) == 3:
            counter += 1
        if board_line_check(board, "M" + str(i), colour) == 3:
            counter += 1
        if board_line_check(board, "I" + str(i), colour) == 3:
            counter += 1
    return counter


def get_number_of_double_morrises(board, colour):
    counter = 0
    outerIndicator_Upper  = True
    outerIndicator_Lower  = True
    middleIndicator_Upper = True
    middleIndicator_Lower = True
    innerIndicator_Upper  = True
    innerIndicator_Lower  = True

    for i in range(0, 5):
        if board.pos["O" + str((7 + i) % 8)] != colour:
            outerIndicator_Upper = False
        if board.pos["O" + str((7 - i) % 8)] != colour:
            outerIndicator_Lower = False
        if board.pos["M" + str((7 + i) % 8)] != colour:
            middleIndicator_Upper = False
        if board.pos["M" + str((7 - i) % 8)] != colour:
            middleIndicator_Lower = False
        if board.pos["I" + str((7 + i) % 8)] != colour:
            innerIndicator_Upper = False
        if board.pos["I" + str((7 - i) % 8)] != colour:
            innerIndicator_Lower = False

    if outerIndicator_Upper:
        counter += 1
    if outerIndicator_Lower:
        counter += 1
    if middleIndicator_Upper:
        counter += 1
    if middleIndicator_Lower:
        counter += 1
    if innerIndicator_Upper:
        counter += 1
    if innerIndicator_Lower:
        counter += 1
    return counter

def isVictory(board, colour):
    if board.get_number_of_pieces(colour) <= 2:
        return True

def removePiece(board, boardList, isWhite):
    if isWhite:
        colour = "W"
    else:
        colour = "B"
    for i in board.pos.keys():
        if board.pos[i] == colour:
            if not board.isMill(i, colour):
                newCopy = copy.deepcopy(board)
                newCopy.pos[i] = "X"
                boardList.append(newCopy)
    return boardList