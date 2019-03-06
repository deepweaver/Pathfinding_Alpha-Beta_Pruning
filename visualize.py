import matplotlib.pyplot as plt 
from matplotlib import colors
import numpy as np


def PlotBoard(board, Xcolor='black', Scolor='yellow', Gcolor='blue', Pcolor='green', _color='white'):
"""
to use this function, input a m x n dimention list
"""
  data = np.zeros((len(board),len(board[0])), dtype=np.uint8)
  cmap = colors.ListedColormap([Xcolor, Scolor, Gcolor, Pcolor, _color])
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == 'X':
        data[i,j] = 0
      elif board[i][j] == 'S':
        data[i,j] = 1
      elif board[i][j] == 'G':
        data[i,j] = 2 
      elif board[i][j] == 'P':
        data[i,j] = 3
      elif board[i][j] == '_':
        data[i,j] = 4
      else:
        print("Something wrong with the board???")
  bounds = [0,1,2,3,4,5]
  norm = colors.BoundaryNorm(bounds, cmap.N)
  fig, ax = plt.subplots()
  ax.imshow(data, cmap=cmap, norm=norm)
  ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
  ax.set_xticks(np.arange(-.5, len(board[0]), 1));
  ax.set_yticks(np.arange(-.5, len(board), 1));
  plt.show()

# PlotBoard(board)