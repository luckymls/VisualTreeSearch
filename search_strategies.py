from node import Node


def tree_search(problem, strategy):
    """
    Function that uses the passed strategy to choose which node to expand
    and expands it
    :param problem
    :param strategy: search strategy to use to choose which node to expand
    :return: None if failure, correct path if success
    """

    fringe = [Node(problem.initial_state, path_cost=1, depth=0)]

    goal_test = Node(problem.goal_test)
    print("GOAL STATE: ")
    print(goal_test.state)

    while True:
        print("FRINGE: ")
        for n in fringe:
            print(n.state)
        print("FRINGE LENGTH: " + str(len(fringe)))

        if len(fringe) == 0:
            # no solution has been found
            return None

        # based on the chosen strategy this chooses the node to expand
        current_node = strategy(fringe)

        if goal_test.state == current_node.state:
            print("Solution found!")
            # solution found
            return current_node.correct_path()

        fringe.remove(current_node)
        for new_node in current_node.expand(problem):
            fringe.append(new_node)


def A_star():
    pass


def BFS(fringe):
    """
    Strategy that choses the shollowest node in the fringe for the expansion
    The function cycles through the fringe to check which node is the one with
    the higher depth (the one with the minimum depth value) and returns it
    :param fringe: list of nodes to expand
    :return: shallowest node
    """

    min_depth = fringe[0]

    for node in fringe:
        if node.depth < min_depth.depth:
            min_depth = node
    return min_depth


def BFS_bidirectional():
    pass


def IDS():
    pass