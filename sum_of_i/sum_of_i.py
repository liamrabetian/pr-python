# not efficient 
def sum1(n):
    final_sum = 0
    for x in range(n+1):
        final_sum += x
    return final_sum


# much more efficient
# algo in jupyter file
def sum2(n):
    return n*(n+1)/2
