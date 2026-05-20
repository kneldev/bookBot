from stats import list_the_dicts, word_count, char_count


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return f.read()


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    character_counts = char_count(book_text)
    sorted_counts = list_the_dicts(character_counts)
    print(f"Found {num_words} total words")
    print(sorted_counts)


if __name__ == "__main__":
    main()
