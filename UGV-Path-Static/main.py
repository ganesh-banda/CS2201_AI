import heapq
import random


ROWS, COLS = 10, 10   


def generate_grid(density=0.2):
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    for i in range(ROWS):
        for j in range(COLS):
            if random.random() < density:
                grid[i][j] = 1  

    return grid


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    pq = [(0, start)]
    came_from = {}
    g_cost = {start: 0}

    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_cost = g_cost[current] + 1

                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    f_cost = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(pq, (f_cost, (nx, ny)))
                    came_from[(nx, ny)] = current

    return None



grid = generate_grid(density=0.2)

start = (0, 0)
goal = (9, 9)


grid[start[0]][start[1]] = 0
grid[goal[0]][goal[1]] = 0

path = astar(grid, start, goal)

print("Grid (0=free, 1=obstacle):")
for row in grid:
    print(row)

print("\nShortest Path:")
print(path)