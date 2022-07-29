import matplotlib.pyplot as plt
import math
from numpy import size
from problem import Problem
from search_strategies import BFS, IDS, A_star, Optimized_A_star, BFS_bidirectional, tree_search
from utils import (generate_puzzle, generate_random_plot_color,
                   get_strategy_name, is_solvable)


class Main:


    algorithms = [IDS, BFS, BFS_bidirectional, A_star, Optimized_A_star]

    def __init__(self, size_problem=9, n_steps=10, no_graph=False, no_diagram_tree=False, verbose=False):
        self.size_problem = size_problem # (4,9,16,25,36,49,64,...,n^2)
        self.n_steps = n_steps
        self.no_graph=no_graph
        self.verbose=verbose
        self.no_diagram_tree=no_diagram_tree 
        self.initialize()
 

    def set_new(self, size_problem=9, n_steps=10):
        self.size_problem=size_problem
        self.n_steps = n_steps
        self.initialize()


    def initialize(self):
        self.goal_state = [x for x in range(1, self.size_problem)]
        self.goal_state.append(0)
        self.initial_state = generate_puzzle(self.n_steps, self.goal_state)

    def solve(self):

        if self.no_graph == False:
            fig, ax = plt.subplots(num='Compute time')
        result_data = {}
        if is_solvable(self.initial_state):

            # initializing the problem:
            # puzzle game with the step cost of 1
            step_cost = 1
            problem = Problem(self.initial_state, self.goal_state, step_cost)

            
            for strategy in Main.algorithms:
                strategy_name = get_strategy_name(strategy)
                if self.verbose:
                    print("\n%s algorithm" % strategy_name)
                result, compute_time = tree_search(problem, strategy, self.no_diagram_tree)
                result_data[strategy_name] = {'time': math.floor(compute_time), 'exp_nodes': problem.expanded_nodes}
                if self.verbose:
                    print("- Time: %s ms" % compute_time)
                    print("- Expanded nodes: %s" % problem.expanded_nodes)

                if self.no_graph == False:
                    ax.bar(problem.expanded_nodes, compute_time, label=strategy_name, width=1, color=generate_random_plot_color(), linewidth=0.7)
            
            if self.no_graph == False:
                plt.xlabel('Expanded nodes')
                plt.ylabel('Compute Time (ms)')
                plt.legend(bbox_to_anchor=(1.0, 1), loc='upper center')
                
                plt.show()
        else:
            print("Not solvable problem, try with different one")
        
        return result_data
                
        
