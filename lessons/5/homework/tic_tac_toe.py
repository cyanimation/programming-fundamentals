#!/usr/bin/env python

# import some modules so that we get some extra functionality
import os
import sys

# REMEMBER THAT THE PROGRAM WILL LOOK FOR THE if __name__ == '__main__' LINE?
# YOU SHOULD TOO. THAT'S WHERE THE PROGRAM WILL BEGIN. IT IS ALWAYS FOUND AT 
# THE END OF THE FILE. 


def parse_results(results):
    """ parses the results file into a dictionary of names and tuples """
    # hold the results in a dictionary
    results_dict = {}
    # loop over each line (result)
    for result in results:
        # split the string based on spaces
        parts = result.split()
        # there should only be a name and an outcome ('w', 'l')
        if len(parts) > 2:
            raise Exception("the results file has a bad format")
        # keep track of the name and the outcome so I don't have to use 
        # parts[0] and parts[1]
        name = parts[0]
        outcome = parts[1]
        # add the name to the dictionary if it's not already there
        if name not in results_dict:
            results_dict[name] = (0, 0)
        # modify the results tuple according to whether its a win or loss
        if outcome == 'w':
            results_dict[name] = (results_dict[name][0]+1, results_dict[name][1])
        elif outcome == 'l':
            results_dict[name] = (results_dict[name][0], results_dict[name][1]+1)
        else:
            raise Exception("I didn't recognize the outcome")
    return results_dict


def print_board(board):
    """ prints the grid with the appropriate X and 0 symbols """
    if not board or len(board) < 1:
        raise Exception("I don't have a valid board")
    cur_ascii = 65 # The ASCII value of 'A' (the rows)
    cur_num = 0 # (the cols)
    # add space at beginning of nums to account for row headers
    sys.stdout.write('  ')
    # print the column numbers
    for cols in range(len(board[0])):
        sys.stdout.write(" %d" % (cur_num))
        cur_num += 1
    sys.stdout.write('\n')
    # add a line at the top of the table
    sys.stdout.write('  ' + '-' * (len(board[0]) * 2 + 1) + '\n')
    # print the row letters
    for row in board:
        sys.stdout.write(chr(cur_ascii) + " ")
        cur_ascii += 1
        for col in row:
            sys.stdout.write('|%s' % (col))
        sys.stdout.write('|\n')
        sys.stdout.write('  ' + '-' * (len(row) * 2 + 1) + '\n')


def write_result(results_file, outcome, player_1, player_2):
  """ writes the results of the game to the file """
  # append the outcome to the file
  with open(results_file, 'a') as f:
      # write the outcome from player 1's perspective
      f.write("%s %s\n" % (player_1, map_outcome(int(outcome))))
      # write the outcome from player 2's perspective (hence the not)
      f.write("%s %s\n" % (player_2, map_outcome(int(not outcome))))


def print_records(results_file, player_1, player_2):
  """ print the players' records to the console """
  # keep track of the results in the file
  results_lines = []

  # read all of the lines from the file into a list
  with open(results_file) as f:
    results_lines = f.readlines()

  # parse the results (results will be a dictionary of string and tuple)
  # { string->name: tuple->(int->wins, int->losses) }
  # { 'reed': (2, 5), 'britney': (5, 2) }
  results = parse_results(results_lines)

  player_1_wins = results[player_1][0]
  player_1_losses = results[player_1][1]
  player_2_wins = results[player_2][0]
  player_2_losses = results[player_2][1]

  print "\n%s's record is %d wins and %d losses" % (player_1, player_1_wins, player_1_losses)
  print "\n%s's record is %d wins and %d losses" % (player_2, player_2_wins, player_2_losses)


def map_outcome(outcome):
  """ 
  turns the integer outcome of 1 (win) and 0 (loss) into a string 
  representation
  """
  return 'w' if outcome == 1 else 'l'


def parse_move(move):
    """ pulls the column and row out of the move """
    if not (len(move) == 2):
        return None, None
    try:
        row = ord(move[0].upper()) - 65
        col = int(move[1])
    except:
        return None, None
    return row, col


def valid_move(board, row, col):
    """ tests whether or not the given row and column are valid """
    return board[row][col] == '-'


