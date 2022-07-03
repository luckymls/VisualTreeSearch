import matplotlib.pyplot as plt

from problem import Problem
from search_strategies import BFS, IDS, A_star, Optimized_A_star, BFS_bidirectional, tree_search
from utils import (generate_puzzle, generate_random_plot_color,
                   get_strategy_name, is_solvable)


if __name__ == "__main__":
    n_steps = 10
    size_problem = 9  # (4,9,16,25,36,49,64,...,n^2)

    goal_state = [x for x in range(1, size_problem)]
    goal_state.append(0)
    initial_state = generate_puzzle(n_steps, goal_state)
    
    if is_solvable(initial_state):

        # initializing the problem:
        # puzzle game with the step cost of 1
        problem = Problem(initial_state, goal_state, 1)

        algorithms = [IDS, BFS, BFS_bidirectional, A_star, Optimized_A_star]
        fig, ax = plt.subplots(num='Compute time')

        for strategy in algorithms:
            strategy_name = get_strategy_name(strategy)
            print("\n%s algorithm" % strategy_name)
            result, compute_time = tree_search(problem, strategy)
            
            print("- Time: %s ms" % compute_time)
            print("- Expanded nodes: %s" % problem.expanded_nodes)

            ax.bar(problem.expanded_nodes, compute_time, label=strategy_name, width=1, color=generate_random_plot_color(), linewidth=0.7)

        plt.xlabel('Expanded nodes')
        plt.ylabel('Compute Time (ms)')
        plt.legend(bbox_to_anchor=(1.0, 1), loc='upper center')
        
        plt.show()
    else:
        print("Not solvable problem, try with different one")
