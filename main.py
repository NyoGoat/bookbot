from stats import get_num_words, get_let_count, sort_on, make_char_list
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        #print(f"Usage: python {sys.argv[0]} <input1> <input2> [optional_inputs...]")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    text = get_book_text(book_path)
    wordcount = get_num_words(text)
    chcount = get_let_count(text)
    sortedlist = make_char_list(chcount)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for item in sortedlist:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

    
#    return print(f"found {wordcount} total words in the document")#, print(chcount)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
