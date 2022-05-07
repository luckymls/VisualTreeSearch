import copy


class Problem:
    """
    Data structure identifying the given problem
    """

    def __init__(self, name, initial_state, goal_test, step_cost):
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

    def successor_function_8_puzzle(self, node):
        tile_pos = self.find_blank_tile(node)

        print('tile 0 in pos ' + str(tile_pos))

        successors = []

        up = (self.moveUp(node.state, tile_pos), 'up')
        down = (self.moveDown(node.state, tile_pos), 'down')
        left = (self.moveLeft(node.state, tile_pos), 'left')
        right = (self.moveRight(node.state, tile_pos), 'right')

        if up[0] is not None:
            if node.parent is None:
                successors.append(up)
            else:
                if up[0] != node.parent.state:
                    successors.append(up)
        if down[0] is not None:
            if node.parent is None:
                successors.append(down)
            else:
                if down[0] != node.parent.state:
                    successors.append(down)

        if left[0] is not None:
            if node.parent is None:
                successors.append(left)
            else:
                if left[0] != node.parent.state:
                    successors.append(left)
        if right[0] is not None:
            if node.parent is None:
                successors.append(right)
            else:
                if right[0] != node.parent.state:
                    successors.append(right)

        for nodes in successors:
            self.print_puzzle(nodes[0])

        return successors

    def find_blank_tile(self, node):
        for i in range(len(node.state)):
            if node.state[i] == 0:
                return i

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
            new_node[blank_tile_position + 1] = 0 # TODO Ho cambiato da +1 a -1
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
