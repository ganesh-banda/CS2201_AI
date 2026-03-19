import heapq
import random

ROWS, COLS = 10, 10

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
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

            if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == 0:
                new_cost = g_cost[current] + 1

                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    f_cost = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(pq, (f_cost, (nx, ny)))
                    came_from[(nx, ny)] = current

    return None


# -------- MAIN --------
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

start = (0, 0)
goal = (9, 9)

current = start

while current != goal:
    path = astar(grid, current, goal)

    if not path:
        print("No path available!")
        break

    print("Current Path:", path)

    # Move one step
    current = path[1]

    # Simulate dynamic obstacle
    if random.random() < 0.3:
        x, y = random.randint(0, ROWS-1), random.randint(0, COLS-1)
        if (x, y) != current and (x, y) != goal:
            grid[x][y] = 1
            print("New obstacle added at:", (x, y))

print("Reached Goal!")