import xlwings as xw
import numpy as np
from helpers import get_solutions, exact_cover_matrix
from solver import solve
from models import Board, Solution
from constants import PENT_BASES, SGIQ_BASES


@xw.sub
def pent512_solver():
    wb = xw.Book.caller()
    sheet = wb.sheets["Pentominos"]
    input_mat = sheet.range("B10:M14").options(np.array).value
    board = Board(input_mat, PENT_BASES)
    def f(x): return {v: k for k, v in board.maps.items()}[x]
    X, Y = exact_cover_matrix(board)
    while True:
        for sol in solve(X, Y, []):
            if sol:
                res_mat = Solution(sol, board).placement_matrix
                res = np.vectorize(f)(res_mat)
                sheet.range("S10:AD14").value = res
                return
        else:
            app = xw.apps.active
            my_msgBox_macro = app.macro('noSolutionAlert')
            my_msgBox_macro()
            return


@xw.sub
def pent610_solver():
    wb = xw.Book.caller()
    sheet = wb.sheets["Pentominos"]
    input_mat = sheet.range("B27:K32").options(np.array).value
    board = Board(input_mat, PENT_BASES)
    def f(x): return {v: k for k, v in board.maps.items()}[x]
    X, Y = exact_cover_matrix(board)
    while True:
        for sol in solve(X, Y, []):
            if sol:
                res_mat = Solution(sol, board).placement_matrix
                res = np.vectorize(f)(res_mat)
                sheet.range("Q27:Z32").value = res
                return
        else:
            app = xw.apps.active
            my_msgBox_macro = app.macro('noSolutionAlert')
            my_msgBox_macro()
            return


@xw.sub
def pent415_solver():
    wb = xw.Book.caller()
    sheet = wb.sheets["Pentominos"]
    input_mat = sheet.range("B35:P38").options(np.array).value
    board = Board(input_mat, PENT_BASES)
    def f(x): return {v: k for k, v in board.maps.items()}[x]
    X, Y = exact_cover_matrix(board)
    while True:
        for sol in solve(X, Y, []):
            if sol:
                res_mat = Solution(sol, board).placement_matrix
                res = np.vectorize(f)(res_mat)
                sheet.range("V35:AJ38").value = res
                return
        else:
            app = xw.apps.active
            my_msgBox_macro = app.macro('noSolutionAlert')
            my_msgBox_macro()
            return

@xw.sub
def pent88_solver():
    wb = xw.Book.caller()
    sheet = wb.sheets["Pentominos"]
    input_mat = sheet.range("D17:K24").options(np.array).value
    board = Board(input_mat, PENT_BASES)
    maps = {v: k for k, v in board.maps.items()}
    maps.update({-1: ""})
    def f(x): return maps[x]
    X, Y = exact_cover_matrix(board)
    while True:
        for sol in solve(X, Y, []):
            if sol:
                res_mat = Solution(sol, board).placement_matrix
                res = np.vectorize(f)(res_mat)
                sheet.range("Q17:X24").value = res
                return
        else:
            app = xw.apps.active
            my_msgBox_macro = app.macro('noSolutionAlert')
            my_msgBox_macro()
            return


@xw.sub
def sgiq_solver():
    wb = xw.Book.caller()
    sheet = wb.sheets["sgiq"]
    input_mat = sheet.range("W2:AG6").options(np.array).value
    board = Board(input_mat, SGIQ_BASES)
    def f(x): return {v: k for k, v in board.maps.items()}[x]
    X, Y = exact_cover_matrix(board)
    while True:
        for sol in solve(X, Y, []):
            if sol:
                res_mat = Solution(sol, board).placement_matrix
                res = np.vectorize(f)(res_mat)
                sheet.range("W10:AG14").value = res
                return
        else:
            app = xw.apps.active
            my_msgBox_macro = app.macro('noSolutionAlert')
            my_msgBox_macro()
            return


@xw.sub
def sgiq_solver_weird():
    wb = xw.Book.caller()
    sheet = wb.sheets["sgiq"]
    input_mat = sheet.range("D17:L25").options(np.array).value
    board = Board(input_mat, SGIQ_BASES)
    maps = {v: k for k, v in board.maps.items()}
    maps.update({-1: ""})
    def f(x): return maps[x]
    X, Y = exact_cover_matrix(board)
    while True:
        for sol in solve(X, Y, []):
            if sol:
                res_mat = Solution(sol, board).placement_matrix
                res = np.vectorize(f)(res_mat)
                sheet.range("T17:AB25").value = res
                return
        else:
            app = xw.apps.active
            my_msgBox_macro = app.macro('noSolutionAlert')
            my_msgBox_macro()
            return
