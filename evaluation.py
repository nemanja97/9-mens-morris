class Evaluation():

    __slots__ = ['evalValue', 'board']

    def __init__(self, board):
        self.evalValue = 0
        self.board = board