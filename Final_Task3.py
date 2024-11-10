import matplotlib.pyplot as plt
import networkx as nx
import heapq

GRAPH = {
    "Kyiv": {"Makariv": 50, "Borodyanka": 45, "Fastiv": 60},
    "Makariv": {"Kyiv": 50, "Radomyshl": 40, "Borodyanka": 20, "Kocheriv": 35},
    "Borodyanka": {"Kyiv": 45, "Makariv": 20},
    "Fastiv": {"Kyiv": 60, "Brusyliv": 35},
    "Brusyliv": {"Fastiv": 35, "Popil'nya": 35, "Kocheriv": 15},
    "Popil'nya": {"Brusyliv": 35, "Zhytomyr": 60},
    "Kocheriv": {"Brusyliv": 15, "Radomyshl": 15, "Makariv": 35, "Korostyshiv": 20},
    "Radomyshl": {"Kocheriv": 15, "Makariv": 40, "Cherniakhiv": 40},
    "Cherniakhiv": {"Radomyshl": 40, "Zhytomyr": 20},
    "Korostyshiv": {"Kocheriv": 20, "Zhytomyr": 25},
    "Zhytomyr": {"Cherniakhiv": 20, "Korostyshiv": 25, "Popil'nya": 65}
}


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


def main():
    print(dijkstra(GRAPH, "Kyiv"))


if __name__ == "__main__":
    main()
