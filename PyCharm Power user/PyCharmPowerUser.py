def show_gameboard(b):
  for r in b:
   print(" | ".join(r))
   print("-"*5)
 
 
def game_won(b, p):
  for i in range(3):
   if all(b[i][j]==p for j in range(3)) or all(b[j][i]==p for j in range(3)):
    return True
  if all(b[i][i]==p for i in range(3)) or all(b[i][2-i]==p for i in range(3)):
   return True
  return False
 
 
def board_full(b):
 return all(c!=" " for r in b for c in r)
 
 
def app():
  gameboard=[[" "for _ in range(3)]for _ in range(3)]
  players=["X","O"]
  print("Tic-Tac-Toe Game")
  show_gameboard(gameboard)
  for turn in range(9):
   current_player=players[turn%2]
   while 1:
    try:
     x_coord,y_coord=map(int,input(f"Player {current_player}, enter row col (between 0-2): ").split())
     if gameboard[x_coord][y_coord]==" ":
      gameboard[x_coord][y_coord]=current_player
      break
     else:
      print("Nope, that space is taken. Try again.")
    except:
     print("Invalid grid, enter integer between 0-2 pls.")
   show_gameboard(gameboard)
   if game_won(gameboard, current_player):
    print(f"P {current_player} wins!")
    return
   if board_full(gameboard):
    print("Draw!")
    return
  print("Draw!")
 
 
app()
