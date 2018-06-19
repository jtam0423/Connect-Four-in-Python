#Jason Tam 24063520

#USER INTERFACE MODULE

import othello_game_logic

def _gather_input() -> list:
    'Gathers input into a list'
    input_list = []
    while len(input_list) < 5: #only 4 inputs
        x = input()
        input_list.append(x)
    return input_list

def _pieces_on_board(game_list: list) -> list:
    'Returns number of pieces on the board as a list'
    piece_list = []
    black_win = 0
    white_win = 0
    for element in game_list:
        for num in element:
            if num == 1: #BLACK
                black_win +=1
            elif num == 2: #WHITE
                white_win += 1
    piece_list.append(black_win)
    piece_list.append(white_win)
    return piece_list

def _print_pieces(piece_list: list) -> list:
    'Prints the number of pieces each player has'
    black_win = piece_list[0]
    white_win = piece_list[1]
    print("B: " + str(black_win) + "  W: " + str(white_win))

def _print_board(rc_list: list) -> None:
    'Prints the current board; Column first, Then Row'
    cols = []
    displayBoard = []
    for col in rc_list:
        displayRow = []
        for row in col:
            if row == 0: #NONE
                displayRow.append('.')
            if row == 1: #BLACK
                displayRow.append('B')
            if row == 2: #WHITE
                displayRow.append('W')
        displayBoard.append(displayRow)
    for x in range(len(displayBoard[0])):
        for col in displayBoard:
            print(col[x], end = ' ')
        print()

def _run_user_interface() -> None:
    print('FULL')
    list_inputs = _gather_input()
    g = othello_game_logic.GameState(list_inputs)
    game_list = g.new_game()
    _print_pieces(_pieces_on_board(game_list))
    _print_board(game_list)
    print("TURN: " + g.get_turn()) # initial start
    while True:
        x = g.make_turn() #enter loop at input
        try:
            if g.check_gamestate(x, game_list):
                print('VALID')
                g.valid_turn(x, game_list)
                _print_pieces(_pieces_on_board(game_list))
                _print_board(game_list)
                g.change_turn()
                if g.check_board_for_moves(game_list):
                    print("TURN: " + g.get_turn())
                elif g.check_board_for_moves(game_list) == False: #checks for valid moves on other team
                    g.change_turn()
                    if g.check_board_for_moves(game_list) == False: #if also no moves, game over
                        print(g.scoring(_pieces_on_board(game_list)))
                        break
                    else:
                        print("TURN: " + g.get_turn())
                        continue
                else:
                    print(g.scoring(_pieces_on_board(game_list)))
                    break
            elif g.check_gamestate(x, game_list) == False:
                print("INVALID")
                continue
            else:
                print(g.scoring(_pieces_on_board(game_list)))
                break
        except:
            break

if __name__ == '__main__':
    _run_user_interface()
