from itertools import combinations

def ncomb(items, n):
    return list(combinations(items, n))

def totalvalue(comb):
    weight = value = 0
    for _, w, v in comb:
        weight += w
        value  += v
    return (value, -weight)

def multimax(list, key):
    "Return all maximum values in the list given a key"

    if len(list) == 0:
        return []

    # Sort the list with highest values towards the top
    s = sorted(list, key=key, reverse=True)

    # The first item is already part of the maximum
    res = [s[0]]
    # The highest key is equal to the key of the first item
    max = key(s[0])

    # Loop from 0 to len(s) while key(s[i]) is still equal to the highest key
    i = 1
    while i < len(s) and key(s[i]) == max:
        res.append(s[i])
        i += 1
    return res


def knapsack(items, bagsize):
    return multimax(ncomb(items, vagsize), key=totalvalue)