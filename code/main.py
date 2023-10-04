import helper
import task1
import task2
import task3

ENERGY_BUDGET = 287932


def main():
    coord, cost, dist, g = helper.load_json_files()

    # run_task_1_BFS(cost, dist, g)
    # run_task_1_DFS(cost, dist, g)
    run_task_1_UCS(cost, dist, g)

    # run_task_2_BFS(cost, dist, g)
    # run_task_2_DFS(cost, dist, g)
    run_task_2_UCS(cost, dist, g)
    # run_task_2_dij(cost, dist, g)

    run_task_3_astar(coord, cost, dist, g)


def run_task_2_dij(cost, dist, g):
    path2_dij = task2.dijkstra_with_energy(g, "1", "50", cost, dist, ENERGY_BUDGET)
    helper.print_path("Task 2 Dijkstra", path2_dij)


def run_task_1_BFS(cost, dist, g):
    path1_bfs = task1.bfs(g, "1", "50", cost, dist)
    helper.print_path("Task 1 BFS", path1_bfs)


def run_task_1_DFS(cost, dist, g):
    path1_dfs = task1.dfs(g, "1", "50", cost, dist)
    helper.print_path("Task 1 DFS", path1_dfs)


def run_task_1_UCS(cost, dist, g):
    path1_ucs = task1.ucs(g, "1", "50", cost, dist)
    helper.print_path("Task 1 UCS", path1_ucs)


def run_task_2_BFS(cost, dist, g):
    path2_bfs = task2.bfs(g, "1", "50", ENERGY_BUDGET, cost, dist)
    helper.print_path("Task 2 BFS", path2_bfs)


def run_task_2_DFS(cost, dist, g):
    path2_dfs = task2.dfs(g, "1", "50", ENERGY_BUDGET, cost, dist)
    helper.print_path("Task 2 DFS", path2_dfs)


def run_task_2_UCS(cost, dist, g):
    path2_ucs = task2.ucs(g, "1", "50", ENERGY_BUDGET, cost, dist)
    helper.print_path("Task 2 UCS", path2_ucs)


def run_task_3_astar(coord, cost, dist, g):
    path3_astar = task3.astar(g, "1", "50", ENERGY_BUDGET, cost, dist, coord, 1)
    helper.print_path("Task 3 AStar", path3_astar)


if __name__ == "__main__":
    main()
