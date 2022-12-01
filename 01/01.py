from itertools import takewhile

if __name__ == "__main__":
    with open("input.txt") as f:
        pointer = iter(f)
        elves = []
        while elf := list(takewhile(lambda s: s.strip(), pointer)):
            elves.append(elf)
    # print(max(sum(int(s.strip()) for s in elf) for elf in elves))
    print(sum(sorted((sum(int(s.strip()) for s in elf) for elf in elves), reverse=True)[:3]))
