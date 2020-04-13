data = 'abcdefghyutz'


# Time: O(n); Space: O(n)
def isUniqueChars(s: str) -> bool:
    if len(s) > 128:
        return False
    char_set = [False for _ in range(128)]
    for i in range(len(s)):
        index = ord(s[i])
        if char_set[index]:
            return False
        char_set[index] = True
    return True


# Time: O(n); Space: O(1)
def isUniqueChars(s: str) -> bool:
    if len(s) > 128:
        return False
    checker = 0
    for i in range(len(s)):
        index = ord(s[i]) - ord('a')
        if checker & (1 << index) > 0:
            return False
        checker |= (1 << index)
    return True

