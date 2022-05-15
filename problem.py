import copy
from utils import find_blank_tile

class Problem:
    """
    Data structure identifying the given problem
    """

    def __init__(self, name, initial_state, goal_test, step_cost, graph):
        """
        Function to initialize the problem
        :param initial_state: initial state of the problem (can be randomized)
        :param goal_test: goal state to reach
        :param successor_function: function that decides which node to expand next
        :param step_cost: cost of the action from a node to another
        """
        self.name = name
        self.initial_state = initial_state
        self.goal_test = goal_test
        self.successor_function = self.successor_function_8_puzzle
        self.step_cost = step_cost
        self.graph = graph
        self.graph_iter = 0

    def successor_function_8_puzzle(self, node, verbose=True):
        tile_pos = find_blank_tile(node)
        successors = []
        path_to_root = [node.state for node in node.correct_path()]

        up = (self.moveUp(node.state, tile_pos), 'up')
        down = (self.moveDown(node.state, tile_pos), 'down')
        left = (self.moveLeft(node.state, tile_pos), 'left')
        right = (self.moveRight(node.state, tile_pos), 'right')

        if up[0] is not None:
            if node.parent is None:
                successors.append(up)
            else:
                if not (up[0] in path_to_root):
                    successors.append(up)

        if down[0] is not None:
            if node.parent is None:
                successors.append(down)
            else:
                if not (down[0] in path_to_root):
                    successors.append(down)

        if left[0] is not None:
            if node.parent is None:
                successors.append(left)
            else:
                if not (left[0] in path_to_root):
                    successors.append(left)
        if right[0] is not None:
            if node.parent is None:
                successors.append(right)
            else:
                if not (right[0] in path_to_root):
                    successors.append(right)


        for nodes in successors:
            if verbose:
                self.print_puzzle(nodes[0])

        return successors


    def moveUp(self, node, blank_tile_position):
        new_node = copy.deepcopy(node)

        if blank_tile_position >= 3:
            new_node[blank_tile_position - 3] = 0
            new_node[blank_tile_position] = node[blank_tile_position - 3]
            return new_node

    def moveDown(self, node, blank_tile_position):
        new_node = copy.deepcopy(node)

        if blank_tile_position < 6:
            new_node[blank_tile_position + 3] = 0
            new_node[blank_tile_position] = node[blank_tile_position + 3]
            return new_node

    def moveRight(self, node, blank_tile_position):
        new_node = copy.deepcopy(node)

        if blank_tile_position != 2 and blank_tile_position != 5 and blank_tile_position != 8:
            new_node[blank_tile_position + 1] = 0
            new_node[blank_tile_position] = node[blank_tile_position + 1] 
            return new_node

    def moveLeft(self, node, blank_tile_position):
        new_node = copy.deepcopy(node)

        if blank_tile_position != 0 and blank_tile_position != 3 and blank_tile_position != 6:
            new_node[blank_tile_position - 1] = 0 
            new_node[blank_tile_position] = node[blank_tile_position -1]
            return new_node

    def print_puzzle(self, node):
        print('- - - | - - - ')
        print('- - - V - - - ')
        print(node[:3])
        print(node[3:6])
        print(node[6:9])
        
        self.graph.add_node(str(self.graph_iter), node)
        if self.graph_iter > 0:
            
            self.graph.add_edge(str(self.graph_iter-1), str(self.graph_iter))
        self.graph_iter+=1