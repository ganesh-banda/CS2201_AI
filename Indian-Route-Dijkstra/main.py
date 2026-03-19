import heapq
import csv

def load_graph(filename):
    graph = {}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            origin = row['Origin']
            dest = row['Destination']
            dist = int(row['Distance'])

            if origin not in graph:
                graph[origin] = []
            if dest not in graph:
                graph[dest] = []

            graph[origin].append((dest, dist))
            graph[dest].append((origin, dist))

    return graph


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)

        for neighbor, weight in graph[node]:
            new_dist = curr_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances


# MAIN
graph = load_graph('indian_cities.csv')

start = input("Enter start city: ")

result = dijkstra(graph, start)

print("\nShortest distances from", start)
for city, dist in result.items():
    print(f"{city}: {dist} km")