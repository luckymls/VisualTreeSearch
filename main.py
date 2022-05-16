from problem import Problem
from utils import is_solvable, generate_puzzle
from search_strategies import tree_search, BFS, IDS, BFS_bidirectional, A_star
import matplotlib.pyplot as plt
from utils import get_strategy_name, generate_random_plot_color

if __name__ == "__main__":
    n_steps = 10
    initial_state = generate_puzzle(n_steps)
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    if is_solvable(initial_state):

        # initializing the problem:
        # in this case we have an 8 tile puzzle game with the step cost of 1
        problem = Problem('8tile', initial_state, goal_state, 1) 

        algorithms = [IDS, BFS, BFS_bidirectional, A_star]
        plt.figure(num='Compute time')
        for strategy in algorithms:
            strategy_name = get_strategy_name(strategy)
            print("Applying %s algorithm" % strategy_name)
            result, compute_time = tree_search(problem, strategy)
            print("%s time: %s ns\n" % (strategy_name, compute_time))
            plt.axhline(y=compute_time, label=strategy_name, color=generate_random_plot_color())
        
        plt.ylabel('Compute Time (ns)')
        plt.legend(bbox_to_anchor=(1.0, 1), loc='upper center')
        plt.show()
    else:
        print("Not solvable problem, try with different one")
