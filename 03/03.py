def priority(c):
    return ord(c) - ord("a" if c.islower() else "A") + (27 if c.isupper() else 1)


def common_between_halves(raw_lines):
    return sum(priority((set((line := raw_line.strip())[:len(line)//2]) & set(line[len(line)//2:])).pop())
               for raw_line in f)


def common_between_three_rows(raw_lines):
    total = 0
    try:
        while True:
            total += priority((set(next(raw_lines)) & set(next(raw_lines)) & set(next(raw_lines)) - {'\n'}).pop())
    except StopIteration:
        return total


if __name__ == "__main__":
    with open("input.txt") as f:
        # print(common_between_halves(f))
        print(common_between_three_rows(f))
