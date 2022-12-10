from math import copysign
from itertools import starmap, pairwise


def follow(head, tail):
    if tail[0] == head[0] and abs(tail[1] - head[1]) >= 2:
        new_tail = (tail[0], int(tail[1] + copysign(1, head[1] - tail[1])))
    elif tail[1] == head[1] and abs(tail[0] - head[0]) >= 2:
        new_tail = (int(tail[0] + copysign(1, head[0] - tail[0])), tail[1])
    elif abs(tail[0] - head[0]) + abs(tail[1] - head[1]) >= 3:
        new_tail = (int(tail[0] + copysign(1, head[0] - tail[0])), int(tail[1] + copysign(1, head[1] - tail[1])))
    else:
        new_tail = tail
    return new_tail


def apply_move(head, tails, direction):
    match direction:
        case "U":
            new_head = (head[0], head[1] - 1)
        case "D":
            new_head = (head[0], head[1] + 1)
        case "L":
            new_head = (head[0] - 1, head[1])
        case "R":
            new_head = (head[0] + 1, head[1])
        case _:
            raise ValueError
    new_tails = [follow(new_head, tails[0])]
    for tail in tails[1:]:
        new_tails.append(follow(new_tails[-1], tail))
    # new_tails = (follow(new_head, tails[0]), *(starmap(follow, pairwise(tails))))
    return new_head, new_tails


def visualize(head, tails, height, width):
    print("\n".join("".join("H" if head == (x, y) else str(tails.index((x, y)) + 1) if (x, y) in tails else "."
                            for x in range(width))
                    for y in range(height)))


def tail_positions_list(head, tails, moves):
    positions = [tails[-1]]
    for direction, count in moves:
        for _ in range(count):
            head, tails = apply_move(head, tails, direction)
            positions.append(tails[-1])
            # visualize(head, tails, 21, 26)
    return positions


if __name__ == '__main__':
    with open("input.txt") as f:
        moves = [(d, int(steps)) for d, steps in (line.split() for line in f)]
    head = (11, 15)
    tails = [(11, 15)]*9
    print(len(set(tail_positions_list(head, tails, moves))))

