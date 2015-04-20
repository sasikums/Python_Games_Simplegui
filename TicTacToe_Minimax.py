"""
Mini-max Tic-Tac-Toe Player
http://www.codeskulptor.org/#user39_As4hTyJT92_4.py
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
   
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    
    The function creates a 'tree' of possible moves. The root
    of the tree is the current board. The first branch is all
    possible moves from the current board, i.e. to the currently
    empty squares. It cycles through each branch with a minmax
    function to calculate best move
    """
    # check if current board results in a win
    if board.check_win()!=None:
        return SCORES[board.check_win()], (-1, -1)
    else:
        # if board is not a win, loops through all
        # empty squares to check possible moves
        best_score = None #init best_score to empty
        for square in board.get_empty_squares():
            #simulates a board copy with the move to
            # the empty square
            board_copy = board.clone()
            board_copy.move(square[0],square[1],player)
            
            # score of board with move is the recursively
            # calculated score of the next branch
            score, dummy_move = mm_move(board_copy,
                                       provided.switch_player(player))
            # if move results in a player win thats
            # the best move
            if board_copy.check_win()== player:
                return SCORES[board_copy.check_win()], square
            else:
                if score * SCORES[player] > best_score or score == 0:	
                    best_score, best_move = score, square               
        return best_score, best_move   
             
                                       
            
            
        
    return 0, (-1, -1)

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.
#provided.play_game(move_wrapper, 1, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
