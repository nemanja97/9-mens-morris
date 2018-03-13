from mills_board import Board
from player_human import PlayerHuman
from alphaBeta import *

ALPHA_CONST = float("-inf")
BETA_CONST  = float("+inf")


class Game:

    __slots__ = ['board', 'playerHuman', 'playerAI']

    def __init__(self):
        self.board = Board()
        self.playerHuman = PlayerHuman('W')
        self.playerAI = PlayerAI('B')

    def win_condition(self):
        self.update_piece_count()
        if self.playerHuman.piecesOnBoard < 3:
            print("AI JE POBEDIO")
            exit(0)
        if self.playerAI.piecesOnBoard < 3:
            print("VI STE POBEDILI")
            exit(0)

    def update_piece_count(self):
        self.playerHuman.piecesOnBoard = self.board.get_number_of_pieces("W")
        self.playerAI.piecesOnBoard    = self.board.get_number_of_pieces("B")

    def phase1(self):
        for i in range(9):
            print("Vaš potez :")
            entered_pos = self.playerHuman.put_piece(self.board)
            self.board.print_table()
            if self.board.isMill(entered_pos, self.playerHuman.colour):
                self.playerHuman.remove_piece(self.board)
                self.board.print_table()

            print("Kompjuterov potez :")
            evaluation = alphaBetaPruning(self.board, 3, False, ALPHA_CONST, BETA_CONST, True)
            self.board = evaluation.board
            self.board.print_table()

    def phase2(self):
        while True:
            print("Vaš potez :")
            entered_pos = self.playerHuman.move_piece(self.board)
            self.board.print_table()
            if self.board.isMill(entered_pos, self.playerHuman.colour):
                self.playerHuman.remove_piece(self.board)
                self.board.print_table()
            self.win_condition()

            print("Kompjuterov potez :")
            evaluation = alphaBetaPruning(self.board, 5, False, ALPHA_CONST, BETA_CONST, False)
            self.board = evaluation.board
            self.board.print_table()
            self.win_condition()

    def play(self):
        self.phase1()
        self.phase2()
