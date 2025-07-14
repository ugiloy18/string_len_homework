def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    length = len(s)
    mid = length // 2
    if length % 2 == 0:
        return s[mid - 1:mid + 1]
    else:
        return s[mid]
print(main("abcde")) 
print(main("abcdef"))