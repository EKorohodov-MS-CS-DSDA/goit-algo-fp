import uuid

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


def BFS(root):
    visit_order = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node not in visit_order:
            visit_order.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return visit_order


def DFS(root):
    visit_order = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visit_order:
            visit_order.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    return visit_order


def update_colors(root, node, color):
    if root is None:
        return

    if root.id == node.id:
        root.color = color

    update_colors(root.left, node, color)
    update_colors(root.right, node, color)


def draw_tree_traversal(tree_root, visited, title='BFS'):
    tree = nx.Graph()
    pos = {tree_root.id: (0, 0)}

    plt.figure(figsize=(8, 5))

    for visited_node in visited:
        plt.clf()
        plt.title(f"{title} Traversal")

        update_colors(tree_root, visited_node, '#1296F0')

        tree = add_edges(tree, tree_root, pos)
        colors = [node[1]['color'] for node in tree.nodes(data=True)]
        labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2000, node_color=colors)
        plt.pause(0.5)

    plt.show()


def make_tree():
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    return root


def main():
    tree = make_tree()
    dfs_order = DFS(tree)
    draw_tree_traversal(tree, dfs_order, title='DFS')

    tree = make_tree()
    bfs_order = BFS(tree)
    draw_tree_traversal(tree, bfs_order, title='BFS')


if __name__ == '__main__':
    main()
