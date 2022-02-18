from xml.etree import ElementInclude
from Cell import Cell


class Map:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._cells = [[Cell() for x in range(cols)] for y in range(rows)]
    
    #TODO: rows getter
    @property
    def rows(self):
        return self._rows
    
    #TODO: cols getter
    @property
    def cols(self):
        return self._cols
    
    def get_cell(self, row, col):
        #TODO:
        if(row < 0 or row >= self.rows or col < 0 or col >= self.cols):
            print("\033[1;31;46mNext move is out of boundary!\033[0;0m")
            return None
        else:
            # return a cell
            return self._cells[row][col]
        # END TODO

    def build_cell(self, row, col, cell):
        #TODO:
        if(row < 0 or row >= self.rows or col < 0 or col >= self.cols):
            print("\033[1;31;46mThe position (%d, %d) is out of boundary!\033[0;0m" %(row, col))
            return False
        else:
            # return a cell
            self._cells[row][col] = cell
            return True
        # END TODO

    def get_neighbours(self, row, col):
        return_cells = []
        # TODO:
        for i in range(max(0, row - 1), min(row + 1, self.rows - 1) + 1):
            for j in range(max(0, col - 1), min(col + 1, self.cols - 1) + 1):
                return_cells.append(self._cells[i][j])
        
        return return_cells
        # END TODO
        

    def display(self):
        # TODO:
        col_index = "   "
        for i in range(self.cols):
            col_index += str(i) + "     "
        print(col_index)
        for i in range(self.rows):
            print(str(i) + " ", end = "")
            for j in range(self.cols):
                self._cells[i][j].display()
            print("\n")

        # END TODO
