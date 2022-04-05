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
