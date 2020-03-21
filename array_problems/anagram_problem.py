"""
These are some solutions to anagram problem.
The question is: 
Given two strings, check to see if they are anagrams. 
An anagram is when the two strings can be written using the exact same letters 
(so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies"

"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".
"""


# Solution 1
def anagram_1(string_1, string_2):
    """Easy simple solution, but python specefic!
    
    Arguments:
        string_1 {[AnyStr]} -- [First String]
        string_2 {[AnyStr]} -- [Second String To Be Compared With First]
    
    Returns:
        [Boolean] -- [If True, Then Anagram!]
    """
    # remove white spaces
    import re

    string_1 = re.sub(r"\s+", "", string_1).lower()
    string_2 = re.sub(r"\s+", "", string_2).lower()

    return sorted(string_1) == sorted(string_2)


def anagram_2(string_1, string_2):
    """
    This solution isn't python specefic.
    Use one HashTable to add counts for each letter,
    and use another to subtract each letter!
    """
    # remove white spaces
    import re

    string_1 = re.sub(r"\s+", "", string_1).lower()
    string_2 = re.sub(r"\s+", "", string_2).lower()

    if len(string_1) != len(string_2):
        return False

    counter = {}
    for letter in string_1:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

    for letter in string_2:
        if letter in counter:
            counter[letter] -= 1
        else:
            counter[letter] = 1

    for key in counter:
        if counter[key] != 0:
            return False

    return True


def anagram_3(string_1, string_2):
    """
    Just like anagram_2, but python specefic
    and much more cleaner.
    """

    # remove white spaces
    import re

    string_1 = re.sub(r"\s+", "", string_1).lower()
    string_2 = re.sub(r"\s+", "", string_2).lower()

    from collections import defaultdict

    dic = defaultdict(int)

    if not len(string_1) == len(string_2):
        return False

    for letter in string_1:
        dic[letter] += 1

    for letter in string_2:
        dic[letter] -= 1

    for key in dic:
        if not dic[key] == 0:
            return False

    return True


if __name__ == "__main__":
    # Test all methods
    strings = (
        ("clint eastwood", "o  ld weSt A ction"),
        ("public relations", "crap built on lies"),
        ("not anagram", "it's not and anagram!"),
    )
    for item in strings:
        print(anagram_1(item[0], item[1]))
        print(anagram_2(item[0], item[1]))
        print(anagram_3(item[0], item[1]))
