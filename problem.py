import copy

from utils import find_blank_tile, is_action_allowed


class Problem:
    """
    Data structure identifying the given problem
    """

    def __init__(self, name, initial_state, goal_test, step_cost, expanded_nodes=0):
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
        self.successor_function = self.successor_function_puzzle
        self.step_cost = step_cost
        self.n_row = int(len(initial_state)**0.5)
        self.actions = {
            "left": -1,
            "right": 1,
            "up": -self.n_row,
            "down": self.n_row}
        self.expanded_nodes = expanded_nodes

    def successor_function_puzzle(self, node):
        tile_pos = find_blank_tile(node)
        successors = []
        path_to_root = [node.state for node in node.correct_path()]

        up = (self.moveUp(node.state, tile_pos), 'up')
        down = (self.moveDown(node.state, tile_pos), 'down')
        left = (self.moveLeft(node.state, tile_pos), 'left')
        right = (self.moveRight(node.state, tile_pos), 'right')

        actions = [up, down, left, right]
        for action in actions:
            if action[0] != None:
                if node.parent != None or action[0] not in path_to_root:
                    successors.append(action)

        return successors

    def moveUp(self, node, blank_tile_position):
        new_node = copy.deepcopy(node)

        if is_action_allowed(new_node, "up")[0]:
            swap_tile = blank_tile_position+self.actions['up']
            new_node[blank_tile_position], new_node[swap_tile] = new_node[swap_tile], new_node[blank_tile_position]
            return new_node

    def moveDown(self, node, blank_tile_position):
        new_node = copy.deepcopy(node)

        if is_action_allowed(new_node, "down")[0]:
            swap_tile = blank_tile_position+self.actions['down']
            new_node[blank_tile_position], new_node[swap_tile] = new_node[swap_tile], new_node[blank_tile_position]
            return new_node

    def moveRight(self, node, blank_tile_position):
        new_node = copy.deepcopy(node)

        if is_action_allowed(new_node, "right")[0]:
            swap_tile = blank_tile_position+self.actions['right']
            new_node[blank_tile_position], new_node[swap_tile] = new_node[swap_tile], new_node[blank_tile_position]
            return new_node

    def moveLeft(self, node, blank_tile_position):
        new_node = copy.deepcopy(node)

        if is_action_allowed(new_node, "left")[0]:
            swap_tile = blank_tile_position+self.actions['left']
            new_node[blank_tile_position], new_node[swap_tile] = new_node[swap_tile], new_node[blank_tile_position]
            return new_node