def get_winner(board):
    """ finds out if there is a winner and who won """

    def who_won(in_a_row, board_size, cur_player):
        """ 
        a function private to get_winner() (yes you can do this. Cool huh!?) 
        that tells get_winner if it has a winner 
        """
        if in_a_row == board_size:
            return 1 if cur_player == 'X' else 2
        else:
            return 0

    def test_row_col(board, rows):
        """ private function to test the rows and columns """
        for i in range(len(board)):
            cur_player = board[i][0] if rows else board[0][i]
            in_a_row = 0
            for j in range(len(board)):
                symbol = board[i][j] if rows else board[j][i]
                if (not symbol == '-') and (symbol == cur_player):
                    in_a_row += 1
                else:
                    break
            winner = who_won(in_a_row, len(board), cur_player)
            if not winner == 0:
                return winner
        return 0

    def test_diagonal(board, normal):
        """ private function to test the two diagonals """
        cur_player = board[0][0] if normal else board[0][len(board)-1]
        in_a_row = 0
        for i in range(len(board)):
            symbol = board[i][i] if normal else board[i][len(board)-1-i]
            if (not symbol == '-') and (symbol == cur_player):
                in_a_row += 1 
            else:
                break
            winner = who_won(in_a_row, len(board), cur_player)
            if not winner == 0:
                return winner
        return 0


    # test rows
    winner = test_row_col(board, True)
    if not winner == 0:
        return winner

    # test cols
    winner = test_row_col(board, False)
    if not winner == 0:
        return winner

    # test diagonal from top left to bottom right
    winner = test_diagonal(board, True)
    if not winner == 0:
        return winner

    # test diagonal from top right to bottom left
    winner = test_diagonal(board, False)
    if not winner == 0:
        return winner

    return 0


def make_move(board, player_num, row, col):
    """ places the player's mark in the row and column """
    board[row][col] = 'X' if player_num == 1 else 'O'


def create_board(board_size):
    """ creates a square board based on the given board size """
    board = []
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append('-')
        board.append(row)
    return board


def tic_tac_toe(board, player_1, player_2):
    """ the main tic-tac-toe logic """
    # do an initial clear
    os.system('clear')
    winner = False
    cur_player = player_1
    player_num = 1
    # do Tic-Tac-Toe until we have found a winner
    while not winner:
        print_board(board)
        move = raw_input('\n%s, where would you like to go? ' % (cur_player))
        row, col = parse_move(move)
        # if we couldn't parse the move then try again
        if row == None or col == None:
            os.system('clear')
            print "I didn't recognize your move!"
            print "Make sure your move is a row and column with no spaces (A4)\n"
            continue
        # if they moved somewhere there is already a mark then try again
        if not valid_move(board, row, col):
            os.system('clear')
            print "You can't move there! Try again.\n"
            continue
        # mark the move on the board
        make_move(board, player_num, row, col)
        # see if there is a winner
        winner = get_winner(board)
        # switch turns
        cur_player = player_2 if cur_player == player_1 else player_1
        player_num = 2 if player_num == 1 else 1
        os.system('clear')
    # the winner will either be 1 or 2. If 1 then outcome is True (for player 1)
    outcome = True if winner == 1 else False
    return outcome


def main():
  """ This is the main function that is our initial entry point into our program """
  # clear the console screen
  os.system('clear')

  # get the names of the players
  player_1 = raw_input('What is the name of player 1? ')
  player_2 = raw_input('What is the name of player 2? ')

  # ask for the board size
  try:
      board_size = raw_input('How many rows and columns would you like to play with (3)? ')
      if board_size.strip() == '':
          board_size = 3
      else:
          board_size = int(board_size)
  except Exception as e:
      print "I don't recognize your board size. Try again."
      sys.exit()

  # create the board (initialize with '-' instead of X and 0)
  board = create_board(board_size)

  # do tic-tac-toe until a winner is found
  outcome = tic_tac_toe(board, player_1, player_2)

  # print the outcome
  os.system('clear')
  print_board(board)
  print "\n%s wins!" % (player_1 if outcome == 1 else player_2)


  # The code below writes the outcome to a file and then determines each 
  # player's record. All you need to do is ensure that outcome is a boolean 
  # value with True representing a win for player 1 and ensure that player_1 
  # and player_2 are both set.


  # the name of our game results file
  results_file = 'game_results.txt'

  write_result(results_file, outcome, player_1, player_2)

  print_records(results_file, player_1, player_2)


  # wait for the user to press enter to quit
  raw_input('\nPress enter to quit...')

  # clear the console screen
  os.system('clear')


# this makes it so that when you run your file that it will call the main
# function. It is always good practice to do this. We put all of the runtime
# functionality in the main function
if __name__ == '__main__':
  main()
