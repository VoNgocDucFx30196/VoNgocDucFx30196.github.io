
def checkWin(grid):
  row = ''
  col = ''
  diag = ''
  win = ''
  #check row
  for i in range(len(grid)):
    for y in range(len(grid[1])):
      row = row +grid[i][y]
    if 'XXXXX' in row:
      win = 'X'
    elif 'OOOOO' in row:
      win = 'O'
    row = ''
  #check colunm
  for i in range(len(grid[0])):
    for y in range(len(grid)):
      col = col + grid[y][i]
    if 'XXXXX' in col:
      win = 'X'
    elif 'OOOOO' in col:
      win = 'O'
    col = ''
  #check diagonal
  for r in range(len(grid)):
    c = 0
    while r >= 0 and c < len(grid[0]):
      diag = diag + grid[r][c]
      c = c + 1
      r = r - 1
    if 'XXXXX' in diag:
      win ='X'
    if 'OOOOO' in diag:
      win = 'O'
    diag = ''
  diag = ''
  for c in range(len(grid[0])):
    r = len(grid)-1
    while r >= 0 and c < len(grid[0]):
      diag = diag + grid[r][c]
      r = r - 1
      c = c+1
    if 'XXXXX' in diag:
      win ='X'
    if 'OOOOO' in diag:
      win = 'O'
    diag = ''
  diag = ''
  for c in range(len(grid[0])):
    r = 0
    while r < len(grid) and c < len(grid[0]):
      diag = diag + grid[r][c]
      r = r + 1
      c = c + 1
    if 'XXXXX' in diag:
      win ='X'
    if 'OOOOO' in diag:
      win = 'O'
    diag = ''
  diag = ''
  for r in range(len(grid)):
    c = 0
    while r < len(grid) and c < len(grid[0]):
      diag = diag + grid[r][c]
      c = c + 1
      r = r + 1
    if 'XXXXX' in diag:
      win ='X'
    if 'OOOOO' in diag:
      win = 'O'
      diag = ''
  return win
