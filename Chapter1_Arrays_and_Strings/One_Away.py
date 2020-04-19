
def one_edie_away(s1: str, s2: str) -> bool:
    if abs(len(s1) - len(s2)) > 1:
        return False

    one = s1 if len(s1) < len(s2) else s2
    two = s2 if len(s1) < len(s2) else s1
    index1, index2 = 0, 0
    diff = False
    while index1 < len(one) and index2 < len(two):
        if one[index1] != two[index2]:
            if diff:
                return False
            diff = True
            if len(one) == len(two):
                index1 += 1
        else:
            index1 += 1
        index2 += 1

    return True


