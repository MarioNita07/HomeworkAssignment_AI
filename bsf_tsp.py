from collections import deque

def bfs_tsp(graph, start):
    queue = deque([(start, [start])])
    best_cost = float('inf')
    best_path = []

    while queue:
        current_node, path = queue.popleft()

        if len(path) == len(graph) + 1 and path[0] == path[-1]:
            current_cost = calculate_cost(graph, path)
            if current_cost < best_cost:
                best_cost = current_cost
                best_path = path
            continue

        for neighbor in graph[current_node]:
            if neighbor not in path or (neighbor == start and len(path) == len(graph)):
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return best_path, best_cost

def calculate_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]
    return cost
