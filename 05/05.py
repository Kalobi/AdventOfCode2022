from itertools import takewhile
from operator import methodcaller, itemgetter
import re


def create_stacks(text):
    return list(list(takewhile(methodcaller("isalpha"), stack))
                for stack in zip(*reversed([line[1::4] for line in text])))


def parse_instructions(text):
    return list(map(int, re.match(r"move (\d+) from (\d+) to (\d+)", line).group(1, 2, 3)) for line in text)


def apply(stacks, instr):
    steps, src, dst = instr
    for _ in range(steps):
        stacks[dst - 1].append(stacks[src - 1].pop())


def apply_modified(stacks, instr):
    steps, src, dst = instr
    stacks[dst - 1] += stacks[src - 1][-steps:]
    del stacks[src - 1][-steps:]


def apply_all(stacks, instrs):
    for instr in instrs:
        apply(stacks, instr)


def apply_all_modified(stacks, instrs):
    for instr in instrs:
        apply_modified(stacks, instr)


def tops(stacks):
    return "".join(map(itemgetter(-1), stacks))


if __name__ == '__main__':
    with open("input.txt") as f:
        stacks_text = list(takewhile(lambda line: "[" in line, f))
        next(f)
        instrs_text = list(line.strip() for line in f)
    stacks = create_stacks(stacks_text)
    instrs = parse_instructions(instrs_text)
    apply_all_modified(stacks, instrs)
    print(tops(stacks))
