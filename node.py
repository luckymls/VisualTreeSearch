
class Node:
    """
    Class that defines the nodes of the three and its methods
    """

    def __init__(self, state, parent=None, children=None, action=None, path_cost=None, depth=0, graph_index=None):
        """
        Initializes the node of the tree
        :param state: problem-dependent representation of the corresponding state
        :param parent: pointer to the parent node
        :param children: list of pointers to the children nodes
        :param action: [???] description of the action that lead from the parent node to this one
        :param path_cost: the total cost of the actions on the path from the root to this node
        :param depth: the number of actions ion the path from the root to this node
        :param graph_index: the index of the node in the complete graph
        """

        if children is None:
            children = []
        self.state = state
        self.parent = parent
        self.children = children
        self.action = action
        self.path_cost = path_cost
        self.depth = depth
        self.graph_index = graph_index

    def correct_path(self):
        """
        Function that returns the correct path, from the node to the root
        :return: correct path
        """
        path = [self]
        iterator_node = self.parent

        while iterator_node is not None:
            path.append(iterator_node)
            iterator_node = iterator_node.parent

        return path

    def expand(self, problem):
        for (result, action) in problem.successor_function(self):
            new_node = Node(state=result,
                            parent=self,
                            action=action,
                            path_cost=(self.path_cost + problem.step_cost),
                            depth=(self.depth+1))

            for child in self.children:
                if new_node.state == child.state:
                    return self.children

            self.children.append(new_node)
        return self.children


def print_path(path):
    for node in reversed(path):
        print(node.action)
        print("|")
        print("V")
        print(node.state)