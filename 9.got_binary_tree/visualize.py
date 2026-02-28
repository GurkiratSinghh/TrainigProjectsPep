from graphviz import Digraph
import time
import os

os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

def visualize_path(root, current):
    dot = Digraph(format="png")

    def draw(node):
        if node is None:
            return

        if node == current:
            dot.node(node.name, node.name, style="filled", color="red")
        else:
            dot.node(node.name, node.name)

        if node.left:
            dot.edge(node.name, node.left.name)
            draw(node.left)
        if node.right:
            dot.edge(node.name, node.right.name)
            draw(node.right)

    draw(root)
    dot.render("step", view=True, cleanup=True)
    time.sleep(1)
