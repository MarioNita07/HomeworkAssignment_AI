import heapq

def ucs_tsp(graph, start):
    pq = []
    heapq.heappush(pq, (0, start, [start]))
    best_cost = float('inf')
    best_path = []

    while pq:
        current_cost, current_node, path = heapq.heappop(pq)

        if len(path) == len(graph) + 1 and path[0] == path[-1]:
            if current_cost < best_cost:
                best_cost = current_cost
                best_path = path
            continue

        for neighbor in graph[current_node]:
            if neighbor not in path or (neighbor == start and len(path) == len(graph)):
                new_cost = current_cost + graph[current_node][neighbor]
                new_path = path + [neighbor]
                heapq.heappush(pq, (new_cost, neighbor, new_path))

    return best_path, best_cost
