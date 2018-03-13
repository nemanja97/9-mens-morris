from player_ai import *

def heuristic_phase1(board):
    evaluation = 0

    # R1 - Closed morris
    if board.wasMillW:
        evaluation += 18
    elif board.wasMillB:
        evaluation -= 18

    # R2 - Morrises number
    numWhiteMills = board.get_mill_num("W")
    numBlackMills = board.get_mill_num("B")
    evaluation += 26 * (numWhiteMills - numBlackMills)

    # R3 - Number of blocked opponent pieces
    numBlockedMillsWhite, numBlockedMillsBlack = blocked_mills(board)
    evaluation += (numBlockedMillsWhite - numBlockedMillsBlack)

    # R4 - Pieces number
    numWhite = board.get_number_of_pieces("W")
    numBlack = board.get_number_of_pieces("B")
    evaluation += 6 * (numWhite - numBlack)

    # R5 - Number of 2-piece configurations / opened morrises
    num2PiecesWhite = get_number_of_open_morrises(board, "W")
    num2PiecesBlack = get_number_of_open_morrises(board, "B")
    evaluation += 12 * (num2PiecesWhite - num2PiecesBlack)

    # R6 - Number of 3-piece configurations
    num3PieceWhite = get_number_of_three_piece_configurations(board, "W")
    num3PieceBlack = get_number_of_three_piece_configurations(board, "B")
    evaluation += 7 * (num3PieceWhite - num3PieceBlack)

    return evaluation

def heuristic_phase2(board):
    evaluation = 0

    # R1 - Closed morris
    if board.wasMillW:
        evaluation += 14
    elif board.wasMillB:
        evaluation -= 14

    # R2 - Morrises number
    numWhiteMills = board.get_mill_num("W")
    numBlackMills = board.get_mill_num("B")
    evaluation += 43 * (numWhiteMills - numBlackMills)

    # R3 - Number of blocked opponent pieces
    numBlockedMillsWhite, numBlockedMillsBlack = blocked_mills(board)
    evaluation += 10 * (numBlockedMillsWhite - numBlockedMillsBlack)

    # R4 - Pieces number
    numWhite = board.get_number_of_pieces("W")
    numBlack = board.get_number_of_pieces("B")
    evaluation += (numWhite - numBlack)

    # R5 - Opened morris
    numOpenWhite = get_number_of_open_morrises(board, "W")
    numOpenBlack = get_number_of_open_morrises(board, "B")
    evaluation += 30 * (numOpenWhite - numOpenBlack)

    # R6 - Double morris
    numDoubleWhite = get_number_of_double_morrises(board, "W")
    numDoubleBlack = get_number_of_double_morrises(board, "B")
    evaluation += 40 * (numDoubleWhite - numDoubleBlack)

    # R7 - Winning configuration
    if isVictory(board, "B"):
        evaluation += 958
    elif isVictory(board, "W"):
        evaluation -= 958

    return evaluation
