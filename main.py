import matplotlib.pyplot as plt

from problem import Problem
from search_strategies import BFS, IDS, A_star, BFS_bidirectional, tree_search
from utils import (generate_puzzle, generate_random_plot_color,
                   get_strategy_name, is_solvable)

if __name__ == "__main__":
    n_steps = 5
    size_problem = 9 # (4,9,16,25,36,49,64,...,n^2)

    goal_state = [x for x in range(1, size_problem)]
    goal_state.append(0)
    initial_state = generate_puzzle(n_steps, goal_state)

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
            plt.axhline(y=compute_time, label=strategy_name,
                        color=generate_random_plot_color())

        plt.ylabel('Compute Time (ns)')
        plt.legend(bbox_to_anchor=(1.0, 1), loc='upper center')
        # plt.show()
    else:
        print("Not solvable problem, try with different one")
