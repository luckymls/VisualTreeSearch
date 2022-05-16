from argparse import Action
import copy, random


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
    
    if int(len(data)**0.5) != len(data)**0.5: # If problem is not a square
        return False

    blank_tile = 0 # Blank tile identifier
    n_inversion = 0
    test_data  = copy.deepcopy(data)
    #test_data.remove(blank_tile) TEST
    n_row = int(len(data)**0.5)

    for i in range(len(test_data)):
        for j in range(i+1, len(test_data)):
            if test_data[i] > test_data[j] and test_data[i] != blank_tile and test_data[j] != blank_tile:
                n_inversion+=1
    
    if n_row % 2 == 0: # If problem has even cells number
        blank_tile_pos_from_bottom = n_row-(int(data.index(blank_tile)/n_row)) # Return blank tile position counting from bottom
        print(blank_tile_pos_from_bottom, n_inversion)
        if blank_tile_pos_from_bottom % 2 == 0 and n_inversion % 2 == 1:
            return True
        if blank_tile_pos_from_bottom % 2 == 1 and n_inversion % 2 == 0:
            return True
        return False

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
        n_row = int(len(node.state)**0.5)
        parent = node.parent
        if parent != None:
            start_blank_pos = find_blank_tile(parent)
            end_blank_pos = find_blank_tile(node)
            diff_pos = end_blank_pos-start_blank_pos
            node.action = get_action_label(diff_pos, n_row)
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
def get_action_label(diff_pos, n_row):

    actions = {-1: "left",
                1: "right",
               -n_row: "up",
                n_row: "down"}

    return actions[diff_pos]



def is_action_allowed(state, action):
    
    
    start_tile = state.index(0)
    n_row = int(len(state)**0.5)
    actions = {"left": -1,
               "right": 1,
               "up": -n_row,
               "down": n_row}

    actions_allowed = []

    right_left = start_tile%n_row
    if right_left == 0:
        actions_allowed.append("right")
    if right_left > 0 and right_left < (n_row-1):
        actions_allowed.append("right")
        actions_allowed.append("left")
    if right_left == (n_row-1):
        actions_allowed.append("left")

    up_down = int(start_tile/n_row)
    if up_down == 0:
        actions_allowed.append("down")
    if up_down > 0 and up_down < (n_row-1):
        actions_allowed.append("down")
        actions_allowed.append("up")
    if up_down == (n_row-1):
        actions_allowed.append("up")
    
    return (action in actions_allowed, actions[action])
    
'''
Generate 8-puzzle game
'''
def generate_puzzle(steps, initial_state):

    n_row = int(len(initial_state)**0.5)
    problem = copy.deepcopy(initial_state)
    actions = {"left": -1,
               "right": 1,
               "up": -n_row,
               "down": n_row}

    forbidden_action = None
    for i in range(steps):
        actions_allowed = []
        start_tile = problem.index(0)

        right_left = start_tile%n_row
        if right_left == 0:
            actions_allowed.append(actions["right"])
        if right_left > 0 and right_left < (n_row-1):
            actions_allowed.append(actions["right"])
            actions_allowed.append(actions["left"])
        if right_left == (n_row-1):
            actions_allowed.append(actions["left"])

        up_down = int(start_tile/n_row)
        if up_down == 0:
            actions_allowed.append(actions["down"])
        if up_down > 0 and up_down < (n_row-1):
            actions_allowed.append(actions["down"])
            actions_allowed.append(actions["up"])
        if up_down == (n_row-1):
            actions_allowed.append(actions["up"])

        if forbidden_action != None:
            actions_allowed.remove(forbidden_action)
        
        if len(actions_allowed) > 0:
            random.shuffle(actions_allowed)
            action_used = actions_allowed[0]
            forbidden_action = -action_used
            swap_tile = start_tile+action_used
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