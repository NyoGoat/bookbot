def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = len(text.split())


    return print(f"{wordcount} words found in the document")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()