Height = 6
Width = 7

def init():
  board = [] #an array
  for i in range(Height):
    board.append(["O"] * Width)
  return board


def print_board(board):
  print("1 2 3 4 5 6 7")
  print("_" * 13)
  for row in board:
    print("|".join(row))

def get_move(board, player):
  column = int(input("Player {} enter a column".format(player)))
  if (column < 1 or column > Width):
    print("Not valid buddy, one between 1 and 7")
    column = get_move(board, player)

  column -= 1

  column_full = True

  for i in range(Height):
    if board[i][column] == "O":
      column_full = False
      break
  if column_full: 
    print("This coumn is full. Please try again.")
    column = get_move(board, player)
  return column