"""The problem is:
Given two arrays, find the missing element from the array.
"""

# O(n^2)
def finder_1(arr_1, arr_2):
    missed = list()
    # O(n)
    for num in arr_1:
        if num in arr_2:
            # to handle duplicates in array
            # O(n)
            arr_2.remove(num)
        else:
            missed.append(num)
    return ', '.join(map(str, missed))


# O(nlogn)
# only one missed element
def finder_2(arr_1, arr_2):
    arr_1.sort()
    arr_2.sort()

    for num_1, num_2 in zip(arr_1, arr_2):
        if num_1 != num_2:
            return num_1
    return arr_1[-1]


# O(n)
def finder_3(arr_1, arr_2):
    from collections import defaultdict

    d = defaultdict(int)

    for num in arr_2:
        d[num] += 1
    
    missed = list()
    for num in arr_1:
        if d[num] == 0:
            missed.append(num) 
        else:
            d[num] -= 1
    return ', '.join(map(str, missed))


# O(n)
# smart, but only works if one is missed
def finder_4(arr_1, arr_2):
    result = 0
    for num in arr_1 + arr_2:
        result ^= num
    return result


# programmatically correct but a lot of problems can occure!
def finder_5(arr_1, arr_2):
    arr_1 = sum(arr_1)
    arr_2 = sum(arr_2)

    return arr_1 - arr_2
    


if __name__ == "__main__":
    arr_1, arr_2 = [1, 2, 3, 4, 5, 6, 7, 7, 12], [3, 1, 4, 12, 7, 5]
    arr_3, arr_4 = [1, 2, 3, 4, 5, 5], [3, 1, 5, 4]
    arr_5, arr_6 = [1, 2, 3, 4], [3, 2, 4]
    print(finder_1(arr_1, arr_2))
    print("---------------------")
    print(finder_2(arr_3, arr_4))
    print("---------------------")
    print(finder_3(arr_3, arr_4))
    print("---------------------")
    print(finder_4(arr_5, arr_6))
    print("---------------------")
    print(finder_5(arr_5, arr_6))
