import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def draw_heap(heap):
    tree = make_tree_from_heap(heap)
    draw_tree(tree)


def make_tree_from_heap(heap):
    root = Node(heap[0])
    tree_nodes = [root]

    for i in range(len(heap)):
        idx_left = 2 * i + 1
        idx_right = 2 * i + 2

        if idx_left < len(heap):
            tree_nodes[i].left = Node(heap[idx_left])
            tree_nodes.append(tree_nodes[i].left)
        if idx_right < len(heap):
            tree_nodes[i].right = Node(heap[idx_right])
            tree_nodes.append(tree_nodes[i].right)

    return tree_nodes[0]


def make_tree():
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    
    return root


def main():
    heap = [0, 4, 5, 10, 1 , 8, 14, 85, 23, 6, 7]
    heapq.heapify(heap)
    draw_heap(heap)


if __name__ == "__main__":
    main()