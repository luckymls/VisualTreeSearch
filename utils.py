import copy


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
Given a strategy function it returns the function name
'''
def get_strategy_name(strategy):
    return strategy.__qualname__


'''
Given a multidimensional python dictionary and a key, it returns the path to the key
'''
def search(d, k, path=None):
    if path is None:
        path = []
    

    if not isinstance(d, dict): # No keys found
        return False
    

    if k in d.keys(): # Keys found
        path.append(k)
        return path
    
    else:
        check = list(d.keys())
        while check:
            first = check[0]
            path.append(first)

            if search(d[first], k, path) is not False:
                break
            else:
                check.pop(0)
                path.pop(-1)
        else:
            return False
        return path



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
Remove duplicate from tree
'''
def remove_duplicates(complete_tree):
    
    pass

