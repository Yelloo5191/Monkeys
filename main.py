# Infinite Monkey Simulator
# Copyright (C) 2022 Hovhannes Muradyan

# Modules
import sys, random
import enchant # for dictionary
from enchant.tokenize import get_tokenizer

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
            if check(queue):
                print("Word found: ", check(queue))
            queue = ""
            count = 0
        count += 1


def check(string: str) -> str:
    # check for word in string
    tknzr = get_tokenizer("en_US")

    words_found = [x for x in tknzr(string) if enchant.request_pwl_dict("wordlist.txt").check(x[0])]
    
    if not words_found:
        return False
    else:
        return words_found

if __name__ == "__main__":
    __main__()