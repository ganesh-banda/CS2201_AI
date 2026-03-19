# UGV Navigation with Dynamic Obstacles

## Overview

This project simulates an **Unmanned Ground Vehicle (UGV)** navigating in a grid environment with **dynamic obstacles**. Unlike static environments, obstacles can appear randomly during execution, requiring the algorithm to **recompute paths in real time**.

---

## Concept

### Dynamic Environment

* Obstacles are **not fixed**
* New obstacles may appear while the UGV is moving
* The path must be updated continuously

---

## Approach Used

A simplified approach using **A* with Replanning** is implemented:

1. Compute shortest path using A*
2. Move one step along the path
3. Randomly introduce a new obstacle
4. Recompute path from current position
5. Repeat until goal is reached

---

## State Space Representation

* **States:** Grid cells (x, y)
* **Actions:** Move up, down, left, right
* **Cost:** Each move has cost = 1

Grid representation:

* `0` → Free space
* `1` → Obstacle

---

## Evaluation Function

```id="u1c3mw"
f(n) = g(n) + h(n)
```

* **g(n):** Cost from start to node
* **h(n):** Manhattan distance to goal

---

## How to Run

1. Open terminal in the project folder
2. Run:

   ```
   python main.py
   ```
3. The program will:

   * Generate grid
   * Simulate movement
   * Add obstacles dynamically
   * Recompute path

---

## Example Output

```id="3b9q2l"
Current Path: [(0, 6), (0, 7), (0, 8), (0, 9), (1, 9), ..., (9, 9)]
Current Path: [(0, 7), (0, 8), (0, 9), (1, 9), ..., (9, 9)]
New obstacle added at: (3, 5)
Current Path: [(1, 9), (2, 9), (3, 9), ..., (9, 9)]
Reached Goal!
```

---

## Measures of Effectiveness

* Replanning time
* Path optimality
* Adaptability to changes
* Number of re-computations
* Success rate

---

## Comparison with Static Approach

| Feature        | A* (Static)  | Dynamic Approach |
| -------------- | ------------ | ---------------- |
| Obstacles      | Fixed        | Changing         |
| Replanning     | Not required | Required         |
| Flexibility    | Low          | High             |
| Real-world use | Limited      | Practical        |

---

## Technologies Used

* Python
* Heap Queue (Priority Queue)
* A* Search Algorithm

---

## Applications

* Military UGV navigation
* Autonomous vehicles
* Robotics in unknown environments
* Disaster response robots

---

## Notes

* This is a **simplified dynamic planning model**
* Full implementation can use **D* or D* Lite algorithms**
* Grid size can be increased (e.g., 70×70)

---

## Conclusion

Dynamic environments require continuous replanning. This project demonstrates how a UGV can adapt to changing obstacles using a simplified A*-based approach, making it suitable for real-world navigation scenarios.

---
