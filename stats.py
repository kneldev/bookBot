from typing import TypedDict


class CharacterCount(TypedDict):
    char: str
    num: int


def word_count(string: str) -> int:
    return len(string.split())


def char_count(string: str) -> dict[str, int]:
    character_count = {}
    string = string.lower()

    for letter in string:
        if letter in character_count:
            character_count[letter] += 1
        else:
            character_count[letter] = 1

    return character_count
