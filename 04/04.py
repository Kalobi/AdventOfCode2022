def contained(a, b):
    return a[0] <= b[0] and a[1] >= b[1] or a[0] >= b[0] and a[1] <= b[1]


def overlap(a, b):
    return a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]


if __name__ == '__main__':
    with open("input.txt") as f:
        print(sum(1 for a, b in ((tuple(int(i) for i in ends.split("-")) for ends in line.strip().split(",")) for line in f) if overlap(a, b)))
