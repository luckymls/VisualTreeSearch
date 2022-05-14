from problem import Problem
from GUI.Graph import Graph
from utils import is_solvable, get_strategy_name
from search_strategies import tree_search, BFS, IDS, BFS_bidirectional, DFS


if __name__ == '__main__':

    initial_state = [1,2,3,4,8,5,7,0,6]
    goal_state = [1,2,3,4,5,6,7,8,0]
    
    
    if is_solvable(initial_state):
        
        print("Puzzle is solvable")

        result_graph = Graph("%s solution" % get_strategy_name(IDS))
        step_graph = Graph("%s step graph" % get_strategy_name(IDS))

        problem = Problem('8tile', initial_state, goal_state, 1, step_graph) 

        choice = input("Algorithm\n[0] IDS\n[1] BFS\n[2] BFS bidirectional\n[3] DFS\n> ")
        while choice not in ['0','1','2','3']:
            choice = input("Algorithm\n[0] IDS\n[1] BFS\n[2] BFS bidirectional\n[3] DFS\n> ")
        choice = int(choice)
        if choice == 0:
            result = tree_search(problem, IDS)
        if choice == 1:
            result = tree_search(problem, BFS)
        if choice == 2:
            result = tree_search(problem, BFS_bidirectional)
        if choice == 3:
            print("Da implementare.")
            result=None
            #result = tree_search(problem, DFS)



        if not result:
            print("No solution found")
        else:

            # Temporaneo, crea il pdf del vettore dei risultati
            index=0
            for node in reversed(result):
                
                if node.state != None:
                    result_graph.add_node(str(index), node.state)
                    if index > 0:
                        result_graph.add_edge(str(index-1), str(index), node.action)
                index +=1
            result_graph.graph_viewer()
            # step_graph.graph_viewer()
            
    else:
        print("Not solvable problem, try with different one")
