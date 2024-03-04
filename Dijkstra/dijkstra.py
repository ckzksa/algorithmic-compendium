# using priority queue
import heapq
from collections import deque

def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    
    predecessors = {node: None for node in graph}
    
    priority_queue = [(0, start_node)]
    
    while priority_queue:
        distance, node = heapq.heappop(priority_queue)
        if distance > distances[node]:
            continue

        for neighbor, weight in graph[node].items():
            new_distance = distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = node
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances, predecessors

def get_direction(starting_point, destinations):
    if starting_point not in graph:
        return None

    if set(destinations) - set(graph.keys()):
        return None

    start = starting_point
    full_path = deque()
    distance = 0
    
    for destination in destinations:
        distances, predecessors = dijkstra(graph, start)

        path = deque()
        stage = destination
        while stage != start:
            path.appendleft(stage)
            stage = predecessors[stage]

        distance += distances[destination]
        full_path.extend(path)
        start = destination

    full_path.appendleft(starting_point)
    return distance, list(full_path)

graph = {
    "London": {"Paris": 344, "Amsterdam": 357, "Brussels": 320},
    "Paris": {"London": 344, "Berlin": 1055, "Madrid": 1054},
    "Berlin": {"Paris": 1055, "Amsterdam": 650, "Prague": 280, "Vienna": 655, "Warsaw": 584},
    "Madrid": {"Paris": 1054, "Rome": 1418, "Lisbon": 1263},
    "Amsterdam": {"London": 357, "Berlin": 650, "Brussels": 173},
    "Brussels": {"London": 320, "Amsterdam": 173, "Paris": 265},
    "Rome": {"Madrid": 1418, "Vienna": 839},
    "Vienna": {"Berlin": 655, "Rome": 839, "Prague": 330},
    "Prague": {"Berlin": 280, "Vienna": 330, "Warsaw": 517},
    "Warsaw": {"Prague": 517, "Berlin": 584},
    "Lisbon": {"Madrid": 1263}
}

if __name__ == "__main__":
    distance, path = get_direction("London", ["Warsaw", "Rome"])
    print(f"{distance}km : {" -> ".join(map(str, path))}")