from stats import word_count, char_count


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return f.read()


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    print(f"Found {num_words} total words")
    print(char_count(book_text))


if __name__ == "__main__":
    main()
