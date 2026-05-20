from stats import list_the_dicts, word_count, char_count


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return f.read()


def format_output(sorted_counts):
    for item in sorted_counts:
        print(f"{item['char']}: {item['num']}")


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    character_counts = char_count(book_text)
    sorted_counts = list_the_dicts(character_counts)
    print(f"Found {num_words} total words")
    format_output(sorted_counts)


if __name__ == "__main__":
    main()
