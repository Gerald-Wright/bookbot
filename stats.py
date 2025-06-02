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

def get_num_words(content):
    """
    return the word count from the contents
    """
    return len(content.split())

def get_sort_list_of_dict(original_dict, is_reverse = True):
    """
    takes a single dictionary passed in,
    breaks it into a list of dictionaries,
    and sorts it in ascending order by value
    """
    list_of_dict = []
    
    for key, value in original_dict.items():
        list_of_dict.append({"char": key, "count": value})
    
    sorted_list = sorted(list_of_dict, key = lambda item: item["count"], reverse = is_reverse)
    return sorted_list

