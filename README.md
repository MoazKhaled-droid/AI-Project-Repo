# 8-Puzzle Solver using AI Search Algorithms 🧩

## 📖 Project Overview
This project is a Python-based implementation of an intelligent agent designed to solve the **8-Puzzle Game**. It utilizes and compares three fundamental AI search algorithms to find the optimal path from a scrambled start state to the goal state.

The primary goal is to demonstrate the difference between **Uninformed Search** (Blind) and **Informed Search** (Heuristic-based) strategies in terms of performance and resource usage.

---

## 📽️ Project Presentation & Documentation
**Detailed explanation included!** For a deep dive into the logic, mathematical analysis, and step-by-step tracing of the algorithms, please refer to the presentation file included in this repository.

📂 **File:** `solving 8-puzzle.pptx` inside the repository.  
It covers:
- Theoretical background of BFS, DlS, and A*.
- Detailed comparison of Time & Space Complexity & completness & optimality.
- Visual examples of the search trees.

---

## 🧠 Algorithms Implemented

### 1. A* Search (A-Star) ⭐ **(Recommended)**
- **Type:** Informed Search.
- **Heuristic Used:** Misplaced Tiles (Counts tiles not in the correct position).
- **Mechanism:** It evaluates nodes based on `f(n) = g(n) + h(n)` to guarantee the **optimal path** with high efficiency.

### 2. Breadth-First Search (BFS)
- **Type:** Uninformed Search.
- **Mechanism:** Explores the search tree level by level.
- **Pros:** Guaranteed to find the **shortest path** (Optimal).
- **Cons:** High memory consumption due to storing the entire frontier.

### 3. Depth-Limited Search (DLS)
- **Type:** Uninformed Search.
- **Mechanism:** Explores deep into branches up to a specific **depth limit** to avoid infinite loops found in standard DFS.
- **Pros:** Extremely memory efficient (Linear Space).
- **Cons:** Not guaranteed to find the shortest path (Non-Optimal).

---

## 📊 Performance Comparison Matrix

| Algorithm | Completeness | Optimality | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **A* Search** | ✅ Yes | ✅ Yes (Shortest Path) | 🚀 Fast | 🔴 High (O(b^d)) |
| **BFS** | ✅ Yes | ✅ Yes (Shortest Path) | 🐢 Slow | 🔴 High (O(b^d)) |
| **DLS** | ❌ No (Depends on limit) | ❌ No | 🚶 Average | 🟢 Low (O(b \times l)) |

**Conclusion:** **A* Search** is the superior choice for the 8-puzzle problem. It balances the optimality of BFS with execution speed by using the heuristic function to prune irrelevant paths, making it significantly faster than blind search methods.

---

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/MoazKhaled-droid/AI-Project-Repo](https://github.com/MoazKhaled-droid/AI-Project-Repo)
