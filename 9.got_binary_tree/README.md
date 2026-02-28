<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Tkinter-FF6F00?style=for-the-badge&logoColor=white" />
</p>

# 🌳 Game of Thrones — Binary Tree Visualizer

> An interactive **binary tree visualizer** built with **Tkinter** — using the Stark family from Game of Thrones to demonstrate tree traversal, parent finding, and children lookup in real time.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🌲 Visual Tree | Graphical binary tree rendered on a Tk canvas |
| 🔍 Find Parent | Enter a name → highlights the parent node in green |
| 👶 Find Children | Enter a name → highlights the child nodes in green |
| 🎬 Traversal Animation | Watch DFS traversal animate node-by-node |
| 🎨 Color Coding | Red = selected, Green = result, Orange = traversal step |

---

## 🏗️ Project Structure

```
got_binary_tree/
├── main.py              # Full app — Node class, tree logic, Tkinter visualizer
├── tree.py              # Standalone tree data structure
├── visualize.py         # Separate visualization helper
├── got_family_tree      # Tree data file
├── got_family_tree.pdf  # Visual reference
├── step_0.png           # Traversal step screenshots
├── step_1.png
└── step_2.png
```

---

## 🚀 Quick Start

```bash
# No external dependencies — uses Python's built-in Tkinter

python main.py
```

A window will open showing the Stark family tree:

```
           Ned
          /   \
       Robb   Sansa
       / \
    Arya  Bran
```

---

## 🔧 How to Use

1. **Enter a name** (e.g., `Robb`) in the input field
2. Click **Find Parent** → highlights Ned (parent) in green, Robb in red
3. Click **Find Children** → highlights Arya & Bran (children) in green
4. Check **Show Traversal Animation** → watch the DFS walk step by step

---

## 🧠 Concepts Demonstrated

- **Binary Tree** data structure
- **Depth-First Search (DFS)** traversal
- **Parent/child relationships** in trees
- **GUI programming** with Tkinter canvas drawing

---

## 🛠️ Tech Stack

- **Python 3** — core language
- **Tkinter** — built-in GUI framework
- **Graphviz** (optional) — for PDF generation

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
