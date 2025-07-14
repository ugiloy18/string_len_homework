def main(s1,s2):
    """
    Given two strings, s1 and s2. Return the shortest length between them.
    Args:
        s1: string
        s2: string
    Returns:
        shortest string
    """
    return min(len(s1) , len(s2))
s1 = input("enter first string:") 
s2 = input("enter second string:")

print("shortest length:" 'main(s1 , s2')