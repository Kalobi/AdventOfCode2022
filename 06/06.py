def find_marker(stream, distinct):
    chars = [""] + list(stream[:distinct - 1])
    for i, c in enumerate(stream[distinct - 1:]):
        del chars[0]
        chars.append(c)
        if len(set(chars)) == len(chars):
            return i + distinct


if __name__ == '__main__':
    with open("input.txt") as f:
        print(find_marker(f.read(), 14))
