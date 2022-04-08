class Frame:


    def __init__(self, data):
        '''
        Create data frame structure for graph representation
        :param data: array with data i.e. [[1,2,3],[4,5,6],[7,8,0]]      -> 1 2 3
                                                                            4 5 6
                                                                            7 8                                                                        
        '''

        self.data = data
        self.l_row = len(self.data)
        self.l_col = len(self.data[0])

    
    def format_frame(self):
        """
        Create frame readable from graphviz for data graph representation
        [[1,2,3],[4,5,6],[7,8,0]] becomes {1|4|7}|{2|5|8}|{3|6| }
        becomes
        1 2 3
        4 5 6
        7 8  

        """
        frame=""
        for i in range(self.l_col):
            frame += "{" # Column frame begins
            for k in range(self.l_row):
                value = self.data[k][i]
                if value == 0:
                    value = " " # Blank cell
                frame += str(value) # Cell data
                frame += "|" # Cell separator

            frame = frame.rstrip("|")
            frame += "}" # Column frame ends
            frame += "|" # Row separator
        frame = frame.rstrip("|") 
        return frame

    
            





    