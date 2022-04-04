# Infinite Monkey Simulator
# Copyright (C) 2022 Hovhannes Muradyan

# Modules
import sys, random
import enchant # for dictionary

possibilities = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ",", "."]


def __main__() -> None:

    print("Starting infinite monkey simulator...")
    print(f"Python version: {sys.version[0:7]}")

    loop(True) 

def loop(condition: bool) -> None:
    queue = ""
    count = 0
    while condition:
        queue += random.choice(possibilities)
        if count > 100:
            print("Word found: ", check(queue))
            queue = ""
            count = 0
        count += 1


def check(string: str) -> str:
    # check for word in string
    d = enchant.Dict("en_US")
    for x in range(len(string)):
        count = len(string)
        print(x)
        print(count)
        while count > 0:
            print(string[x:count])
            if d.check(string[x:count]):
                return string[x:count]
            else:
                count -= 1
    return "No word found"

if __name__ == "__main__":
    __main__()