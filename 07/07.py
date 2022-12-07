from typing import Optional
from functools import cache
from operator import methodcaller


class Directory:
    def __init__(self, name: str, parent: Optional["Directory"]):
        self.name = name
        self.parent: Optional["Directory"] = parent
        self.children: dict[str, Directory] = {}
        self.files = {}

    def add_child(self, name: str) -> "Directory":
        new_dir = Directory(name, self)
        self.children[name] = new_dir
        return new_dir

    def add_file(self, name: str, size: int):
        self.files[name] = size

    @cache
    def size(self) -> int:
        return sum(self.files.values()) + sum(d.size() for d in self.children.values())

    def __str__(self):
        return f"{self.name}, parent {self.parent.name if self.parent else 'None'}, {len(self.children)} children, {len(self.files)} files"


def process_command(current_dir: Optional[Directory], command_block: str, all_dirs: set[Directory]) -> Directory:
    lines = command_block.splitlines()
    command = lines[0].split()
    match command[0]:
        case "cd":
            if command[1] == "..":
                return current_dir.parent
            else:
                if current_dir is None:
                    root = Directory(command[1], None)
                    all_dirs.add(root)
                    return root
                return current_dir.children[command[1]]
        case "ls":
            for line in lines[1:]:
                size_or_type, name = line.split()
                if size_or_type == "dir":
                    all_dirs.add(current_dir.add_child(name))
                else:
                    current_dir.add_file(name, int(size_or_type))
            return current_dir
        case _:
            raise ValueError("invalid command")


if __name__ == '__main__':
    with open("input.txt") as f:
        commands = f.read().split("$ ")[1:]
    current_dir = None
    all_dirs = set()
    for command in commands:
        current_dir = process_command(current_dir, command, all_dirs)
    while current_dir.name != "/":
        current_dir = current_dir.parent
    free_space = 70000000 - current_dir.size()
    # print(sum(d.size() for d in all_dirs if d.size() <= 100000))
    print(min(filter(lambda d: d.size() >= 30000000 - free_space, all_dirs), key=methodcaller("size")).size())
