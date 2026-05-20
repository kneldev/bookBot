import sys
from stats import CharacterCount, list_the_dicts, word_count, char_count


def input_handler():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        return book_path


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return f.read()


def format_output(sorted_counts: list[CharacterCount]) -> None:
    for item in sorted_counts:
        print(f"{item['char']}: {item['num']}")


def main():
    book_path = input_handler()
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    character_counts = char_count(book_text)
    sorted_counts = list_the_dicts(character_counts)
    print(f"Found {num_words} total words")
    format_output(sorted_counts)


if __name__ == "__main__":
    main()
