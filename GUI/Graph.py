from time import monotonic
import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

class Graph:

    def __init__(self, graph_name):
        """
        Create data frame structure for graph representation
        :param graph_name
        """
        self.graph = graphviz.Digraph(graph_name, node_attr={'shape': 'record'})

    def node_struct(self, data, l_row, l_col):
        """
        Create node readable from graphviz for data graph representation given an array
        [[1,2,3],[4,5,6],[7,8,0]] becomes {1|4|7}|{2|5|8}|{3|6| }
        becomes
        1 2 3
        4 5 6
        7 8  

        NOTE: 0 is used to represent blank cell
        """
        frame=""
        for i in range(l_col):
            frame += "{" # Column frame begins
            for k in range(l_row):
                value = data[k][i]
                if value == 0:
                    value = " " # Blank cell
                frame += str(value) # Cell data
                frame += "|" # Cell separator

            frame = frame.rstrip("|")
            frame += "}" # Column frame ends
            frame += "|" # Row separator
        frame = frame.rstrip("|") 
        return frame

    def mono2multi_array(self, data):
        multi = []
        numbers_per_game_row = int(len(data)**0.5) # Radice della lunghezza del vettore per capire numero di colonne e righe (il gioco deve essere un quadrato)

        for i in range(numbers_per_game_row):
            start = numbers_per_game_row*i
            end = numbers_per_game_row*(i+1)
            multi.append(data[start:end])
        return multi



    def add_node(self, name, data, color=None):
        """
        This function allow user to add a node to the graph
        name: node name identifier
        data: array with data i.e. [[1,2,3],[4,5,6],[7,8,0]]      -> 1 2 3
                                                                     4 5 6
                                                                     7 8 
        """
        data = self.mono2multi_array(data)
        l_row = len(data)
        l_col = len(data[0])
        node_struct = self.node_struct(data, l_row, l_col)
        self.graph.node(name, node_struct, color=color)


    def add_edge(self, from_node, to_node, label=None, color=None):
        """
        This function allow user to add an edge between two nodes
        from_node: starting node name identifier
        to_node: goal node name identifier
        label: [OPTIONAL] edge name
        """
        self.graph.edge(from_node, to_node, label, color=color)
    


    def graph_viewer(self):
        """
        Allow user to visualize graph
        """
        self.graph.view()







    