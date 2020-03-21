"""The problem is:
Given an integer array, output all the unique pairs
In an array that sum up to a specific value k.

"""

def pair_sum(array, k):

    if len(array) < 2:
        return None
    
    seen = set()
    output = set()

    for num in array:
        target = k - num

        if not target in seen:
            seen.add(num)
        else:
            output.add((min(target, num), max(target, num)))
    
    return '\n'.join(map(str, output))


if __name__ == "__main__":
    print(pair_sum([1, 3, 2, 2], 4))
    print("----------------")
    print(pair_sum([1, 9, 2, 8, -1, 11, 13, 12], 10))