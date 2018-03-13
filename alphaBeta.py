from evaluation import Evaluation
from heuristics import *

def alphaBetaPruning(board, depth, isWhite, alpha, beta, isPhase_1):
    finalEval = Evaluation(board)

    if depth != 0:

        if isPhase_1:
            possibleBoards = generate_all_moves(board, isWhite)
        else:
            possibleBoards = generate_all_moves_phase2(board, isWhite)

        for possibleBoard in possibleBoards:
            if isWhite:
                currentEval = alphaBetaPruning(possibleBoard, depth - 1, not isWhite, alpha, beta, isPhase_1)

                if currentEval.evalValue > alpha:
                    alpha = currentEval.evalValue
                    finalEval.board = possibleBoard
            else:
                currentEval = alphaBetaPruning(possibleBoard, depth - 1, not isWhite, alpha, beta, isPhase_1)

                if currentEval.evalValue < beta:
                    beta = currentEval.evalValue
                    finalEval.board = possibleBoard
            if alpha >= beta:
                break

        if isWhite:
            finalEval.evalValue = alpha
        else:
            finalEval.evalValue = beta
    else:
        if isPhase_1:
            finalEval.evalValue = heuristic_phase1(board)
        else:
            finalEval.evalValue = heuristic_phase2(board)
    return finalEval
