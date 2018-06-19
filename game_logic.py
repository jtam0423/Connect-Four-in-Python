#Jason Tam 24063520

#GAME LOGIC

NONE = 0
BLACK = 1
WHITE = 2

MOVE_LIST = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]

class GameError(Exception):
    '''
    Raised whenever an attempt to use a NoneType
    '''
    pass

class GameState:
    def __init__(self, inp_list: list):
        self._inp = inp_list
        self._rows = int(inp_list[0])
        self._columns = int(inp_list[1])
        self._turn = inp_list[2]
        self._position = inp_list[3]
        self._mode = inp_list[4]

    def make_turn(self) -> list:
        "Takes in user input and places in list"
        player_input = input()
        new_list = player_input.split()
        try:
            for num in range(len(new_list)):
                new_list[num] = int(new_list[num]) - 1
        except:
            return []
        return new_list
        
    def check_gamestate(self, make_list: list, game_list: list) -> bool:
        "Evaluates if valid move available"
        try:
            row = make_list[0]
            column = make_list[1]
            if row > self._rows - 1 or column > self._columns - 1:
                raise GameError()
            elif row < 0 or column < 0:
                raise GameError()
            elif self.check_disc_cell(row, column, game_list) != 0:
                raise GameError()
            elif len(self.list_of_moves(make_list, game_list, self.get_opposite_num())) == 0:
                raise GameError()
            elif self.use_find(row, column, game_list) == False:
                raise GameError()
            else:
                return True
        except:
            return False

    def list_of_moves(self, make_list:list, game_list: list, color: int) -> list:
        'Returns list one of pieces around it is same or different'
        row = make_list[0]
        column = make_list[1]
        new_list = []
        for coordinate in MOVE_LIST:
            x = row + coordinate[0]
            y = column + coordinate[1]
            if x >= 0 and x <= self._rows - 1:
                if y >= 0 and y <= self._columns - 1:
                    if game_list[y][x] == color:
                        new_list.append((x,y))
        return new_list

    def check_list(self, find_list: list, game_list: list)-> int:
        'Checks the list for something to flip, returns coordinates to flip'
        if len(find_list) > 0:
            if find_list[0] != self.get_opposite_num():
                return None
            for num in range(len(find_list)):
                if num != 0:
                    if find_list[num] == self.get_turn_num():
                        if find_list[num - 1] == self.get_opposite_num():
                            return num
        else:
            return None
            
    def right_find(self, row: int, column: int, game_list: list) -> int:
        'Mutates a list of coordinates in the specified direction: Right'
        coord_list = []
        rf_list = []
        try:
            while True:
                if column + 1 < self._columns:
                    column += 1
                    coord_list.append(column)
                    rf_list.append(game_list[column][row])
                else:
                    break
        except:
            return None
        checked = self.check_list(rf_list, game_list)
        try:
            for num in range(checked):
                coord_num = coord_list[num]
                self.change_piece_color(row, coord_num, game_list)
        finally:
            return checked

    
    def left_find(self, row: int, column: int, game_list: list) -> int:
        'Mutates a list of coordinates in the specified direction: Left'
        coord_list = []
        rf_list = []
        try:
            while True:
                if column - 1 >= 0:
                    column += -1
                    coord_list.append(column)
                    rf_list.append(game_list[column][row])
                else:
                    break
        except:
            return None
        checked = self.check_list(rf_list, game_list)
        try:
            for num in range(checked):
                coord_num = coord_list[num]
                self.change_piece_color(row, coord_num, game_list)
        finally:
            return checked

    def up_find(self, row: int, column: int, game_list: list) -> int:
        'Mutates a list of coordinates in the specified direction: Up'
        coord_list = []
        rf_list = []
        try:
            while True:
                if row - 1 >= 0:
                    row += -1
                    coord_list.append(row)
                    rf_list.append(game_list[column][row])
                else:
                    break
        except:
            return None
        checked = self.check_list(rf_list, game_list)
        try:
            for num in range(checked):
                coord_num = coord_list[num]
                self.change_piece_color(coord_num, column, game_list)
        finally:
            return checked

    def down_find(self, row: int, column: int, game_list: list) -> int:
        'Mutates a list of coordinates in the specified direction: Down'
        coord_list = []
        rf_list = []
        try:
            while True:
                if row + 1 < self._rows:
                    row += 1
                    coord_list.append(row)
                    rf_list.append(game_list[column][row])
                else:
                    break
        except:
            return None
        checked = self.check_list(rf_list, game_list)
        try:
            for num in range(checked):
                coord_num = coord_list[num]
                self.change_piece_color(coord_num, column, game_list)
        finally:
            return checked

    def up_right_find(self, row: int, column: int, game_list: list) -> int:
        'Mutates a list of coordinates in the specified direction: Up Right'
        row_list = []
        col_list = []
        rf_list = []
        try:
            while True:
                if row - 1 >= 0:
                    if column + 1 < self._columns:
                        row += -1
                        column += 1
                        row_list.append(row)
                        col_list.append(column)
                        rf_list.append(game_list[column][row])
                    else:
                        break
                else:
                    break
        except:
            return None
        checked = self.check_list(rf_list, game_list)
        try:
            for num in range(checked):
                row_num = row_list[num]
                col_num = col_list[num]
                self.change_piece_color(row_num, col_num, game_list)
        finally:
            return checked
    
    def down_right_find(self, row: int, column: int, game_list: list) -> int:
        'Mutates a list of coordinates in the specified direction: Down Right'
        row_list = []
        col_list = []
        rf_list = []
        try:
            while True:
                if row + 1 < self._rows:
                    if column + 1 < self._columns:
                        row += 1
                        column += 1
                        row_list.append(row)
                        col_list.append(column)
                        rf_list.append(game_list[column][row])
                    else:
                        break
                else:
                    break
        except:
            return None
        checked = self.check_list(rf_list, game_list)
        try:
            for num in range(checked):
                row_num = row_list[num]
                col_num = col_list[num]
                self.change_piece_color(row_num, col_num, game_list)
        finally:
            return checked

    def down_left_find(self, row: int, column: int, game_list: list) -> int:
        'Mutates a list of coordinates in the specified direction: Down Left'
        row_list = []
        col_list = []
        rf_list = []
        try:
            while True:
                if row + 1 < self._rows:
                    if column - 1 >= 0:
                        row += 1
                        column += -1
                        row_list.append(row)
                        col_list.append(column)
                        rf_list.append(game_list[column][row])
                    else:
                        break
                else:
                    break
        except:
            return None
        checked = self.check_list(rf_list, game_list)
        try:
            for num in range(checked):
                row_num = row_list[num]
                col_num = col_list[num]
                self.change_piece_color(row_num, col_num, game_list)
        finally:
            return checked

    def up_left_find(self, row: int, column: int, game_list: list) -> int:
        'Mutates a list of coordinates in the specified direction: Up Left'
        row_list = []
        col_list = []
        rf_list = []
        try:
            while True:
                if row - 1 >= 0:
                    if column - 1 >= 0:
                        row += -1
                        column += -1
                        row_list.append(row)
                        col_list.append(column)
                        rf_list.append(game_list[column][row])
                    else:
                        break
                else:
                    break
        except:
            return None
        checked = self.check_list(rf_list, game_list)
        try:
            for num in range(checked):
                row_num = row_list[num]
                col_num = col_list[num]
                self.change_piece_color(row_num, col_num, game_list)
        finally:
            return checked     
                        
    def use_find(self, row: int, column: int, game_list: list)-> bool:
        'Uses each -find- to flip all potential flips for all directions'
        try:
            none_list = []
            none_list.append(self.right_find(row, column, game_list))
            none_list.append(self.left_find(row, column, game_list))
            none_list.append(self.down_find(row, column, game_list))
            none_list.append(self.up_find(row, column, game_list))
            none_list.append(self.up_right_find(row, column, game_list))
            none_list.append(self.down_right_find(row, column, game_list))
            none_list.append(self.up_left_find(row, column, game_list))
            none_list.append(self.down_left_find(row, column, game_list))
            for element in none_list:
                if element != None:
                    return True
            raise GameError()
        except:
            return False
        
    def get_turn(self) -> str:
        'Returns str identifying the turn'
        if self._turn == 'B':
            return "B"
        else:
            return "W"
        
    def get_turn_num(self) -> int:
        'Returns BLACK or WHITE identifying the turn'
        if self._turn == 'B':
            return BLACK
        else:
            return WHITE

    def get_opposite_num(self) -> int:
        'Returns BLACK or WHITE of opposite pieces'
        if self._turn == 'B':
            return WHITE
        else:
            return BLACK

    def check_disc_cell(self, row: int, column: int, game_list: list) -> int:
        "Checks if disc cell is full or not"
        value = game_list[column][row]
        return value

    def valid_turn(self, make_list: list, game_list) -> None:
        "Appends valid turn onto the board"
        print('VALID')
        row = make_list[0]
        column = make_list[1]
        game_list[column][row] = self.get_turn_num()

    def new_game(self) -> list:
        'Creates a new board'
        new_list = []
        for column in range(self._columns):
            new_list.append([])
            for rows in range(self._rows):
                new_list[-1].append(NONE)
        four_discs = self._inp[3]
        r_half = int(self._rows/2) - 1
        c_half = int(self._columns/2)- 1
        
        if four_discs == 'B':
            new_list[c_half][r_half] = BLACK
            new_list[c_half+1][r_half] = WHITE
            new_list[c_half][r_half+1] = WHITE
            new_list[c_half+1][r_half+1] = BLACK
        else:
            new_list[c_half][r_half] = WHITE
            new_list[c_half+1][r_half] = BLACK
            new_list[c_half][r_half+1] = BLACK
            new_list[c_half+1][r_half+1] = WHITE
        return new_list

    def change_turn(self) -> None:
        'Change the turn'
        if self._turn == 'B':
            self._turn = 'W'
        else:
            self._turn = 'B'

    def change_piece_color(self, row: int, column: int, game_list: list) -> None:
        'Changes a piece\'s color'
        if game_list[column][row] == BLACK:
            game_list[column][row] = WHITE
        else:
            game_list[column][row] = BLACK
            
    def scoring(self, piece_list: list) -> None:
        'Counts up and returns the winner'
        black_win = piece_list[0]
        white_win = piece_list[1]
        if black_win > white_win and self._mode == '>':
            print('WINNER: B')
        elif black_win > white_win and self._mode == '<':
            print('WINNER: W')
        elif black_win < white_win and self._mode == '>':
            print('WINNER: W')
        elif black_win < white_win and self._mode == '<':
            print('WINNER: B')
        else:
            print('WINNER: NONE')

    def check_board_for_moves(self, game_list: list) -> bool:
        'Returns true if there are still moves on the board'
        move_list = []
        copy_list = []
        for element in game_list:
            spare_list = []
            for obj in element:
                spare_list.append(obj)
            copy_list.append(list(spare_list))
        for column_num in range(len(copy_list)):
            for row_num in range(len(copy_list[column_num])):
                if self.check_disc_cell(row_num, column_num, copy_list) == 0:
                    if self.use_find(row_num, column_num, copy_list) == False:
                        move_list.append(0)
                    else:
                        move_list.append(1)
                else:
                    move_list.append(0)
        for num in move_list:
            if num != 0:
                return True
        return False
