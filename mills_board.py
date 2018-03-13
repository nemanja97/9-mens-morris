class Board:

    __slots__ = ['pos', 'wasMillW', 'wasMillB']

    def __init__(self):
        self.pos = {
            'O0': "X",
            'O1': "X",
            'O2': "X",
            'O3': "X",
            'O4': "X",
            'O5': "X",
            'O6': "X",
            'O7': "X",
            'M0': "X",
            'M1': "X",
            'M2': "X",
            'M3': "X",
            'M4': "X",
            'M5': "X",
            'M6': "X",
            'M7': "X",
            'I0': "X",
            'I1': "X",
            'I2': "X",
            'I3': "X",
            'I4': "X",
            'I5': "X",
            'I6': "X",
            'I7': "X",
        }
        self.wasMillW = False
        self.wasMillB = False

    def adjacent_positions(self, pos):
        adjacent = []

        adjacent_1 = pos[0] + str((int(pos[1]) - 1) % 8)
        adjacent_2 = pos[0] + str((int(pos[1]) + 1) % 8)

        adjacent.append(adjacent_1)
        adjacent.append(adjacent_2)

        if int(pos[1]) % 2 == 0:
            if pos[0] == "O":
                adjacent_3 = "M" + pos[1]
                adjacent.append(adjacent_3)
            if pos[0] == "M":
                adjacent_3 = "O" + pos[1]
                adjacent_4 = "I" + pos[1]
                adjacent.append(adjacent_3)
                adjacent.append(adjacent_4)
            if pos[0] == "I":
                adjacent_3 = "M" + pos[1]
                adjacent.append(adjacent_3)
        return adjacent

    def get_mill_num(self, colour):
        counter = 0
        for i in range (0, 7, 2):
            if self.pos["O"+str(i)] == self.pos["O"+str((i + 1) % 8)] == self.pos["O"+str((i -1) % 8)] == colour:
                counter += 1
            if self.pos["M"+str(i)] == self.pos["M"+str((i + 1) % 8)] == self.pos["M"+str((i -1) % 8)] == colour:
                counter += 1
            if self.pos["I"+str(i)] == self.pos["I"+str((i + 1) % 8)] == self.pos["I"+str((i -1) % 8)] == colour:
                counter += 1
            if self.pos["O"+str(i)] == self.pos["M"+str(i)] == self.pos["I"+str(i)] == colour:
                counter += 1
        return counter

    def get_number_of_pieces(self, colour):
        counter = 0
        for i in self.pos.values():
            if i == colour:
                counter += 1
        return counter

    def check_mill(self, pos, colour):
        if int(pos[1]) % 2 == 0:
            nextField = pos[0] + str((int(pos[1]) + 1) % 8)
            prevField = pos[0] + str((int(pos[1]) - 1) % 8)

            if (self.get_pos(pos) == self.get_pos(nextField) == self.get_pos(prevField) == colour):
                return True

            if (self.get_pos('O'+pos[1]) == self.get_pos('M'+pos[1]) == self.get_pos('I'+pos[1]) == colour):
                return True

            return False

        else:
            nextField = pos[0] + str((int(pos[1]) + 1) % 8)
            nextField_2 = pos[0] + str((int(pos[1]) + 2) % 8)

            prevField = pos[0] + str((int(pos[1]) - 1) % 8)
            prevField_2 = pos[0] + str((int(pos[1]) - 2) % 8)

            if (self.get_pos(pos) == self.get_pos(nextField) == self.get_pos(nextField_2) == colour):
                return True
            if (self.get_pos(pos) == self.get_pos(prevField) == self.get_pos(prevField_2) == colour):
                return True

            return False

    def isMill(self, pos, colour):
        try:
            value = self.get_pos(pos)
            if value != "X":
                return self.check_mill(pos, colour)
            else:
                return False
        except KeyError:
            print("Nepoznat unos polja")
            raise KeyError

    def set_pos(self, pos, value):
        try:
            self.pos[pos] = value
        except KeyError:
            print("Nepoznat unos polja")
            raise KeyError

    def get_pos(self, pos):
        try:
            return self.pos[pos]
        except KeyError:
            print("Nepoznat unos polja")
            raise KeyError

    def print_table(self):
        print(self.pos['O7'], "---------------", self.pos['O0'], "---------------", self.pos['O1'])
        print("|                 |                 |")
        print("|       ", self.pos['M7'], "------", self.pos['M0'], "------", self.pos['M1'], "       |")
        print("|        |        |        |        |")
        print("|        |  ", self.pos['I7'], "--", self.pos['I0'], "--", self.pos['I1'], "  |        |")
        print("|        |   |         |   |        |")
        print(self.pos['O6'], "------", self.pos['M6'], "-", self.pos['I6'], "       ", self.pos['I2'], "-",
              self.pos['M2'], "------", self.pos['O2'])
        print("|        |   |         |   |        |")
        print("|        |  ", self.pos['I5'], "--", self.pos['I4'], "--", self.pos['I3'], "  |        |")
        print("|        |        |        |        |")
        print("|       ", self.pos['M5'], "------", self.pos['M4'], "------", self.pos['M3'], "       |")
        print("|                 |                 |")
        print(self.pos['O5'], "---------------", self.pos['O4'], "---------------", self.pos['O3'])
