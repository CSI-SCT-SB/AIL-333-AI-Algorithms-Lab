
import math 
game_state=[[' ',' ',' '],
		   [' ',' ',' '],
		   [' ',' ',' ']]
players=['X','O']

def play_move(state,player,block_num):
	if state[int((block_num-1)/3)][(block_num-1)%3]==' ': 
		state[int((block_num-1)/3)][(block_num-1)%3]=player
	else:
		block_num=int(input("block already occupied! enter new block number(1-9)"))
		play_move(state,player,block_num)

def copy_game_state(state):
	new_state=[[' ',' ',' '],
		   [' ',' ',' '],
		   [' ',' ',' ']]
	for i in range(3):
		for j in range(3):
			new_state[i][j]=state[i][j]
	return  new_state

def check_current_state(game_state):
	
	#horizontal
	if (game_state[0][0]==game_state[0][1] and game_state[0][1]==game_state[0][2] and game_state[0][0]!=' '):
		return game_state[0][0],"Done"			
	if (game_state[1][0]==game_state[1][1] and game_state[1][1]==game_state[1][2] and game_state[1][0]!=' '):
		return game_state[1][0],"Done"		
	if (game_state[2][0]==game_state[2][1] and game_state[2][1]==game_state[2][2] and game_state[2][0]!=' '):
		return game_state[2][0],"Done"	
	#vertical
	if (game_state[0][0]==game_state[1][0] and game_state[1][0]==game_state[2][0] and game_state[0][0]!=' '):
		return game_state[0][0],"Done"			
	if (game_state[0][1]==game_state[1][1] and game_state[1][1]==game_state[2][1] and game_state[0][1]!=' '):
		return game_state[0][1],"Done"		
	if (game_state[0][2]==game_state[1][2] and game_state[1][2]==game_state[2][2] and game_state[0][2]!=' '):
		return game_state[0][2],"Done"	
	#diagonal
	if (game_state[0][0]==game_state[1][1] and game_state[1][1]==game_state[2][2] and game_state[0][0]!=' '):
		return game_state[0][0],"Done"			
	if (game_state[0][2]==game_state[1][1] and game_state[1][1]==game_state[2][0] and game_state[0][2]!=' '):
		return game_state[2][0],"Done"		
	draw_flag=0
	for i in range(3):
		for j in range(3):
			if game_state[i][j]==' ':
				draw_flag=1	
	if draw_flag==0:
		return None,"Draw"
	return None,"Not Done"

def print_board(game_state):
	print("-------")
	print("|"+str(game_state[0][0])+"|"+str(game_state[0][1])+"|"+str(game_state[0][2])+"|")	
	print("|"+str(game_state[1][0])+"|"+str(game_state[1][1])+"|"+str(game_state[1][2])+"|")	
	print("|"+str(game_state[2][0])+"|"+str(game_state[2][1])+"|"+str(game_state[2][2])+"|")	
	print("-------")			
		
def getBestMove(state,player):
	winner_loser,done=check_current_state(state)
	if done=="Done" and winner_loser=='O':
		return (1,0)
	elif done=="Done" and winner_loser=='X':
		return (-1,0)
	elif done=="Draw":
		return (0,0)
	moves=[]
	empty_cells=[]
	for i in range(3):
		for j in range(3):
			if state[i][j]==' ':
				empty_cells.append(i*3+(j+1))
	for empty_cell in empty_cells:
		move={}
		move['index']=empty_cell
		new_state=copy_game_state(state)
		play_move(new_state,player,empty_cell)
		if player=='O':
			result,_=getBestMove(new_state,'X')
			move['score']=result
		else:
			result,_=getBestMove(new_state,'O')
			move['score']=result				
		moves.append(move)
	best_move=None
	if player=='O':
		best=-math.inf
		for move in moves:
			if move['score']>best:
				best=move['score']
				best_move=move['index']
	else:
		best=math.inf
		for move in moves:
			if move['score']<best:
				best=move['score']
				best_move=move['index'] 
	return (best,best_move)
	
					
#main						
play_again='Y'
while play_again=='Y' or play_again=='y':
	game_state=[[' ',' ',' '],
		   	   [' ',' ',' '],
		  	   [' ',' ',' ']]
	current_state="Not Done"
	print("NEW GAME")
	print_board(game_state)
	player_choice=input("who makes the first move you(X) or ai(O)")
	Winner=None
	if player_choice=='x' or player_choice=='X':
		current_player=0
	else:
		current_player=1
	while current_state=="Not Done":
		if current_player==0:
			block_choice=int(input("enter which block to mark(1-9)"))
			play_move(game_state,players[current_player],block_choice)
		else:
			_,block_choice=getBestMove(game_state,players[current_player])
			play_move(game_state,players[current_player],block_choice)
			print("ai plays move"+str(block_choice))
		print_board(game_state)
		Winner,current_state=check_current_state(game_state)
		if Winner is not None:
			print(str(Winner)+" won!")
		else:		
			current_player=(current_player+1)%2
		if current_state=="Draw":
			print("Draw")
	play_again=input("play again? (y/n)")
	if play_again=='N' or play_again=='n':
		print("GAME OVER")
"""
NEW GAME
-------
| | | |
| | | |
| | | |
-------
who makes the first move you(X) or ai(O)x
enter which block to mark(1-9)5
-------
| | | |
| |X| |
| | | |
-------
ai plays move1
-------
|O| | |
| |X| |
| | | |
-------
enter which block to mark(1-9)3
-------
|O| |X|
| |X| |
| | | |
-------
ai plays move7
-------
|O| |X|
| |X| |
|O| | |
-------
enter which block to mark(1-9)4
-------
|O| |X|
|X|X| |
|O| | |
-------
ai plays move6
-------
|O| |X|
|X|X|O|
|O| | |
-------
enter which block to mark(1-9)2
-------
|O|X|X|
|X|X|O|
|O| | |
-------
ai plays move8
-------
|O|X|X|
|X|X|O|
|O|O| |
-------
enter which block to mark(1-9)9
-------
|O|X|X|
|X|X|O|
|O|O|X|
-------
Draw
play again? (y/n)n
GAME OVER

"""					
