import turtle
import logic

CELLSIZE = 30


# Fullscreen the canvas

screen = turtle.Screen()
screen.setup(1.0, 1.0)
t = turtle.Turtle()
ROW = int(t.screen.numinput("Input row","Row:",5,5,10))
COL = int(t.screen.numinput("Input col","Col:",5,5,10))
winner = ['',False]
grid=[['-' for c in range(COL)] for r in range(ROW)]
turn="X"
t.speed(0)
t.penup()
t.goto(-1*CELLSIZE*COL/2,CELLSIZE*ROW/2)
o_pos = t.pos()
t.pendown()
for i in range(ROW):
  for i in range(COL):
    for i in range(4):
      t.forward(CELLSIZE)
      t.right(90)
    t.forward(CELLSIZE)
  t.right(90)
  t.forward(CELLSIZE)
  t.right(90)
  t.forward(CELLSIZE*COL)
  t.right(180)
def checkInput(x,y):
  X=int(abs(x-(-1*CELLSIZE*COL/2))//CELLSIZE)
  Y=int(abs(y-(CELLSIZE*ROW/2))//CELLSIZE)
  
  
  if (x>o_pos[0] and x<o_pos[0]+(CELLSIZE*COL)) and (y<o_pos[1] and y>o_pos[1]-(CELLSIZE*ROW)):
    if grid[X][Y]=='-':
      return True
  return False
def drawO():
  t.pencolor("blue")
  t.right(90)
  t.forward((CELLSIZE*2)/3/2)
  t.left(90)
  t.down()
  t.circle((CELLSIZE*2)/3/2)
  t.up()
  t.left(90)
  t.forward((CELLSIZE*2)/3/2)
  t.right(90)
  t.pencolor("black")
def drawX():
  t.pencolor("red")
  t.down()
  t.setheading(45)
  t.forward((CELLSIZE*2)/6)
  t.backward(((CELLSIZE*2)/6)*2)
  t.forward((CELLSIZE*2)/6)
  t.setheading(135)
  t.forward((CELLSIZE*2)/6)
  t.backward(((CELLSIZE*2)/6)*2)
  t.forward((CELLSIZE*2)/6)
  t.setheading(0)
  t.up()
  t.pencolor("black")
def showBoard(grid):
  for i in range(len(grid)):
    row = ''
    for y in range(len(grid[0])):
      row = row+grid[y][i]
    print(row)

def showWinPlayer():
    t.goto(0,CELLSIZE*ROW/2)
    t.write(winner[0]+" WIN",align="center",font=('Arial',30,'normal'))
    
def updateGrid(col,row,XorO):
    global grid
    print(col,row)
    if grid[col][row]=='-':
      grid[col][row]=XorO
    print(grid)
    winner[0]=logic.checkWin(grid)
    if winner[0]:
      winner[1]=True
      showWinPlayer()
    showBoard(grid)
def oClick(x,y):
  global turn
  t.up()
  t.goto(-1*CELLSIZE*COL/2,CELLSIZE*ROW/2)
  X=abs(x-(-1*CELLSIZE*COL/2))//CELLSIZE
  Y=abs(y-(CELLSIZE*ROW/2))//CELLSIZE
  print(str(X)+","+str(Y))
  t.goto((-1*CELLSIZE*COL/2)+(CELLSIZE/2)+(X*CELLSIZE),((CELLSIZE*ROW/2)-(CELLSIZE/2)-(Y*CELLSIZE)))
  if turn=="X" and not winner[1] and checkInput(int(x),int(y)):
    drawX()
    updateGrid(int(X),int(Y),turn)
    turn = "O"
  elif turn=="O" and  not winner[1] and checkInput(int(x),int(y)):
    drawO()
    updateGrid(int(X),int(Y),turn)
    turn="X"
  t.up()

screen.onclick(oClick)
screen.mainloop()