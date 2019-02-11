grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def show(grid):
    for i in range(len(grid)):
        print(grid[i])


def valid_neighbors(select, any_grid, delta, g, f):
    neighbors = []
    g += cost
    for i in range(len(delta)):
        c1 = select[0] + delta[i][0]
        c2 = select[1] + delta[i][1]
        if 0 <= c1 < len(any_grid) and 0 <= c2 < len(any_grid[0]) and any_grid[c1][c2] != 1:
            f = g + heuristic[c1][c2]
            neighbors.append([f, g, c1, c2])
    return neighbors


def path_neighbors(select, any_grid, delta, g):
    neighbors = []
    for i in range(len(delta)):
        c1 = select[0] + delta[i][0]
        c2 = select[1] + delta[i][1]
        if 0 <= c1 < len(any_grid) and 0 <= c2 < len(any_grid[0]) and any_grid[c1][c2] != 1:
            neighbors.append([g, c1, c2])
    return neighbors


def common_elements(list1, list2):
    return [element for element in list1 if element in list2]


def lowest_f(open_list):
    o = []
    for i in range(len(open_list)):
        o.append(open_list[i][0])
    return o.index(min(o))


def search(grid, init, goal, cost, heuristic):
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]   # Because closed = grid doesn't work
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    plan = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            closed[r][c] = grid[r][c]
    reached = False
    fail = False
    path = None
    selected_list = []
    plan_path = []
    f_value = 0 + heuristic[init[0]][init[1]]
    e = 0
    open_list = [[f_value] + [0] + init]

    while reached is False and fail is False:
        if len(open_list) == 0:
            fail = True
            print('failed')
        else:
            for i in range(len(open_list)):
                i = lowest_f(open_list)                         # chooses the open_list element with the lowest f-value
                selected = open_list[i]
                selected_cell = [selected[2], selected[3]]
                f_curr = selected[0]
                g_curr = selected[1]
                selected_list.append([selected[1], selected[2], selected[3]])
                selected_list.sort()
                selected_list.reverse()
                expand[selected[2]][selected[3]] = e
                e += 1
                if selected_cell == goal:
                    reached = True
                    path = selected_list[0]
                    # print(selected_list)
                    plan_path.append(selected_list[0])
                    for p in plan_path:
                        if p[1] == 0:
                            break
                        coord = path_neighbors([p[1], p[2]], grid, delta, p[0]-1)
                        chosen = common_elements(coord, selected_list)
                        plan_path.append(chosen[0])
                    for j in range(len(plan_path)):
                        if plan_path[j][0] <= 0:
                            break
                        difference = [plan_path[j][1]-plan_path[j+1][1], plan_path[j][2]-plan_path[j+1][2]]
                        for d in range(len(delta)):
                            if difference == delta[d]:
                                plan[plan_path[j+1][1]][plan_path[j+1][2]] = delta_name[d]
                        plan[goal[0]][goal[1]] = '*'
                    print('\nPath to goal:')
                    show(plan)
                    print('\nExpanded list:')
                    show(expand)
                    break
                else:
                    open_list.pop(i)
                    closed[selected_cell[0]][selected_cell[1]] = 1
                    neighbors = valid_neighbors(selected_cell, closed, delta, g_curr, f_curr)
                    for n in neighbors:
                        if n not in open_list:
                            open_list.append(n)
    return path


print('\n', search(grid, init, goal, cost, heuristic))
