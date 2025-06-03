import stats
import sys

def main():
    """
    read the book
    calc word count
    create dict of char counts
    convert dict into sorted list of dicts
    build report
    """
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_file = sys.argv[1]
    text = get_book_text(book_file)
    if text != None:
        num_words = stats.get_num_words(text) 
        unsorted_char_dict = stats.get_char_count(text)
        sorted_char_list = stats.get_sort_list_of_dict(unsorted_char_dict)
        print_report(book_file, num_words, sorted_char_list, False)

def get_book_text(path_to_file):
    """
    return the text found in a file
    """    
    file_contents = None
    try:
        with open(path_to_file) as textfile:
            file_contents = textfile.read()
    except FileNotFoundError:
        print(f"The file '{path_to_file}' was not found!", )
    except:
        print("something else went wrong")

    return file_contents
    
def print_report(book_path, num_words, sorted_list, include_nonalpha = True):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
   
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
   
    print("--------- Character Count -------")
    for item in sorted_list:
        if (item['char'].isalpha() or include_nonalpha):
            print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
    
