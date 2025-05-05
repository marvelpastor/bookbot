import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import (
    count_words,
    count_char,
    sorted,
)

def get_book_text (path):
    with open(path) as f:
        text = f.read()
        return text

def print_report (a,b,c):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {a}")
    print("----------- Word Count ----------")
    print(f"Found {b} total words")
    print("--------- Character Count -------")
    for item in c:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
        else:
            continue
    print("============= END ===============")

def main (path):
    text = get_book_text(path)
    total_words = count_words(text)
    total_chars = count_char(text)
    sorted_chars = sorted(total_chars)
    print_report (path,total_words,sorted_chars)
    

main (sys.argv[1])