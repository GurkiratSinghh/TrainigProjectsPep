import tkinter as tk
import time

# ---------- NODE ----------
class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.left = None
        self.right = None
        self.x = x
        self.y = y


# ---------- TREE LOGIC ----------
def find_node(root, name):
    if not root:
        return None
    if root.name.lower() == name.lower():
        return root
    return find_node(root.left, name) or find_node(root.right, name)


def find_parent(root, target, parent=None):
    if not root:
        return None
    if root == target:
        return parent
    return (
        find_parent(root.left, target, root)
        or find_parent(root.right, target, root)
    )


def dfs_traversal(root, visit):
    if not root:
        return
    visit(root)
    dfs_traversal(root.left, visit)
    dfs_traversal(root.right, visit)


# ---------- VISUALIZER ----------
class TreeVisualizer:
    def __init__(self, root):
        self.root = root
        self.red_node = None
        self.green_nodes = []
        self.orange_node = None

        self.window = tk.Tk()
        self.window.title("Binary Tree Visualizer (Parent / Children + Traversal)")

        self.canvas = tk.Canvas(self.window, width=900, height=520, bg="white")
        self.canvas.pack()

        controls = tk.Frame(self.window)
        controls.pack(pady=8)

        tk.Label(controls, text="Enter Name:").grid(row=0, column=0, padx=5)
        self.entry = tk.Entry(controls, width=20)
        self.entry.grid(row=0, column=1, padx=5)

        tk.Button(controls, text="Find Parent", command=self.on_find_parent)\
            .grid(row=0, column=2, padx=5)

        tk.Button(controls, text="Find Children", command=self.on_find_children)\
            .grid(row=0, column=3, padx=5)

        self.animate_var = tk.IntVar()
        tk.Checkbutton(
            controls,
            text="Show Traversal Animation",
            variable=self.animate_var
        ).grid(row=0, column=4, padx=10)

        self.status = tk.Label(self.window, text="", fg="blue")
        self.status.pack()

        self.draw_tree()

    # ---------- DRAW ----------
    def draw_tree(self):
        self.canvas.delete("all")
        self._draw_edges(self.root)
        self._draw_nodes(self.root)
        self.window.update()

    def _draw_edges(self, node):
        if not node:
            return
        if node.left:
            self.canvas.create_line(node.x, node.y, node.left.x, node.left.y)
            self._draw_edges(node.left)
        if node.right:
            self.canvas.create_line(node.x, node.y, node.right.x, node.right.y)
            self._draw_edges(node.right)

    def _draw_nodes(self, node):
        if not node:
            return

        color = "lightblue"
        if node == self.orange_node:
            color = "orange"
        if node == self.red_node:
            color = "red"
        if node in self.green_nodes:
            color = "green"

        r = 22
        self.canvas.create_oval(
            node.x - r, node.y - r,
            node.x + r, node.y + r,
            fill=color
        )
        self.canvas.create_text(node.x, node.y, text=node.name)

        self._draw_nodes(node.left)
        self._draw_nodes(node.right)

    # ---------- TRAVERSAL ----------
    def animate_traversal(self):
        def visit(node):
            self.orange_node = node
            self.draw_tree()
            time.sleep(0.6)

        dfs_traversal(self.root, visit)
        self.orange_node = None

    # ---------- ACTIONS ----------
    def on_find_parent(self):
        self.reset_highlights()
        name = self.entry.get().strip()

        target = find_node(self.root, name)
        if not target:
            self.status.config(text="Person not found")
            self.draw_tree()
            return

        if self.animate_var.get():
            self.animate_traversal()

        parent = find_parent(self.root, target)
        self.red_node = target
        if parent:
            self.green_nodes = [parent]
            self.status.config(text=f"Parent of {target.name} is {parent.name}")
        else:
            self.status.config(text=f"{target.name} is root (no parent)")

        self.draw_tree()

    def on_find_children(self):
        self.reset_highlights()
        name = self.entry.get().strip()

        target = find_node(self.root, name)
        if not target:
            self.status.config(text="Person not found")
            self.draw_tree()
            return

        if self.animate_var.get():
            self.animate_traversal()

        self.red_node = target
        if target.left:
            self.green_nodes.append(target.left)
        if target.right:
            self.green_nodes.append(target.right)

        if self.green_nodes:
            names = ", ".join(n.name for n in self.green_nodes)
            self.status.config(text=f"Children of {target.name}: {names}")
        else:
            self.status.config(text=f"{target.name} has no children")

        self.draw_tree()

    def reset_highlights(self):
        self.red_node = None
        self.green_nodes = []
        self.orange_node = None


# ---------- BUILD TREE ----------
ned = Node("Ned", 450, 60)
robb = Node("Robb", 250, 180)
sansa = Node("Sansa", 650, 180)
arya = Node("Arya", 200, 340)
bran = Node("Bran", 300, 340)

ned.left = robb
ned.right = sansa
robb.left = arya
robb.right = bran

# ---------- RUN ----------
TreeVisualizer(ned).window.mainloop()
