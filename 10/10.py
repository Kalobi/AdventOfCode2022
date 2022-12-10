def apply_instructions(instrs, samples):
    x = 1
    cycle = 0
    signals = []
    for instr in instrs:
        cycle += 1
        if cycle in samples:
            signals.append(cycle*x)
        if instr:
            cycle += 1
            if cycle in samples:
                signals.append(cycle*x)
            x += instr
    return signals


def render(instrs, width, height):
    x = 1
    row = 0
    column = 0
    screen = [[" " for _ in range(width)] for _ in range(height)]

    def increment():
        nonlocal column
        nonlocal row
        column += 1
        if column >= width:
            column = 0
            row += 1
        if row >= height:
            row = 0

    def draw():
        screen[row][column] = "#" if x - 1 <= column <= x + 1 else "."

    for instr in instrs:
        draw()
        increment()
        if instr:
            draw()
            increment()
            x += instr
    return screen


if __name__ == '__main__':
    with open("input.txt") as f:
        instructions = [int(line.split()[1]) if line.startswith("addx") else None for line in f]
    print("\n".join("".join(row) for row in render(instructions, 40, 6)))
