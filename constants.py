import numpy as np

from models import Base

# Define constants related to pentoominoes

PENT_BASES = [Base('L', 1, np.array([[1, 1, 1, 1], [0, 0, 0, 1]])),
              Base('F', 2, np.array([[0, 2, 2], [2, 2, 0], [0, 2, 0]])),
              Base('N', 3, np.array([[3, 0], [3, 0], [3, 3], [0, 3]])),
              Base('P', 4, np.array([[4, 4, 4], [4, 4, 0]])),
              Base('Y', 5, np.array([[5, 0], [5, 0], [5, 5], [5, 0]])),
              Base('T', 6, np.array([[6, 6, 6], [0, 6, 0], [0, 6, 0]]), 4, 1),
              Base('U', 7, np.array([[7, 0, 7], [7, 7, 7]]), 4, 1),
              Base('V', 8, np.array([[8, 0, 0], [8, 0, 0], [8, 8, 8]]), 4, 1),
              Base('W', 9, np.array([[9, 0, 0], [9, 9, 0], [0, 9, 9]]), 4, 1),
              Base('Z', 10, np.array(
                  [[10, 10, 0], [0, 10, 0], [0, 10, 10]]), 2, 2),
              Base('I', 11, np.array([[11], [11], [11], [11], [11]]), 2, 1),
              Base('X', 12, np.array(
                  [[0, 12, 0], [12, 12, 12], [0, 12, 0]]), 1, 1)
              ]


# Define constants related to smartgames IQ puzzle

SGIQ_BASES = [Base('A', 1, np.array([[0, 0, 1, 0], [1, 1, 1, 1]])),
              Base('B', 2, np.array([[0, 0, 2], [2, 2, 2], [0, 2, 0]])),
              Base('C', 3, np.array([[3, 3, 3, 3], [0, 0, 0, 3]])),
              Base('D', 4, np.array([[0, 4], [4, 4], [4, 0]]),2,2),
              Base('E', 5, np.array([[5, 0], [5, 0], [5, 5], [0, 5]])),
              Base('F', 6, np.array([[0, 6, 6], [6, 6, 0], [6, 0, 0]]), 4, 1),
              Base('G', 7, np.array([[7, 7, 7], [7, 0, 0]])),
              Base('H', 8, np.array([[0, 0, 8], [0, 0, 8], [8, 8, 8]]), 4, 1),
              Base('I', 9, np.array([[9, 9], [0, 9]]), 4, 1),
              Base('J', 10, np.array([[10, 0], [10, 10], [10, 10]])),
              Base('K', 11, np.array([[11, 11, 11], [0, 11, 0]]), 4, 1),
              Base('L', 12, np.array([[12, 12], [0, 12], [12, 12]]), 4, 1)
              ]
