from stats import get_num_words

def main():
    text = get_book_text("books/frankenstein.txt")
    if text != None:
        print(f"{get_num_words(text)} words found in the document")

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
    
if __name__ == "__main__":
    main()
    
