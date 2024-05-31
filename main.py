import numpy as np
from bsf_tsp import bfs_tsp
from ucs_tsp import ucs_tsp
from astar_tsp import astar_tsp

# Example graph: dictionary of dictionaries
# For a real application, replace with your graph representation
graph = {
    0: {1: 10, 2: 15, 3: 20},
    1: {0: 10, 2: 35, 3: 25},
    2: {0: 15, 1: 35, 3: 30},
    3: {0: 20, 1: 25, 2: 30}
}

start_node = 0

# Running BFS
bfs_path, bfs_cost = bfs_tsp(graph, start_node)
print(f"BFS Path: {bfs_path}, Cost: {bfs_cost}")

# Running UCS
ucs_path, ucs_cost = ucs_tsp(graph, start_node)
print(f"UCS Path: {ucs_path}, Cost: {ucs_cost}")

# Running A*
astar_path, astar_cost = astar_tsp(graph, start_node)
print(f"A* Path: {astar_path}, Cost: {astar_cost}")
