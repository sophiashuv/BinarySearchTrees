# code is particulary by @dobosevych

import random
from copy import deepcopy
from btree import Tree
from btnode import Node

class Board:
    """
    Class for board representation
    """
    NOUGHT = 1
    CROSS = -1
    EMPTY = 0

    NOUGHT_WINNER = 1
    CROSS_WINNER = -1
    DRAW = 2
    NOT_FINISHED = 0

    WINNING_COMBINATIONS = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
                            ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 2), (2, 2)),
                            ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)),
                            ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))

    def __init__(self):
        self.cells = [[0] * 3 for _ in range(3)]
        self.last_move = Board.NOUGHT
        self.number_of_moves = 0

    def make_move(self, cell):
        """
        The function that makes move
        """
        if self.cells[cell[0]][cell[1]] != 0:
            return False
        self.last_move = -self.last_move
        self.cells[cell[0]][cell[1]] = self.last_move
        self.number_of_moves += 1
        return True

    def has_winner(self):
        """
        The function that checks if ther is a winer
        """
        for combination in self.WINNING_COMBINATIONS:
            lst = list()
            for cell in combination:
                lst.append(self.cells[cell[0]][cell[1]])
            if max(lst) == min(lst) and max(lst) != Board.EMPTY:
                return max(lst)
        if self.number_of_moves >= 9:
            return Board.DRAW
        return Board.NOT_FINISHED

    def make_random_move(self):
        """
        The function that makes a random move
        """
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] == Board.EMPTY:
                    possible_moves.append((i, j))
        cell = random.choice(possible_moves)
        self.last_move = -self.last_move
        self.cells[cell[0]][cell[1]] = self.last_move
        self.number_of_moves += 1
        return True

    def __str__(self):
        """
        The function for string representation of a board
        """
        transform = {0: " ", 1: "O", -1: "X"}
        s = "\n"
        s += "      0     1     2\n"
        s += "   -------------------\n"
        for i in range(3):
            for j in range(3):
                if j == 0:
                    s += str(i) + "  |  " + str(transform[(self.cells[i][j])]) + "  |"

                else:
                    s += "  " + str(transform[self.cells[i][j]]) + "  |"
            if i < 2:
                s += "\n   -------------------\n"
        s += "\n   -------------------\n"
        return s


    def computer_move(self):
        """
        The function that makes computer move
        """
        if self.has_winner():
            return
        board1 = deepcopy(self)
        board1.make_random_move()
        board2 = deepcopy(self)
        board2.make_random_move()
        score1 = board1.compute_score()
        score2 = board2.compute_score()
        if score1 > score2:
            for i in range(3):
                for j in range(3):
                    if self.cells[i][j] != board1.cells[i][j]:
                        self.make_move([i, j])
        else:
            for i in range(3):
                for j in range(3):
                    if self.cells[i][j] != board2.cells[i][j]:
                        self.make_move([i, j])

    def compute_score(self):
        """
        The function returns sum of all scores in binary tree
        """
        board = Tree(self)
        if self.has_winner():
            winner_scores = {Board.NOUGHT_WINNER: 1,
                             Board.CROSS_WINNER: -1,
                             Board.DRAW: 0}
            return winner_scores[self.has_winner()]
        board.key = Node(self)
        left_board = deepcopy(self)
        left_move = left_board.make_random_move()
        board.key.left = Node(left_move)
        right_board = deepcopy(self)
        right_move = right_board.make_random_move()
        board.key.right = Node(right_move)
        return left_board.compute_score() + right_board.compute_score()
