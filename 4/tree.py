import numpy as np

def gen_tree_list(data):
    n = int(data.pop(0))

    nodes1, nodes2 = zip(*map(lambda x: tuple(x.split(' ')), data))
    nodes1 = np.asarray(nodes1, int)
    nodes2 = np.asarray(nodes2, int)

    graph_list = [[i] + list(nodes2[np.where(nodes1 == i)]) for i in range(1, n + 1)]

    return graph_list

def connection_counter(graph_list):
    branches = []
    while len(graph_list) > 0:
        first_tree, *other_trees = graph_list
        first_tree = set(first_tree)

        i = -1
        while len(first_tree) > i:
            i = len(first_tree)

            remaining_trees = []
            for next_tree in other_trees:
                next_tree = set(next_tree)

                if (first_tree & next_tree) != set():
                    first_tree |= next_tree

                else:
                    remaining_trees.append(next_tree)

            other_trees = remaining_trees

        branches.append(first_tree)
        graph_list = other_trees

    return  branches, len(branches) - 1


def tree():
    file = input("Enter graph data filename\n")
    with open(file, 'r+') as f:
        data = [line.rstrip('\n') for line in f]

    graph_list = gen_tree_list(data)

    branches, edges = connection_counter(graph_list)
    print(branches)
    print(edges)
if __name__ == "__main__":
    tree()





file = '/Volumes/KatahdinHD/Downloads/rosalind_ini6.txt'
with open(file, 'r+') as f:
    data = [line.rstrip('\n') for line in f]
