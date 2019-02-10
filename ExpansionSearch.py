grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]]

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

def valid_neighbors(select, closed,  delta, g):
    neighbors = []
    for i in range(len(delta)):
        c1 = select[0] + delta[i][0]
        c2 = select[1] + delta[i][1]
        if 0 <= c1 < len(closed) and 0 <= c2 < len(closed[0]) and closed[c1][c2] != 1:
                neighbors.append([g, c1, c2])
    return neighbors

def common_elements(list1, list2):
    return [element for element in list1 if element in list2]


def search(grid, init, goal, cost):
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]           # Because closed = grid doesn't work properly
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    plan = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            closed[r][c] = grid[r][c]
    reached = False
    fail = False
    path = None
    selected_list = []
    plan_path = []
    e = 0
    open_list = [[0] + init]

    while reached is False and fail is False:
        if len(open_list) == 0:
            fail = True
            print('failed')
        else:
            for i in range(len(open_list)):
                i = 0
                selected = open_list[i]
                selected_cell = [selected[1], selected[2]]
                selected_list.append(selected)
                selected_list.sort()
                selected_list.reverse()
                # expand[selected[1]][selected[2]] = e
                # e += 1
                if selected_cell == goal:
                    reached = True
                    path = selected
                    plan_path.append(selected_list[0])
                    for p in plan_path:
                        if p[0] == 0:
                            break
                        coord = valid_neighbors([p[1], p[2]], grid, delta, p[0]-1)
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
                    show(plan)
                    break
                else:
                    open_list.pop(i)
                    closed[selected_cell[0]][selected_cell[1]] = 1
                    neighbors = valid_neighbors(selected_cell, closed, delta, (selected[0] + cost))
                    for n in neighbors:
                        if n not in open_list:
                            open_list.append(n)
    return path


print(search(grid, init, goal, cost))
