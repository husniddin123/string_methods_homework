def main(s):
    """
    A str of several words is given. All letters are lowercase. Make sure that the first letter of each word is capitalized.    A str of several words is given. All letters are lowercase. Make sure that the first letter of each word is capitalized.
    Args:
        s: str
    Returns:
        str: answer
    """
    
    answer = s.istitle()

    return answer

print(main("Helov A Emi")) 