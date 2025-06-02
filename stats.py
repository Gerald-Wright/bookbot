def get_num_words(content):
    """
    return the word count from the contents
    """
    return len(content.split())

def get_char_count(content):
    """
    return a dictionary that contains each character and the number of times
    is occurs inside content
    ex:  {'p': 6121, 'r': 20818, 'o': 25225, ...
    """

    char_count = {}
    lower_content = content.lower()

    for char in lower_content:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count
