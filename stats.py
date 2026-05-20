from typing import TypedDict


class CharacterCount(TypedDict):
    char: str
    num: int


def sort_on(character_count: CharacterCount) -> int:
    return character_count["num"]


def list_the_dicts(main_dict: dict[str, int]) -> list[CharacterCount]:
    # Convert the raw frequency map into a sortable list and drop non-letter characters.
    list_dicts = []

    for entry in main_dict:
        if entry.isalpha():
            list_dicts.append({"char": entry, "num": main_dict[entry]})
    list_dicts.sort(reverse=True, key=sort_on)
    return list_dicts


def word_count(string: str) -> int:
    return len(string.split())


def char_count(string: str) -> dict[str, int]:
    character_count = {}
    # Normalize case so uppercase and lowercase letters are counted together.
    string = string.lower()

    for letter in string:
        if letter in character_count:
            character_count[letter] += 1
        else:
            character_count[letter] = 1

    return character_count
