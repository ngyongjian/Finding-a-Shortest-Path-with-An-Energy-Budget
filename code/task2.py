from queue import PriorityQueue
import helper


def bfs(graph, start_node, end_node, energy_budget, cost_dict, dist_dict):
    visited = set()
    queue = [[0, [start_node]]]

    while queue:
        energy_used, path = queue.pop(0)
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
                    queue.append([new_energy, (path + [neighbor])])

    return helper.PathInfo()


def dfs(graph, start_node, end_node, energy_budget, cost_dict, dist_dict):
    visited = set()
    stack = [[0, [start_node]]]

    while stack:
        energy_used, path = stack.pop()
        node = path[-1]

        visited.add(node)

        if node == end_node:
            path_info = helper.PathInfo()
            path_info.path = "->".join(path)
            path_info.dist = helper.calc_path_distance(path, dist_dict)
            path_info.energy = helper.calc_path_energy(path, cost_dict)
            return path_info

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                new_energy = energy_used + cost_dict[f"{node},{neighbor}"]

                if new_energy <= energy_budget:
                    stack.append([new_energy, (path + [neighbor])])

    return helper.PathInfo()


def ucs(graph, start_node, end_node, energy_budget, cost_dict, dist_dict):
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
                    new_dist = dist_dict[f"{node},{neighbor}"]
                    total_dist = cost + new_dist

                    new_path = list(path)
                    new_path.append(neighbor)

                    pq.put((total_dist, (new_energy, new_path)))

    return helper.PathInfo()


def dijkstra_with_energy(graph, start_node, end_node, cost_dict, dist_dict, energy_budget):
    visited = set()
    distances = {node: float("inf") for node in graph}
    energies = {node: float("inf") for node in graph}
    distances[start_node] = 0
    energies[start_node] = 0
    pq = PriorityQueue()
    pq.put((0, (0, [start_node])))

    while not pq.empty():
        cost, (energy_used, path) = pq.get()
        node = path[-1]
        # print(node)
        if node in visited:
            continue

        visited.add(node)

        if node == end_node:
            path_info = helper.PathInfo()
            path_info.path = "->".join(path)
            path_info.dist = distances[node]
            path_info.energy = energies[node]
            return path_info

        for neighbor in graph[node]:
            edge_key = f"{node},{neighbor}"
            new_distance = distances[node] + dist_dict.get(edge_key, float("inf"))
            new_energy = energies[node] + cost_dict.get(edge_key, 0)

            if new_energy <= energies[neighbor] and new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                energies[neighbor] = new_energy

            if new_energy <= energy_budget:
                new_path = list(path)
                new_path.append(neighbor)

                pq.put((new_distance, (new_energy, new_path)))

    return helper.PathInfo()
