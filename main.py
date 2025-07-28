from stats import *
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book_name = sys.argv[1]
    print(f"Analyzing book found at {book_name}...")
    book_text = get_book_text(book_name)
    num_of_words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    char_list = sort_chr_dict(cnt_chr_dict(book_text.lower()))
    for char in char_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()
