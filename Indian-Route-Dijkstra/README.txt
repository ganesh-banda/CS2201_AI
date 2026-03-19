# Indian Route Finder using Dijkstra Algorithm

## Overview

This project implements **Dijkstra’s Algorithm (Uniform Cost Search)** to find the shortest distance between cities in India. Cities are represented as nodes and road distances as weighted edges.

---

## Files

* `main.py` → Python program implementing Dijkstra’s algorithm
* `indian_cities.csv` → Dataset containing city distances

---

## Concept

The program models cities as a graph and calculates the minimum distance from a given start city to all other cities using a priority queue.

---

## How to Run

1. Open terminal in the project folder
2. Run:

   ```
   python main.py
   ```
3. Enter the start city

---

## Example Input

```
Enter start city: Hyderabad
```

---

## Example Output

```
Shortest distances from Hyderabad
Delhi: 1464 km
Mumbai: 710 km
Pune: 560 km
Bangalore: 570 km
Chennai: 920 km
```

---

## Requirements

* Python 3.x

---

## Key Features

* Uses Dijkstra’s Algorithm
* Reads data from CSV
* Efficient shortest path computation
* Simple and user-friendly

---

## Applications

* GPS navigation
* Route optimization
* Transportation systems

---

## Notes

* City names should match dataset format
* Keep CSV file in same folder as `main.py`
