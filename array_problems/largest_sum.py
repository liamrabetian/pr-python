"""Given an array of integers, calculate the largest current sum
in the array.
"""


def largest_cur_sum_1(arr):
    if len(arr) == 0:
        return 0
    
    largest_sum = 0
    cur_sum = arr[0]

    for index in range(1, (len(arr))):
        cur_sum += arr[index]
        if cur_sum > largest_sum:
            largest_sum = cur_sum
    
    return largest_sum


def largest_cur_sum_2(arr):
    if len(arr) == 0:
        return 0
    
    largest_sum = cur_sum = arr[0]

    for num in arr[1:]:
        cur_sum = max(cur_sum+num, num)
        largest_sum = max(cur_sum, largest_sum)
    
    return largest_sum


if __name__ == "__main__":
    print(largest_cur_sum_1([1, 2, -1, 10, 10, -10, 20, -30, 2]))
    print(largest_cur_sum_2([1, 2, -1, 10, 10, -10, 20, -30, 2]))