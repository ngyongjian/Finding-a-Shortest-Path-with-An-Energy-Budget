from math import sqrt
from queue import PriorityQueue
import helper

def astar(graph, start_node, end_node, energy_budget, cost_dict, dist_dict, coord_dict, h_factor):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, (0, [start_node])))

    while not pq.empty():
        cost, (energy_used, path) = pq.get()
        node = path[-1]

        visited.add(node)

        if node == end_node:
            path_info = helper.PathInfo()
            path_info.path = "->".join(path)
            path_info.dist = helper.calc_path_distance(path, dist_dict)
            path_info.energy = helper.calc_path_energy(path, cost_dict)
            return path_info

        for neighbor in graph[node]:
            if neighbor not in visited:
                new_energy = energy_used + cost_dict[f"{node},{neighbor}"]

                if new_energy <= energy_budget:
                    path_dist = cost + dist_dict[f"{node},{neighbor}"]
                    h_dist = h_func(neighbor, end_node, coord_dict)*h_factor
                    total_dist = path_dist + h_dist

                    new_path = list(path)
                    new_path.append(neighbor)

                    pq.put((total_dist, (new_energy, new_path)))

    return helper.PathInfo()


def h_func(source, destination, coord_dict):
    source_coord = coord_dict[source]
    dest_coord = coord_dict[destination]

    dx = abs(source_coord[0] - dest_coord[0])
    dy = abs(source_coord[1] - dest_coord[1])

    return sqrt(dx**2 + dy**2)