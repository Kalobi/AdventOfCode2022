from itertools import chain, product, takewhile


def visibility_map_directional(grid):
    result_grid = []
    for row in grid:
        threshold = -1
        result_row = []
        for tree in row:
            if tree > threshold:
                result_row.append(True)
                threshold = tree
            else:
                result_row.append(False)
        result_grid.append(result_row)
    return result_grid


def visibility_count(grid):
    left = visibility_map_directional(grid)
    right = [list(reversed(line)) for line in visibility_map_directional(reversed(line) for line in grid)]
    top = list(zip(*visibility_map_directional(zip(*grid))))
    bottom = list(reversed(list(zip(*visibility_map_directional(zip(*reversed(grid)))))))
    return count_all_true(left, right, top, bottom)


def scenic_scores(grid):
    result_grid = []
    for i, row in enumerate(grid):
        result_row = []
        for j, tree in enumerate(row):
            up = 0
            for i_up in range(i-1, -1, -1):
                up += 1
                if grid[i_up][j] >= tree:
                    break
            down = 0
            for i_down in range(i+1, len(grid)):
                down += 1
                if grid[i_down][j] >= tree:
                    break
            left = 0
            for j_left in range(j-1, -1, -1):
                left += 1
                if grid[i][j_left] >= tree:
                    break
            right = 0
            for j_right in range(j+1, len(grid[i])):
                right += 1
                if grid[i][j_right] >= tree:
                    break
            result_row.append(up*down*left*right)
        result_grid.append(result_row)
    return result_grid


def count_all_true(*grids):
    return sum(any(tree) for tree in zip(*(chain.from_iterable(grid) for grid in grids)))


if __name__ == '__main__':
    with open("input.txt") as f:
        grid = [[int(c) for c in line.strip()] for line in f]
    print(visibility_count(grid))
    print(max(chain.from_iterable(scenic_scores(grid))))
