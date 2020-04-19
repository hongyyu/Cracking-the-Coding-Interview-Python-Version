from collections import defaultdict


def is_permutation_palindrome(s: str) -> bool:
    counter = 0
    mapping = defaultdict(int)
    for char in s:
        if char == ' ':
            continue
        mapping[char] += 1
        if mapping.get(char) % 2 == 1:
            counter += 1
        else:
            counter -= 1

    return counter <= 1

s = 'tact coa'
