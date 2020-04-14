from collections import defaultdict


def permutation(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count_s = defaultdict(int)
    for word in s:
        count_s[word] += 1

    for word in t:
        count_s[word] -= 1
        if count_s.get(word) < 0:
            return False
    return True

