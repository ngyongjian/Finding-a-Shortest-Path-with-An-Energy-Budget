import json
from typing import Tuple

class PathInfo:
    def __init__(self, path="No path found", dist=-1, energy=-1):

        self.path = path
        self.dist = dist
        self.energy = energy


def load_json_files() -> Tuple[dict, dict, dict, dict]:
    with open("Coord.json", "r") as f:
        coord = json.load(f)
        f.close()

    with open("Cost.json", "r") as f:
        cost = json.load(f)
        f.close()

    with open("Dist.json", "r") as f:
        dist = json.load(f)
        f.close()

    with open("G.json", "r") as f:
        g = json.load(f)
        f.close()

    return coord, cost, dist, g


def calc_path_distance(path: list, dist: dict):
    dist_taken = 0

    for i in range(len(path) - 1):
        dist_taken += dist[f"{path[i]},{path[i+1]}"]

    return dist_taken


def calc_path_energy(path: list, cost: dict):
    energy_used = 0

    for i in range(len(path) - 1):
        energy_used += cost[f"{path[i]},{path[i+1]}"]

    return energy_used


def print_path(label: str, path_info: PathInfo):
    print(label)
    print(f"Shortest path: {path_info.path}")
    print(f"Shortest distance: {path_info.dist}")
    print(f"Total energy cost: {path_info.energy}\n")