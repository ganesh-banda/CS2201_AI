# UGV Path Planning using A* Algorithm

## Overview

This project implements the **A* (A-Star) algorithm** for an Unmanned Ground Vehicle (UGV) to navigate a grid-based environment. The goal is to find the shortest path from a start position to a goal position while avoiding obstacles.

---

## Concept

### State Space Representation

* **States:** Grid cells (x, y)
* **Actions:** Move up, down, left, right
* **Cost:** Each move has a cost of 1

The environment is represented as a 2D grid:

* `0` → Free cell
* `1` → Obstacle

---

## Evaluation Function

The A* algorithm uses:

```
f(n) = g(n) + h(n)
```

* **g(n):** Cost from start to current node
* **h(n):** Heuristic (Manhattan distance to goal)

---

## Algorithm Steps

1. Initialize OPEN list (priority queue)
2. Add start node
3. Repeat:

   * Select node with lowest f(n)
   * If goal is reached → return path
   * Explore neighbors
   * Skip obstacles
   * Update costs
4. Continue until path is found

---

## How to Run

1. Open terminal in the project folder
2. Run:

   ```
   python main.py
   ```
3. The program will:

   * Generate a grid with obstacles
   * Compute the shortest path
   * Display the path

---

## Example Output

### Grid (0 = free, 1 = obstacle)

```
[0, 0, 0, 0, 0]
[0, 1, 1, 0, 0]
[0, 0, 0, 0, 1]
[0, 1, 0, 0, 0]
```

### Shortest Path

```
[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 3)]
```

---

## Obstacle Density Levels

* Low → 0.2
* Medium → 0.4
* High → 0.6

Obstacle density controls how many blocked cells are generated.

---

## Measures of Effectiveness

* Path length
* Time taken
* Nodes explored
* Obstacle avoidance success

---

## Technologies Used

* Python
* Heap Queue (Priority Queue)
* A* Search Algorithm

---

## Applications

* Autonomous robots
* Military UGV navigation
* Game AI pathfinding
* Robotics and automation

---

## Notes

* Grid size can be changed (e.g., 70×70)
* Start and goal must not be obstacles
* A* is faster than Dijkstra due to heuristic guidance

---

## Conclusion

The A* algorithm efficiently computes the shortest path in a grid with obstacles. It is widely used in real-world navigation systems due to its optimality and performance.

---
