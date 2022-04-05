import copy


class Problem:
    """
    Data structure identifying the given problem
    """

    def __init__(self, name, initial_state, goal_test, successor_function,  step_cost):
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
        self.successor_function = successor_function
        self.step_cost = step_cost

    def successor_function_8_puzzle(self, node):
        pass

    def find_blank_tile(self, node):
        for i in range(9):
            if node.state[i] == 0:
                return i

    def moveUp(self, node, blank_tile_position):
        new_node = copy.deepcopy(node)

        if blank_tile_position >= 3:
            new_node.state[blank_tile_position - 3] = 0
            new_node.state[blank_tile_position] = node.state[blank_tile_position - 3]

        return new_node

    def moveDown(self, node, blank_tile_position):
        new_node = copy.deepcopy(node)

        if blank_tile_position < 6:
            new_node.state[blank_tile_position + 3] = 0
            new_node.state[blank_tile_position] = node.state[blank_tile_position + 3]

        return new_node

    def moveRight(self, node, blank_tile_position):
        new_node = copy.deepcopy(node)

        if blank_tile_position != 2 and blank_tile_position != 5 and blank_tile_position != 8:
            new_node.state[blank_tile_position + 1] = 0
            new_node.state[blank_tile_position] = node.state[blank_tile_position + 1]

        return new_node

    def moveLeft(self, node, blank_tile_position):
        new_node = copy.deepcopy(node)

        if blank_tile_position != 0 and blank_tile_position != 3 and blank_tile_position != 6:
            new_node.state[blank_tile_position + 1] = 0
            new_node.state[blank_tile_position] = node.state[blank_tile_position + 1]

        return new_node

    def print_puzzle(self, node):
        print('- - - - - - - ')
        print(node.state[:3])
        print(node.state[3:6])
        print(node.state[6:9])
