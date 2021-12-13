from pickle import dump, load
import pandas as pd
import numpy as np

from models import Poly
from solver import exact_cover, solve


def exact_cover_matrix(board):
    shapes = board.usable_shapes
    names = board.usable_names
    Y = {}
    X = board.placeable_area | shapes
    for name in names:
        Y.update(board.possible_placement(Poly(name, board.bases)))
    return exact_cover(X, Y)


def get_solutions(board):
    X,Y = exact_cover_matrix(board)
    solutions = list(solve(X, Y, []))
    if len(solutions) == 0:
        print("Sorry,there are no solution.")
    else:
        print("Problem solved! There are %s solutions." % len(solutions))
    return solutions


def load_solutions(file_name="sols.pkl"):
    with open(file_name, "rb") as f:
        solutions = load(f)
    return solutions


def save_solutions(solutions, file_name="sols.pkl"):
    with open(file_name, "rb") as f:
        dump(solutions, f)


def read_board():
    df = pd.read_clipboard(header=None,sep='\t')
    df.fillna(0,inplace=True)
    return np.array(df)
