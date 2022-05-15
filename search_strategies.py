from node import Node
from GUI.Graph import Graph
from utils import get_complete_tree, assign_graph_index, remove_duplicates

def tree_search(problem, strategy):
    """
    Function that uses the passed strategy to choose which node to expand
    and expands it
    :param problem
    :param strategy: search strategy to use to choose which node to expand
    :return: None if failure, correct path if success
    """

    fringe = [Node(problem.initial_state, path_cost=1, depth=0, graph_index=0)] # Initialize the fringe
    

    new_graph_test = Graph("Total")
    # --- FINE GRAFICA ---
    
    goal_test = Node(problem.goal_test)
    while True:
        if len(fringe) == 0: # no solution
            return None

        # based on the chosen strategy this chooses the node to expand
        current_node = strategy(fringe, problem)
        
        if current_node.state == goal_test.state: # Solution found
            print("Solution found!")
            result = current_node.correct_path() # Solution

            total_tree = get_complete_tree(current_node)
            #remove_duplicates(total_tree)
            assign_graph_index(total_tree)

            for node in total_tree:

                parent = node.parent
                node_index = node.graph_index


                node_color = "black"
                if node in result:
                    node_color="green"
                    if node.state == goal_test.state:
                        node_color="red"

                new_graph_test.add_node(str(node_index), node.state, color=node_color) 

                if parent:
                    parent_index = parent.graph_index
                    new_graph_test.add_edge(str(parent_index), str(node_index), node.action, color=node_color)

            new_graph_test.graph_viewer()


            return result
        
        fringe.remove(current_node)

        for new_node in current_node.expand(problem):
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

        for node1 in fringe:
            for node2 in fringe2:
                if node1.state == node2.state:
                    curr_node = node1
                    for parent in node2.correct_path()[1:]:
                        curr_node.children.append(parent)
                        parent.parent = curr_node
                        curr_node = parent

                    return curr_node

        fringe.remove(current_node1)
        for new_node in current_node1.expand(problem):
            fringe.append(new_node)

        fringe2.remove(current_node2)
        for new_node in current_node2.expand(problem):
            fringe2.append(new_node)


def DFS(fringe, problem=None):
    return fringe.pop()


def IDS(fringe, problem):
    root = fringe[0]
    depth_limit = 1
    iterator = 0

    while depth_limit < 100:
        while len(fringe) != 0:
            current_node = DFS(fringe)
            # fringe.remove(current_node) # test 
            if current_node.state == problem.goal_test:
                
                return current_node

            if current_node.depth != depth_limit:
                for new_node in current_node.expand(problem):
                    fringe.append(new_node)

                iterator += 1

        depth_limit *= 2
        fringe.append(root)

    return None
