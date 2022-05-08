import node
from node import Node
from problem import Problem
from search_strategies import tree_search, BFS, IDS
from utils import is_solvable, get_strategy_name
from GUI.Graph import Graph

if __name__ == '__main__':
    initial_state = [0, 1, 3, 4, 2, 5, 7, 8, 6]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    
    if is_solvable(initial_state):
        print("Test stato iniziale ")
        print(initial_state)
        print("Puzzle is solvable")
        result_graph = Graph("%s algorithm" % get_strategy_name(IDS))
        step_graph = Graph("%s step graph" % get_strategy_name(IDS))

        problem = Problem('8tile', initial_state, goal_state, 1, step_graph)
        #result = tree_search(problem, BFS)
        result = tree_search(problem, IDS)

        if result is None:
            print('rip')
        else:
            node.print_path(result)
            # Temporaneo
            indice=0
            for node in reversed(result):
                
                if node.action != None:
                    
                    print(node.action)
                    print("|")
                    print("V")
                if node.state != None:
                    result_graph.add_node(str(indice), node.state)
                    if indice > 0:
                        result_graph.add_edge(str(indice-1), str(indice), node.action)
                    print(node.state)
                indice +=1
            result_graph.graph_viewer()
            step_graph.graph_viewer()
    else:
        print("Not solvable problem, try with different one")
