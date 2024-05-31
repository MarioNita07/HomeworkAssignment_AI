import heapq

def astar_tsp(graph, start):
    pq = []
    heapq.heappush(pq, (heuristic(start, graph), 0, start, [start]))
    best_cost = float('inf')
    best_path = []

    while pq:
        estimated_total_cost, current_cost, current_node, path = heapq.heappop(pq)

        if len(path) == len(graph) + 1 and path[0] == path[-1]:
            if current_cost < best_cost:
                best_cost = current_cost
                best_path = path
            continue

        for neighbor in graph[current_node]:
            if neighbor not in path or (neighbor == start and len(path) == len(graph)):
                new_cost = current_cost + graph[current_node][neighbor]
                new_path = path + [neighbor]
                estimated_cost = new_cost + heuristic(neighbor, graph)
                heapq.heappush(pq, (estimated_cost, new_cost, neighbor, new_path))

    return best_path, best_cost
def calculate_minimum_spanning_tree(graph):
    # Initialize minimum spanning tree as an empty dictionary
    mst = {}
    
    # Choose arbitrary starting node
    start_node = list(graph.keys())[0]
    
    # Initialize set of visited nodes
    visited = set([start_node])
    
    # Initialize priority queue (heap) with edges from the starting node
    pq = [(weight, start_node, neighbor) for neighbor, weight in graph[start_node].items()]
    heapq.heapify(pq)
    
    while pq:
        weight, u, v = heapq.heappop(pq)
        if v not in visited:
            visited.add(v)
            mst.setdefault(u, {})[v] = weight
            mst.setdefault(v, {})[u] = weight
            for neighbor, weight in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, v, neighbor))
    
    return mst

def estimate_minimum_spanning_tree_cost(mst, node):
    # Calculate the total weight of the minimum spanning tree rooted at the given node
    return sum(weight for weight in mst[node].values())


def heuristic(node, graph):
    if 'mst' not in heuristic.__dict__:
        heuristic.mst = calculate_minimum_spanning_tree(graph)
    return estimate_minimum_spanning_tree_cost(heuristic.mst, node)
