import copy, random
from tracemalloc import start


def is_solvable(data):
    """
    param data: 8 puzzle as vector: [1,2,3,4,5,6,7,8,0]


    8 puzzle is solvable if number of inversion is even
    8 puzzle is not solvable if number of inversion is odd

    Inversion is when a pair of tail appear to be in in reverse order as they are in the goal state

    1 2 3
    5 4 6
    8 7 0

    1 2 3 5 4 6 8 7 0

    Here the number of inversion is 2 (5,4) and (8,7)
    puzzle is solvable bc number of inversion is even
    """

    blank_tile = 0 # Blank tile identifier
    n_inversion = 0
    test_data  = copy.deepcopy(data)
    test_data.remove(blank_tile)

    for i in range(len(test_data)):
        for j in range(i+1, len(test_data)):
            if test_data[i] > test_data[j]:
                n_inversion+=1

    return n_inversion % 2 == 0

'''
Return all children of a node
'''
def get_children(node):
    temp = []
    for child in node.children:
        temp.append(child)
        temp += get_children(child)
    return temp

'''
Given a node, returns all the linked nodes
'''
def get_complete_tree(solution_node):
    result = []
    start_node = solution_node.correct_path()[-1]
    result.append(start_node)
    result += get_children(start_node)

    return result

'''
Assign index to each node to later print that
'''
def assign_graph_index(complete_tree):

    index = 0
    for node in complete_tree:
        node.graph_index = index
        index += 1

'''
Assign node action to each node
'''
def assign_node_action(complete_tree):
    
    for node in complete_tree:
        parent = node.parent
        if parent != None:
            start_blank_pos = find_blank_tile(parent)
            end_blank_pos = find_blank_tile(node)
            diff_pos = end_blank_pos-start_blank_pos
            node.action = get_action_label(diff_pos)
        else:
            node.action = None

'''
Given a strategy function it returns the function name
'''
def get_strategy_name(strategy):
    return strategy.__qualname__


'''
Return position of blank tile in puzzle
'''
def find_blank_tile(node):

    return node.state.index(0)


'''
Return action label based on position array difference
'''    
def get_action_label(diff_pos):

    actions = {-1: "left",
                1: "right",
               -3: "up",
                3: "down"}

    return actions[diff_pos]

'''
Generate 8-puzzle game
'''
def generate_puzzle(steps):

    problem = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    actions = {"left": -1,
               "right": 1,
               "up": -3,
               "down": 3}
    for i in range(steps):
        actions_allowed = []
        start_tile = problem.index(0)

        right_left = start_tile%3
        if right_left == 0:
            actions_allowed.append(actions["right"])
        if right_left == 1:
            actions_allowed.append(actions["right"])
            actions_allowed.append(actions["left"])
        if right_left == 2:
            actions_allowed.append(actions["left"])

        up_down = int(start_tile/3)
        if up_down == 0:
            actions_allowed.append(actions["down"])
        if up_down == 1:
            actions_allowed.append(actions["down"])
            actions_allowed.append(actions["up"])
        if up_down == 2:
            actions_allowed.append(actions["up"])

        if len(actions_allowed) > 0:
            random.shuffle(actions_allowed)
            swap_tile = start_tile+actions_allowed[0]
            # Swap tiles
            problem[start_tile], problem[swap_tile] = problem[swap_tile], problem[start_tile]
            
    return problem


'''
Generate random color for plot lines
'''
def generate_random_plot_color():
    
    r = random.random()
    b = random.random()
    g = random.random()
    color = (r, g, b)
    return color