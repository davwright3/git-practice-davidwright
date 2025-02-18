def show_gameboard(b):
 for r in b:
  print(" | ".join(r))
  print("-"*5)
 
 
def c_w(b,p):
 for i in range(3):
  if all(b[i][j]==p for j in range(3)) or all(b[j][i]==p for j in range(3)):
   return True
 if all(b[i][i]==p for i in range(3)) or all(b[i][2-i]==p for i in range(3)):
  return True
 return False
 
 
def f(b):
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
     r,c=map(int,input(f"P {current_player}, row col (0-2): ").split())
     if gameboard[r][c]==" ":
      gameboard[r][c]=current_player
      break
     else:
      print("Nope. Again.")
    except:
     print("Wrong. 0-2 pls.")
   show_gameboard(gameboard)
   if c_w(gameboard,current_player):
    print(f"P {current_player} wins!")
    return
   if f(gameboard):
    print("Draw!")
    return
  print("Draw!")
 
 
app()
