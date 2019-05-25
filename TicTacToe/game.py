from board import Board


class Game:
    """Class game representation"""
    def __init__(self):
        self.board = Board()

    def main(self):
        """
        The main game function
        """
        while not self.board.has_winner():
            try:
                try:
                    begin = input('Enter move: ')
                    a, b = int(begin[0]), int(begin[-1])
                except:
                    print('You wrote wrong coords')
                if self.board.cells[a][b] == Board.EMPTY:
                    self.board.make_move((a, b))
                    self.board.computer_move()
                    print(self.board)
                else:
                    print("This cell isn't empty")
            except:
                pass

        if self.board.has_winner() == 1:
            print('You loos')
        elif self.board.has_winner() == -1:
            print('You won!')
        else:
            print('You draw')


if __name__ == '__main__':
    Game().main()
