#!/usr/bin/python3
"""
N-Queens Problem Solver
"""


import sys
from typing import List, Set


class NQueensSolver:
    def __init__(self, n: int):
        """
        Initialize the N-Queens solver.

        Args:
            n (int): Size of the chessboard (N x N)
        """
        self.n = n
        self.solutions = []
        self.board = [[0] * n for _ in range(n)]
        self.cols = set()
        self.pos_diag = set()
        self.neg_diag = set()

    def solve(self) -> List[List[int]]:
        """
        Find all solutions to the N-Queens problem.

        Returns:
            List[List[int]]: List of solutions
        """
        self._backtrack(0)
        return self.solutions

    def _backtrack(self, row: int) -> None:
        """
        Recursive backtracking function to find valid queen placements.

        Args:
            row (int): Current row being processed
        """
        if row == self.n:
            solution = self._get_queen_positions()
            self.solutions.append(solution)
            return

        for col in range(self.n):
            if self._is_safe_placement(row, col):
                self._place_queen(row, col)
                self._backtrack(row + 1)
                self._remove_queen(row, col)

    def _is_safe_placement(self, row: int, col: int) -> bool:
        """
        Check if a queen can be safely placed at the given position.

        Args:
            row (int): Row coordinate
            col (int): Column coordinate

        Returns:
            bool: True if placement is safe, False otherwise
        """
        return not (col in self.cols or
                    (row + col) in self.pos_diag or
                    (row - col) in self.neg_diag)

    def _place_queen(self, row: int, col: int) -> None:
        """
        Place a queen on the board and update tracking sets.

        Args:
            row (int): Row coordinate
            col (int): Column coordinate
        """
        self.board[row][col] = 1
        self.cols.add(col)
        self.pos_diag.add(row + col)
        self.neg_diag.add(row - col)

    def _remove_queen(self, row: int, col: int) -> None:
        """
        Remove a queen from the board and update tracking sets.

        Args:
            row (int): Row coordinate
            col (int): Column coordinate
        """
        self.board[row][col] = 0
        self.cols.remove(col)
        self.pos_diag.remove(row + col)
        self.neg_diag.remove(row - col)

    def _get_queen_positions(self) -> List[List[int]]:
        """
        Convert the current board state to a list of queen positions.

        Returns:
            List[List[int]]: List of [row, col] coordinates for each queen
        """
        positions = []
        for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col] == 1:
                    positions.append([row, col])
        return positions


def validate_input(arg: str) -> int:
    """
    Validate command line input and convert to integer.

    Args:
        arg (str): Command line argument for board size

    Returns:
        int: Validated board size

    Raises:
        ValueError: If input is not a valid integer or is less than 4
    """
    try:
        n = int(arg)
        if n < 4:
            raise ValueError("N must be at least 4")
        return n
    except ValueError as e:
        if str(e) == "N must be at least 4":
            raise
        raise ValueError("N must be a number")


def main() -> None:
    """
    Main function to handle command line execution of the N-Queens solver.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = validate_input(sys.argv[1])
        solver = NQueensSolver(n)
        solutions = solver.solve()
        for solution in solutions:
            print(solution)
    except ValueError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
