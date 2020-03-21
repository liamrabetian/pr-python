"""Reverse the given string sentence:
Ex: This is a sentence -> sentence a is This
"""

def reverse_1(string):
    string = string.strip()
    string_list = string.split()

    reversed_list = list()
    for reverse_index in range((len(string_list) - 1), -1, -1):
        reversed_list.append(string_list[reverse_index])
    
    return ' '.join(reversed_list)


def reverse_4(string):
    string = string.strip().split()
    reversed_list = list()

    while string:
        reversed_list.append(string.pop())
    
    return ' '.join(reversed_list)


def reverse_2(string):
    return ' '.join(reversed(string.strip().split()))


def reverse_3(string):
    return ' '.join(string.strip().split()[::-1])


if __name__ == "__main__":
    print(reverse_1('This is a test string'))
    print(reverse_2('This is a test string'))
    print(reverse_3('This is a test string'))
    print(reverse_4('This is a test string'))
