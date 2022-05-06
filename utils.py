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
