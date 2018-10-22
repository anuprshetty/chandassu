from constant import Constant
import re
import copy


class Poem:
    _poem = ""
    _poem_kannada_symbols = []
    _poem_kannada_letters = []

    @classmethod
    def set_poem(cls, poem):
        cls._poem = poem

    @classmethod
    def cleanup(cls):
        if cls._poem == "":
            return

        cls._filter_kannada_symbols()
        cls._form_kannada_letters()

    @classmethod
    def letters(cls):
        return cls._poem_kannada_letters

    @classmethod
    def _filter_kannada_symbols(cls):
        poem = ""

        # remove all non-kannada unicode characters.
        for letter in cls._poem:
            letter_unicode = ord(letter)
            if (
                Constant.kannada_unicode_range.get("start")
                <= letter_unicode
                <= Constant.kannada_unicode_range.get("end")
                or letter == " "
                or letter == "\n"
            ):
                poem += letter

        poem = re.sub(r" +", " ", poem)  # replace multiple spaces with single space.
        poem = re.sub(r"\n+", "\n", poem)  # replace multiple '\n' with single '\n'.
        poem_lines = poem.split("\n")
        poem_lines = [
            poem_line.strip() for poem_line in poem_lines
        ]  # strip the left and right spaces in each line.
        poem_lines = [
            poem_line for poem_line in poem_lines if poem_line != ""
        ]  # remove empty lines.

        cls._poem_kannada_symbols = [list(poem_line) for poem_line in poem_lines]

