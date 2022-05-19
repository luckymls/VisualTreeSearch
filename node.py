class Node:
    """
    Class that defines the nodes of the three and its methods
    """

    def __init__(self, state, parent=None, children=None, action=None, path_cost=0, depth=0,
                 graph_index=None, g=None, h=None):
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
        self.g = g
        self.h = h

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
        """
        Function that expands the node, creating the node's children and returns the list of
        the child nodes
        """

        unique_node = True

        # check all the possible states and actions from the given node using the successor
        # function of the given problem
        for (result, action) in problem.successor_function(self):

            # create the node based on the information gathered by the successor function
            new_node = Node(state=result,
                            parent=self,
                            action=action,
                            path_cost=(self.path_cost + problem.step_cost),
                            depth=(self.depth + 1))

            # filter out all the duplicated nodes
            for child in self.children:
                if new_node.state == child.state:
                    unique_node = False

            if unique_node:
                self.children.append(new_node)
                problem.expanded_nodes += 1

        return self.children
