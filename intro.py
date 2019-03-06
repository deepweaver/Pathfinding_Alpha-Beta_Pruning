from visualize import PlotBoard

strboard = '''XXXXXXXXXX
X___XX_X_X
X_X__X___X
XSXX___X_X
X_X__X___X
X___XX_X_X
X_X__X_X_X
X__G_X___X
XXXXXXXXXX'''
# print(strboard)
board = board = [[j for j in range(10)] for i in range(9)] 
for i in range(9):
  for j in range(10):
    board[i][j] = strboard.split('\n')[i][j]
PlotBoard(board)





