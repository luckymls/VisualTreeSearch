import search_strategies
from node import Node
from problem import Problem
from search_strategies import tree_search, BFS

if __name__ == '__main__':
    initial_state = [0, 3, 4, 1, 2, 6, 7, 5, 8]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    problem = Problem('8tile', initial_state, goal_state, 1)

    result = tree_search(problem, BFS)

    if result is None:
        print('rip')
    else:
        print(result)
