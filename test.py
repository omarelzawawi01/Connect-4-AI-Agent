
import math
import copy
from treelib import Node, Tree
AI=1
PLAYER=2
import string
import random
def calculate_score(board):
      AI_fours=get_fours(board,AI)
      AI_three=get_threes(board,AI)
      AI_two=get_twos(board,AI)
      player_fours=get_fours(board,PLAYER)
      player_three=get_threes(board,PLAYER)
      player_two=get_twos(board,PLAYER)
      return 10*AI_fours+AI_three*5+AI_two*2-10*player_fours-player_three*5-player_two*2

def get_threes(board,turn):
      threes=0
      for iZ in range(len(board)):
            for j in range(len(board[0])):
                  if j < len(board[0])-3:
                        # horizontal right
                        if board[i][j] == board[i][j+1]==board[i][j+2] == turn and board[i][j+3] == 0:
                              threes+=1
                        if i < len(board)-3:
                              #diagonal right down
                              if board[i][j] == board[i+1][j+1]==board[i+2][j+2] == turn and board[i+3][j+3] == 0:
                                    threes+=1
                  if j >=3:
                        #horizontal left
                        if board[i][j] == board[i][j-1]==board[i][j-2] == turn and board[i][j-3] == 0:
                              threes+=1
                        if i< len(board)-3:
                              #diagonal left down
                              if board[i][j] == board[i+1][j-1]==board[i+2][j-2] == turn and board[i+3][j-3] == 0:
                                    threes+=1
                  if i >=3:
                        #vertical
                        if board[i][j] == board[i-1][j]==board[i-2][j] == turn and board[i-3][j] == 0:
                              threes+=1
      return threes

def get_fours(board,turn):
      fours=0
      for i in range(len(board)):
            for j in range(len(board[0])):
                  if j < len(board[0])-3:
                        # horizontal right
                        if board[i][j] == board[i][j+1]==board[i][j+2] == turn == board[i][j+3] :
                              fours+=1
                        if i < len(board)-3:
                              #diagonal right down
                              if board[i][j] == board[i+1][j+1]==board[i+2][j+2] == board[i+3][j+3]  == turn:
                                    fours+=1
                  if j >=3:
                        #horizontal left
                        if board[i][j] == board[i][j-1]==board[i][j-2] == board[i][j-3]  == turn :
                              fours+=1
                        if i< len(board)-3:
                              #diagonal left down
                              if board[i][j] == board[i+1][j-1]==board[i+2][j-2] == turn == board[i+3][j-3]:
                                    fours+=1
                  if i >=3:
                        #vertical
                        if board[i][j] == board[i-1][j]==board[i-2][j] == turn == board[i-3][j]:
                              fours+=1
      return fours



def get_twos(board, turn):
      twos=0
      for i in range(len(board)):
            for j in range(len(board[0])):
                  if j < len(board[0])-3:
                        # horizontal right
                        if board[i][j] == board[i][j+1] == turn and board[i][j+2] == board[i][j+3] == 0:
                              twos+=1
                        if i < len(board)-3:
                              #diagonal right down
                              if board[i][j] == board[i+1][j+1] == turn and board[i+3][j+3] == board[i+2][j+2] == 0:
                                    twos+=1
                  if j >=3:
                        #horizontal left
                        if board[i][j] == board[i][j-1] == turn and board[i][j-3] == board[i][j-2] == 0:
                              twos+=1
                        if i< len(board)-3:
                              #diagonal left down
                              if board[i][j] == board[i+1][j-1] == turn and board[i+3][j-3] == board[i+2][j-2] == 0:
                                    twos+=1
                  if i >=3:
                        #vertical
                        if board[i][j] == board[i-1][j] == turn and board[i-3][j] == board[i-2][j] == 0:
                              twos+=1
      return twos

# def get_best_colomn(board,turn):

#       available_colomns=get_available_colomns(board)
#       best_score=-math.infs
#       best_col=0
#       for j in available_colomns:
#             row = get_available_row(board,j)
#             temp_board=copy.deepcopy(board)
#             play_move(temp_board,row,j,turn)
#             if win(board,AI):
#                   score=25641459
#             else:
#                   score=calculate_score(board, turn)
#             if score > best_score:
#                   best_score=score
#                   best_col=j
#       return best_col

def get_available_colomns(board):
      colomns=list()
      for j in range(len(board[0])):
            if board[0][j] == 0:
                  colomns.append(j)
      return colomns

def get_available_row(board,j):
      for i in range(5,-1,-1):
            if board[i][j] == 0:
                  return i
      return None

