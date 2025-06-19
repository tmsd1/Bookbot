import string
import sys
from stats import get_num_words, count_characters, sort_on
import sys

def main():
        if len(sys.argv) < 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        else:
            text = get_book_text(sys.argv[1])
            print("\n============ BOOKBOT ============\n")
            print("Analyzing book found at ...\n")


            num_words = get_num_words(text)
            print("----------- Word Count ----------\n")
            print(f"Found {num_words} total words\n")

            num_characters = count_characters(text)
            print("--------- Character Count -------\n")
            sort_on(num_characters)
            print("============= END ===============\n")

def get_book_text(filepath):
        with open(filepath, "r") as f:
            return f.read()

main()