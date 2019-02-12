grid = [[0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0]]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def valid_neighbors(cell, grid, delta, g):
    neighbors = []
    for i in range(len(delta)):
        c1 = cell[0] + delta[i][0]
        c2 = cell[1] + delta[i][1]
        if 0 <= c1 < len(grid) and 0 <= c2 < len(grid[0]) and grid[c1][c2] != -1:
            neighbors.append([g, c1, c2])
    return neighbors


def show(grid):
    for i in range(len(grid)):
        print(grid[i])


def compute_plan(grid, goal, cost):
    path = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    closed = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                closed[row][col] = 0
    open_list = [[0] + goal]
    grid_pathing_complete = False

    while grid_pathing_complete is False:
        if len(open_list) != 0:
            for i in range(len(open_list)):
                if len(open_list) != 0:
                    # print(open_list)
                    i = 0
                    selected = open_list[i]
                    selected_cell = [selected[1], selected[2]]
                    g = selected[0]
                    open_list.pop(i)
                    neighbors = valid_neighbors(selected_cell, closed, delta, g + cost)
                    closed[selected_cell[0]][selected_cell[1]] = -1
                    for n in neighbors:
                        difference = [selected_cell[0]-n[1], selected_cell[1]-n[2]]
                        for d in range(len(delta)):
                            if difference == delta[d]:
                                path[n[1]][n[2]] = delta_name[d]
                        if n not in open_list:
                            open_list.append(n)
        else:
            grid_pathing_complete = True
    path[goal[0]][goal[1]] = '*'
    show(path)

    return path


def compute_value(grid, goal, cost):
    closed = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                value[row][col] = 0
                closed[row][col] = 0

    g = 0
    open_list = [[g] + goal]
    grid_evaluation_complete = False

    while grid_evaluation_complete is False:
        if len(open_list) != 0:
            for i in range(len(open_list)):
                if len(open_list) != 0:
                    i = 0
                    selected = open_list[i]
                    selected_cell = [selected[1], selected[2]]
                    g = selected[0]
                    open_list.pop(i)
                    value[selected_cell[0]][selected_cell[1]] = g
                    neighbors = valid_neighbors(selected_cell, closed, delta, g + cost)
                    closed[selected_cell[0]][selected_cell[1]] = -1
                    for n in neighbors:
                        if n not in open_list:
                            open_list.append(n)
        else:
            for row in range(len(value)):
                for col in range(len(value[0])):
                    if value[row][col] == 0:
                        value[row][col] = 99
            value[goal[0]][goal[1]] = 0
            grid_evaluation_complete = True
    show(value)

    return value


compute_value(grid, goal, cost)
compute_plan(grid, goal, cost)