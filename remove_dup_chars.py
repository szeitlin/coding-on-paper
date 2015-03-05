__author__ = 'szeitlin'

def remove_dup_chars(word):
    """
    Remove duplicate chars without creating an entire additional copy of the array.

    (all duplicates, or only sequential duplicates?
    how do you handle multiple duplicates, i.e. 'aaaa'? does that become 'aa' or just 'a'?)

    :param word: str
    :return: str

    >>>remove_dup_chars('aab')
    'ab'
    >>>remove_dup_chars('abb')
    'ab'
    >>>remove_dup_chars('aabb')
    'ab'
    >>>remove_dup_chars('aabbaa')
    'aba'
    """


    marker = ''
    out = ''

    for char in word:
        if marker != char:
            marker = char
            out = out + char

    print out




remove_dup_chars('aab')
remove_dup_chars('abb')
remove_dup_chars('aabb')
remove_dup_chars('aabbaa')