def minimax(board,depth,alpha,beta,Maximizing,p,search_tree):
      pruning=0
      availabe_colomns=get_available_colomns(board)
      terminal,winner=if_game_ended(board)
      if depth==0 or terminal:
            if terminal:
                  if winner==AI:
                        stringg=f"alpha: {alpha} beta: {beta} score: 1000000"
                        S = 10  # number of characters in the string.
                        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
                        search_tree.create_node(stringg,ran,parent=p)
                        return(None,1000000)
                  if winner==PLAYER:
                        stringg=f"alpha: {alpha} beta: {beta} score: -1000000"
                        S = 10  # number of characters in the string.
                        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
                        search_tree.create_node(stringg,ran,parent=p)
                        return(None,-1000000)
                  else:
                        stringg=f"alpha: {alpha} beta: {beta} score: 0"
                        S = 10  # number of characters in the string.
                        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
                        search_tree.create_node(stringg,ran,parent=p)
                        return(None,0)

            else:
                  stringg=f"alpha: {alpha} beta: {beta} score: {calculate_score(board)}"
                  S = 10
                  ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
                  search_tree.create_node(stringg,ran,parent=p)
                  return(None,calculate_score(board))
      if Maximizing:
            pruning=0
            maxscore=-math.inf
            colomn=availabe_colomns[0]
            for j in availabe_colomns:
                  row=get_available_row(board,j)
                  temp_board=copy.deepcopy(board)
                  play_move(temp_board,row,j,AI)
                  stringg=f"Maximizing node, alpha: {alpha} beta: {beta} score: {maxscore}"
                  S = 10
                  ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))

                  search_tree.create_node(stringg,ran,parent=p)
                  new_score=minimax(temp_board, depth-1, alpha,beta,False,ran,search_tree)[1]
                  if new_score > maxscore:
                        maxscore=new_score
                        colomn=j
                  alpha=max(alpha,maxscore)
                  if alpha >= beta:
                        pruning=1
                        break
            if pruning==1:
                  stringg=f"Maximizing node (pruning occured), alpha: {alpha} beta: {beta} score: {maxscore}"
                  search_tree.update_node(ran,tag=stringg)
            else:
                  stringg=f"Maximizing node (no pruning occured), alpha: {alpha} beta: {beta} score: {maxscore}"
                  search_tree.update_node(ran,tag=stringg)
            return colomn,maxscore
      else:
            pruning=0
            minscore=math.inf
            colomn=availabe_colomns[0]
            for j in availabe_colomns:
                  row=get_available_row(board,j)
                  temp_board=copy.deepcopy(board)
                  play_move(temp_board,row,j,PLAYER)
                  stringg=f"Minimizing node, alpha: {alpha} beta: {beta} score: {minscore}"
                  S = 10  # number of characters in the string.
                  ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
                  search_tree.create_node(stringg,ran,parent=p)
                  new_score=minimax(temp_board, depth-1, alpha,beta,True,ran,search_tree)[1]
                  if new_score < minscore:
                        minscore=new_score
                        colomn=j
                  beta=min(beta,minscore)
                  if alpha >= beta:
                        pruning=1
                        break
            if pruning==1:
                  stringg=f"Minimzing node (pruning occured), alpha: {alpha} beta: {beta} score: {minscore}"
                  search_tree.update_node(ran,tag=stringg)
            else:
                  stringg=f"Minimizing node (no pruning occured), alpha: {alpha} beta: {beta} score: {minscore}"
                  search_tree.update_node(ran,tag=stringg)
            return colomn,minscore


def play_move(board,row,col,turn):
      board[row][col]=turn

def if_game_ended(board):
      for j in range(len(board[0])):
            if board[0][j] == 0:
                  return (False,0)
      playerfours=get_fours(board,PLAYER)
      AIfours=get_fours(board,AI)
      if playerfours==AIfours:
            return(True,0)
      elif playerfours > AIfours:
            return (True,PLAYER)
      else:
            return (True,AI)

def print_arr(arr):
      print("\n\n\n\n\n\n\n\n\n\n\n")
      for row in range(6):
            print("-"*35)
            for col in range(7):
                  if arr[row][col]==0:
                        print("|   |", end="")
                  else:
                        print("| " + str(arr[row][col]) + " |", end="")
            print()
      print("-"*35)
board=      [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],]

print_arr(board)


while True:
      col=int(input("Enter col:"))
      if get_available_row(board, col) != None:
            play_move(board,get_available_row(board,col),col,2)
      print_arr(board)
      search_tree=Tree()
      search_tree.create_node("Parent",0)
      nextcol,score=minimax(board,2,-math.inf,math.inf,True,0,search_tree)
      stringg=f"Max score:{score}, Next colomn: {nextcol}"

      search_tree.update_node(0,tag=stringg)
      search_tree.show()
      if nextcol == None:
            if score == 1000000:
                  print("AI WINS")
            elif score == -1000000:
                  print("PLAYER WINS")
            else:
                  print("TIE")
            print_arr(board)
            break
      else:
            play_move(board,get_available_row(board,nextcol),nextcol,1)
            print_arr(board)
# a=1
# b=2
# string=f"Five plus ten is {a + b} and not {2 * (a + b)}"
# search=Tree()
# search.create_node(string, 0 )
# search.create_node(string,1,parent=0)
# search.show()
# print(string)











