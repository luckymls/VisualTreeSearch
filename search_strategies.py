import time

import numpy as np

from GUI.Graph import Graph
from node import Node
from utils import (assign_graph_index, assign_node_action, get_complete_tree,
                   get_strategy_name)


def tree_search(problem, strategy):
    """
    Function that uses the passed strategy to choose which node to expand
    and expands it
    :param problem
    :param strategy: search strategy to use to choose which node to expand
    :return: None if failure, correct path if success
    """
    problem.expanded_nodes = 0
    fringe = [Node(problem.initial_state, path_cost=1, depth=0,
                   graph_index=0)]  # Initialize the fringe

    strategy_name = get_strategy_name(strategy)
    result_graph = Graph("%s Graph Result" % strategy_name)
    # --- FINE GRAFICA ---

    goal_test = Node(problem.goal_test)
    end = 0

    while True:
        if len(fringe) == 0:  # no solution
            return None

        start = time.time_ns()
        current_node = strategy(fringe, problem)
        end += time.time_ns()-start

        # based on the chosen strategy this chooses the node to expand
        if current_node.state == goal_test.state:  # Solution found
            result = current_node.correct_path()  # Solution

            total_tree = get_complete_tree(current_node)
            assign_graph_index(total_tree)
            assign_node_action(total_tree)

            for node in total_tree:
                parent = node.parent
                node_index = node.graph_index
                node_color = "black"

                if node in result:
                    node_color = "green"
                    if node.state == goal_test.state:
                        node_color = "red"

                result_graph.add_node(
                    str(node_index), node.state, color=node_color)

                if parent:
                    parent_index = parent.graph_index
                    result_graph.add_edge(str(parent_index), str(
                        node_index), node.action, color=node_color)

            result_graph.graph_viewer()

            compute_time = end  # *10 ** -9
            return [result, compute_time]

        fringe.remove(current_node)
        for new_node in current_node.expand(problem):
            fringe.append(new_node)


def A_star(fringe, problem):
    """
    Strategy that uses the evaluation function to choose the node to expand.
    The evaluation function returns the sum of the path cost from the root to the current node and the
    estimation of the path cost from the current node to the solution node.
    The node chosen base on minimum value of the evaluation function: the node in the fringe with the min
    evaluation function value is chosen to be expanded.
    """
    # initializing the node to expand as the first node in the fringe
    node_to_expand = fringe[0]
    min_path_cost = f(node_to_expand, problem.goal_test)

    # check for each node in the fringe which one has the minimum f-value
    for node in fringe:
        curr_node_path_cost = f(node, problem.goal_test)
        if curr_node_path_cost < min_path_cost:
            min_path_cost = curr_node_path_cost
            node_to_expand = node

    # return the node with the min f-value
    return node_to_expand


def f(node, goal_state):
    """
    Node evaluation function for the A* algorithm.
    It sums up the g(n) and h(n) values
    """
    
    node.g = g(node)
    node.h = h(node, goal_state)
    return g(node) + h(node, goal_state)


def g(node):
    """
    Function for the A* algorithm that returns the
    path cost from the root to the current node.
    """
    return node.path_cost


def h(node, goal_state):
    """
    Function for the A* algorithm that returns the estimation of the
    path cost from the current node to the solution.
    """
    # returns the number of misplaced tiles between the current node's state and the goal state
    return sum((np.array(node.state) != np.array(goal_state)))


def BFS(fringe, problem):
    """
    Strategy that chooses the shallowest node in the fringe for the expansion
    The function cycles through the fringe to check which node is the one with
    the higher depth (the one with the minimum depth value) and returns it
    :param fringe: list of nodes to expand
    :param problem: current problem
    :return: shallowest node
    """
    min_depth = fringe[0]

    for node in fringe:
        if node.depth < min_depth.depth:
            min_depth = node
    return min_depth


def BFS_bidirectional(fringe, problem):
    """
    Strategy that creates 2 trees by expanding the initial state and the goal state at the same time.
    At every step the algorithm checks if there are nodes in common in the fringes. If this is true the
    2 trees get merged and the solution is found.
    """

    # initializing the second fringe containing the nodes to expand from the second tree
    fringe2 = [Node(problem.goal_test, path_cost=1, depth=0)]

    while True:

        # if the fringe is empty no solution has been found
        if len(fringe) == 0:
            return None

        # checks if there are nodes in common between the fringes
        for node1 in fringe:
            for node2 in fringe2:

                # if a common node is found the merging begins
                if node1.state == node2.state:
                    curr_node = node1
                    for parent in node2.correct_path()[1:]:
                        parent.children = []
                        parent.action = curr_node.action
                        curr_node.children.append(parent)
                        parent.parent = curr_node
                        curr_node = parent

                    # returns the solution node so that the tree_search algorithm gets the solution
                    return curr_node

        # expanding both the trees with BFS algorithm
        current_node1 = BFS(fringe, problem)
        current_node2 = BFS(fringe2, problem)

        # refreshing the fringe of the first tree
        fringe.remove(current_node1)
        for new_node in current_node1.expand(problem):
            fringe.append(new_node)

        # refreshing the fringe of the second tree: this is different, because we don't remove the already
        # expanded nodes, instead we increase their depth so that they don't get expanded endlessly.
        # this allows us to get a better solution and avoid duplicated states in the path. it also removes a
        # problem where a solvable puzzle with one step would get solved with more than one step and
        # also get duplicated nodes
        current_node2.depth += 10000
        for new_node in current_node2.expand(problem):
            fringe2.append(new_node)


def DFS(fringe, problem=None):
    """
    Strategy that chooses the deepest node to expand
    """
    return fringe.pop()


def IDS(fringe, problem):
    """
    Strategy based on the DFS algorithm:
    A depth limit is set, so that the tree won't get any deeper than the limit. Everytime the limit is reached,
    without finding a solution, it gets increased, with a maximum of 100
    """
    # saving the root
    root = fringe[0]

    # initializing the depth limit to 0
    depth_limit = 1

    while depth_limit < 100:
        while len(fringe) != 0:

            # choosing the node to expand with DFS algorithm
            current_node = DFS(fringe)

            # check if the chosen node is the goal state
            if current_node.state == problem.goal_test:
                return current_node

            # check the depth of the node and the limit: if the limit is reached the node doesn't get expanded
            if current_node.depth < depth_limit-1:
                for new_node in current_node.expand(problem):
                    if new_node is not None:
                        fringe.append(new_node)

        # increasing the depth limit
        depth_limit += 1

        # restarting the algorithm
        fringe.append(root)

    # if the algorithm ends up here it means that no solution has been found
    return None
