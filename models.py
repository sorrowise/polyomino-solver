import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


plt.rcParams['figure.figsize'] = (15, 9.27)


class Base:
    def __init__(self, shape, baseid, mat, rot_c=4, flip_c=2):
        self.shape = shape
        self.baseid = baseid
        self.mat = mat
        self.rc = rot_c
        self.fc = flip_c

    @property
    def variants(self):
        res = []
        for r in range(self.rc):
            for f in range(self.fc):
                res.append(self.shape+str(r)+str(f))
        return res


class Poly:
    def __init__(self, name, bases):
        self.name = name
        self.shape = name[0]
        self.rot = int(name[1])
        self.flipped = int(name[2])
        self.bases = get_all_bases(bases)

    def repr_mat(self):
        mat = self.bases[self.shape]
        if self.flipped == 1:
            return np.fliplr(np.rot90(mat, self.rot))
        else:
            return np.rot90(mat, self.rot)

    def region(self):
        return self.repr_mat().nonzero()

    def draw(self):
        sns.heatmap(self.repr_mat(), square=True, cbar=False,
                    xticklabels=False, yticklabels=False,
                    linewidth=1, cmap="Greens")


class Board:
    def __init__(self, input_mat, bases):
        self.br = input_mat.shape[0]
        self.bc = input_mat.shape[1]
        self.bases = bases
        self.input_mat = input_mat
        self.maps = {x.shape: x.baseid for x in self.bases}
        self.shapes = set(get_all_bases(self.bases).keys())

    @property
    def mat(self):
        f = lambda x: self.maps.get(x,0) if x != "no" else -1
        arr = [[f(x) for x in row] for row in self.input_mat]
        return np.array(arr)

    @property
    def usable_shapes(self):
        used_shapes = set()
        for row in self.input_mat:
            for x in row:
                if x != 0:
                    used_shapes.add(x)
        return self.shapes - used_shapes

    @property
    def usable_names(self):
        all_names = set(get_all_names(self.bases))
        return {x for x in all_names if x[0] in self.usable_shapes}

    @property
    def non_empty_cells(self):
        rows, cols = self.mat.nonzero()
        res = {(x+1, y+1) for x, y in zip(rows, cols)}
        return res

    @property
    def forbid_cells(self):
        res = set()
        for i in range(self.br):
            for j in range(self.bc):
                if self.mat[i, j] == -1.:
                    res.add((i+1, j+1))
        return res

    def draw(self):
        sns.heatmap(self.mat, square=True, cbar=False,
                    xticklabels=False, yticklabels=False,
                    linewidth=1, center=6)
        plt.show()

    @property
    def placeable_area(self):
        res = set()
        for i in range(self.br):
            for j in range(self.bc):
                if self.mat[i,j] == 0:
                    res.add((i+1,j+1))
        return res

    def possible_placement(self, poly):
        placement = {}
        rgr, rgc = poly.region()
        p_area = self.placeable_area
        for i in range(1, self.br+1):
            for j in range(1, self.bc+1):
                plr, plc = i + rgr, j + rgc
                if all((x, y) in p_area for x, y in zip(plr, plc)):
                    placement[(poly.name, (i, j))] = [poly.shape] + \
                        [(r, c) for r, c in zip(plr, plc)]
        return placement


class Solution:
    def __init__(self, solution, board):
        self.sol = solution
        self.board = board
        self.shapes = board.shapes
        self.bases = board.bases

    @property
    def placement_matrix(self):
        mat = self.board.mat
        for name, (r, c) in self.sol:
            R, C = Poly(name, self.bases).region()
            for x, y in zip(R, C):
                mat[r+x-1, c+y -
                    1] = self.board.maps[Poly(name, self.bases).shape]
        return mat

    def draw(self):
        mat = self.placement_matrix
        sns.heatmap(mat, square=True, cbar=False,
                    xticklabels=False, yticklabels=False,
                    linewidth=1, center=6)


def get_all_bases(bases):
    res = {x.shape: x.mat for x in bases}
    return res


def get_all_names(bases):
    res = []
    for base in bases:
        res.extend(base.variants)
    return res
