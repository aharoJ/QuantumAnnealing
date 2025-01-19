import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
import copy
import random


# Example Sudoku Puzzle (0 represents empty cells)
sudoku_puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_sudoku(grid):
    """Utility function to print the Sudoku grid in a readable format."""
    for i in range(9):
        row = ""
        for j in range(9):
            num = grid[i][j]
            row += f"{num} " if num != 0 else ". "
            if (j + 1) % 3 == 0 and j < 8:
                row += "| "
        print(row)
        if (i + 1) % 3 == 0 and i < 8:
            print("- " * 11)

print_sudoku(sudoku_puzzle)
