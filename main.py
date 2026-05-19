##from stats import


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():
    num_words = word_count(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words")


if __name__ == "__main__":
    main()
