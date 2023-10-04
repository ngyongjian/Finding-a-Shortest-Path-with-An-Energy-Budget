from queue import PriorityQueue
import helper


def bfs(graph, start_node, end_node, cost_dict, dist_dict):
    visited = set()
    queue = [[start_node]]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            visited.add(node)

            if node == end_node:
                path_info = helper.PathInfo()
                path_info.path = "->".join(path)
                path_info.dist = helper.calc_path_distance(path, dist_dict)
                path_info.energy = helper.calc_path_energy(path, cost_dict)
                return path_info

            for neighbor in graph[node]:
                queue.append((path + [neighbor]))

    return helper.PathInfo()


def dfs(graph, start_node, end_node, cost_dict, dist_dict):
    visited = set()
    stack = [[start_node]]

    while stack:
        path = stack.pop()
        node = path[-1]

        if node not in visited:
            visited.add(node)

            if node == end_node:
                path_info = helper.PathInfo()
                path_info.path = "->".join(path)
                path_info.dist = helper.calc_path_distance(path, dist_dict)
                path_info.energy = helper.calc_path_energy(path, cost_dict)
                return path_info

            for neighbor in reversed(graph[node]):
                stack.append((path + [neighbor]))

    return helper.PathInfo()


def ucs(graph, start_node, end_node, cost_dict, dist_dict):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, [start_node]))

    while not pq.empty():
        cost, path = pq.get()
        node = path[-1]

        if node not in visited:
            visited.add(node)

            if node == end_node:
                path_info = helper.PathInfo()
                path_info.path = "->".join(path)
                path_info.dist = helper.calc_path_distance(path, dist_dict)
                path_info.energy = helper.calc_path_energy(path, cost_dict)
                return path_info

            for neighbor in graph[node]:
                new_dist = dist_dict[f"{node},{neighbor}"]
                score = cost + new_dist

                new_path = list(path)
                new_path.append(neighbor)

                pq.put((score, new_path))

    return helper.PathInfo()
