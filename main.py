from problem import Problem
from utils import is_solvable, generate_puzzle
from search_strategies import tree_search, BFS, IDS, BFS_bidirectional
import matplotlib.pyplot as plt
from utils import get_strategy_name, generate_random_plot_color

if __name__ == "__main__":
    n_steps = 8
    initial_state = generate_puzzle(n_steps)
    goal_state = [1,2,3,4,5,6,7,8,0]

    # --- BUGS KNOWN
    # initial_state = [1, 2, 3, 4, 5, 6, 7, 0, 8] # Bug in BFS bi
    # initial_state = [1, 2, 3, 0, 5, 6, 4, 7, 8] # Bug in BFS bi

    # ---

    


    if is_solvable(initial_state):

        problem = Problem('8tile', initial_state, goal_state, 1) 

        algorithms = [IDS, BFS, BFS_bidirectional]
        plt.figure(num='Compute time')
        for strategy in algorithms:
            strategy_name = get_strategy_name(strategy)
            print("Applying %s algorithm" % strategy_name)
            result, compute_time = tree_search(problem, strategy)
            print("%s time: %s ns\n" % (strategy_name, compute_time))
            plt.axhline(y=compute_time, label=strategy_name, color=generate_random_plot_color())
        
        plt.ylabel('Compute Time (ns)')
        plt.legend(bbox_to_anchor = (1.0, 1), loc = 'upper center')
        plt.show()
        '''   
        choice = input("Algorithm\n[0] IDS\n[1] BFS\n[2] BFS bidirectional\n[3] A*\n> ")
        while choice not in ['0', '1', '2', '3']:
            choice = input("Algorithm\n[0] IDS\n[1] BFS\n[2] BFS bidirectional\n[3] A*\n> ")
        choice = int(choice)
        if choice == 0:
            result, compute_time = tree_search(problem, IDS)
            
        if choice == 1:
            result, compute_time = tree_search(problem, BFS)
        if choice == 2:
            result, compute_time = tree_search(problem, BFS_bidirectional)
        if choice == 3:
            print("Algoritmo A* non implementato.")
            result = None
            # result = tree_search(problem, A)
        '''

    else:
        print("Not solvable problem, try with different one")
