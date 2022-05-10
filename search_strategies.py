from node import Node
from utils import search, get_dict_instance_given_path

def tree_search(problem, strategy):
    """
    Function that uses the passed strategy to choose which node to expand
    and expands it
    :param problem
    :param strategy: search strategy to use to choose which node to expand
    :return: None if failure, correct path if success
    """

    fringe = [Node(problem.initial_state, path_cost=1, depth=0)] # Initialize the fringe
    complete_tree = {Node(problem.initial_state, path_cost=1, depth=0): {}}

    goal_test = Node(problem.goal_test)
    print("GOAL STATE: ")
    print(goal_test.state)

    while True:
        if len(fringe) == 0:
            # no solution has been found
            return None

        # based on the chosen strategy this chooses the node to expand
        current_node = strategy(fringe, problem)
        
        if goal_test.state == current_node.state:
            print("Solution found!")
            # solution found
            print((complete_tree))
            return current_node.correct_path()

        fringe.remove(current_node)

        for new_node in current_node.expand(problem):
            path_to_key = search(complete_tree, current_node)
            dict[path_to_key]
            path_dict_instance = get_dict_instance_given_path(complete_tree, path_to_key)
            path_dict_instance.update = {new_node: {}}
            fringe.append(new_node)


def A_star():
    pass


def BFS(fringe, problem):
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


def BFS_bidirectional(fringe, problem):
    fringe2 = [Node(problem.goal_test, path_cost=1, depth=0)]

    while True:
        if len(fringe) == 0:
            return None

        current_node1 = BFS(fringe, problem)
        current_node2 = BFS(fringe2, problem)

        for node in fringe2:
            if current_node1.state == node.state:
                for parent in node.correct_path():
                    if parent != node:
                        if len(current_node1.children) == 0:
                            parent.parent = current_node1
                        else:
                            parent.parent = current_node1.children[-1]
                        current_node1.children.append(parent)
                return current_node1.children[-1]

        fringe.remove(current_node1)
        for new_node in current_node1.expand(problem):
            fringe.append(new_node)

        fringe2.remove(current_node2)
        for new_node in current_node2.expand(problem):
            fringe2.append(new_node)


def DFS(fringe):
    return fringe.pop()


def IDS(fringe, problem):
    root = fringe[0]
    depth_limit = 1
    iterator = 0

    while depth_limit < 100:
        while len(fringe) != 0:
            current_node = DFS(fringe)

            if current_node.state == problem.goal_test:
                return current_node

            if current_node.depth != depth_limit:
                for new_node in current_node.expand(problem):
                    fringe.append(new_node)

                iterator += 1

        depth_limit *= 2
        fringe.append(root)

    return None
