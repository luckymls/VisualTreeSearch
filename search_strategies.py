from node import Node
from utils import search, get_dict_instance_given_path
from GUI.Graph import Graph

def tree_search(problem, strategy):
    """
    Function that uses the passed strategy to choose which node to expand
    and expands it
    :param problem
    :param strategy: search strategy to use to choose which node to expand
    :return: None if failure, correct path if success
    """

    fringe = [Node(problem.initial_state, path_cost=1, depth=0, graph_index=0)] # Initialize the fringe
    to_visit = [fringe[0]]
    visited = [fringe[0]]
    complete_graph = Graph("Graph")
    goal_test = Node(problem.goal_test)

    while True:
        if len(fringe) == 0: # no solution
            return None

        # based on the chosen strategy this chooses the node to expand
        current_node = strategy(fringe, problem)
        
        if current_node.state == goal_test.state: # Solution found
            print("Solution found!")
            result = current_node.correct_path() # Solution
            
            indice = 0
            complete_graph.add_node(str(visited[0].graph_index), visited[0].state, color="green")
            
            while len(to_visit) > 0:
                for node in to_visit:
                    parent_index = node.graph_index
                    for child in node.children:
                        to_visit.append(child)
                        visited.append(child)
                        indice+=1
                        child.graph_index = indice
                        node_color="black" 
                        if child in result:
                            node_color="green"
                            if child.state == goal_test.state:
                                node_color="red"

                        
                        
                        complete_graph.add_node(str(child.graph_index), child.state, color=node_color)
                        complete_graph.add_edge(str(parent_index), str(child.graph_index), child.action, color=node_color)
                    to_visit.remove(node)
            complete_graph.graph_viewer()

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


def DFS(fringe, problem=None):
    return fringe.pop()
    return fringe[-1] # TODO Prima c'era fringe.pop(), facendo così veniva restituito l'ultimo elemento della fringe MA veniva anche rimosso (può creare problemi?)


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
