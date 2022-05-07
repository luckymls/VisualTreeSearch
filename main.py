import node
from node import Node
from problem import Problem
from search_strategies import tree_search, BFS, IDS
from utils import is_solvable

if __name__ == '__main__':
    initial_state = [1, 2, 3, 4, 5, 0, 7, 8, 6]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    if is_solvable(initial_state):
        print("Test stato iniziale ")
        print(initial_state)
        print("Puzzle is solvable")
        problem = Problem('8tile', initial_state, goal_state, 1)

        #result = tree_search(problem, BFS)
        result = tree_search(problem, IDS)

        if result is None:
            print('rip')
        else:
            node.print_path(result)
    else:
        print("Not solvable problem, try with different one")
