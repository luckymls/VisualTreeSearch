class Frame:


    def __init__(self, n_row, n_col, data):
        '''
        Create data frame structure for graph representation
        :param n_row: number of row
        :param n_col: number of col
        :param data: array with data i.e. [[1,2,3],[4,5,6],[7,8,0]]      -> 1 2 3
                                                                            4 5 6
                                                                            7 8                                                                        
        '''

        self.n_row = n_row
        self.n_col = n_col
        self.data = data

    
    def format_frame(self):
        frame=""
        for row in self.data:
            frame += "{" # Column frame begins
            for value in row:
                if value == 0:
                    value = " " # Blank cell
                frame += value # Cell data
                frame += "|" # Cell separator

            frame = frame.rstrip("|")
            frame += "}" # Column frame ends
            frame += "|" # Row separator
        frame = frame.rstrip("|") 
        return frame

            





    