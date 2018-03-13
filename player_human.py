class PlayerHuman():

    __slots__ = ["colour", "piecesOnBoard"]

    def __init__(self, colour):
        self.colour = colour
        self.piecesOnBoard = 0

    def put_piece(self, board):
        while True:
            try:
                pos = input("Unesite polje O[0..7], M[0..7], I[0..7] >> ")
                if board.get_pos(pos) != "X":
                    print("Ovo polje je zauzeto")
                else:
                    board.set_pos(pos, self.colour)
                    return pos
            except KeyError:
                pass

    def move_piece(self, board):
        while True:
            try:
                pos = input("Unesite polje koje želite pomeriti O[0..7], M[0..7], I[0..7] >> ")
                if board.get_pos(pos) != "W":
                    print("Ovo polje ne možete pomeriti")
                else:
                    pos2 = input("Unesite lokaciju gde ga želite pomeriti O[0..7], M[0..7], I[0..7] >> ")
                    adjLocations = board.adjacent_positions(pos)
                    if pos2 in adjLocations and board.pos[pos2] == "X":
                        board.set_pos(pos2, self.colour)
                        board.set_pos(pos, "X")
                        return pos2
                    else:
                        print("Ne možete ovde pomeriti polje")
            except KeyError:
                pass

    def remove_piece(self, board):
        allMills = True
        for pos in board.pos.keys():
            if board.isMill(pos, "B"):
                allMills = False
                break
        while True:
            try:
                pos = input("Koje polje uklanjate? O[0..7], M[0..7], I[0..7] >> ")
                if board.get_pos(pos) == "X":
                    print("Ovo polje je prazno")
                elif board.get_pos(pos) == "W":
                    print("Ovo je vaše polje")
                else:
                    if board.isMill(pos, "B") is True and allMills is False:
                        print("Ovo polje je unutar mice")
                    else:
                        board.set_pos(pos, "X")
                        return pos
            except KeyError:
                pass
