def score(opponent, you):
    opponent = chr(ord(opponent) + ord("X") - ord("A"))
    match you:
        case "X":  # rock
            shape = 1
        case "Y":  # paper
            shape = 2
        case "Z":  # scissors
            shape = 3
        case _:
            raise ValueError
    if opponent == you:
        outcome = 3
    else:
        if (opponent, you) in {("X", "Y"), ("Y", "Z"), ("Z", "X")}:
            outcome = 6
        else:
            outcome = 0
    return shape + outcome


def rpsshift(shape, shift):
    return chr((ord(shape) - ord("X") + shift) % 3 + ord("X"))


def choice(opponent, result):
    opponent = chr(ord(opponent) + ord("X") - ord("A"))
    match result:
        case "Y":
            return opponent
        case "X":
            return rpsshift(opponent, 2)
        case "Z":
            return rpsshift(opponent, 1)
    raise ValueError


if __name__ == "__main__":
    with open("input.txt") as f:
        pairs = [line.strip().split(" ") for line in f]
    # print(sum(score(*pair) for pair in pairs))
    print(sum(score(opponent, choice(opponent, instruction)) for opponent, instruction in pairs))
