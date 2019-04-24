from ..utils.constant import Constant
import re
import copy


class Poem:
    def __init__(self, poem):
        self._poem = poem

        self._poem_kannada_symbols = []
        self._poem_kannada_letters = []

    def cleanup(self):
        if self._poem == "":
            return

        self._filter_kannada_symbols()
        self._form_kannada_letters()

    def letters(self):
        return self._poem_kannada_letters

    def _filter_kannada_symbols(self):
        poem = ""

        # remove all non-kannada unicode characters.
        for letter in self._poem:
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

        self._poem_kannada_symbols = [list(poem_line) for poem_line in poem_lines]

    def _form_kannada_letters(self):
        poem_letters = copy.deepcopy(self._poem_kannada_symbols)

        halant = Constant.kannada_symbols.get("halant")
        alphabets = Constant.kannada_symbols.get("alphabets")

        lines_count = len(poem_letters)
        i = 0
        while i < lines_count:
            letters_count = len(poem_letters[i])
            j = 0
            while j < letters_count:
                if poem_letters[i][j] == halant:
                    if j + 1 == letters_count or poem_letters[i][j + 1] == " ":
                        poem_letters[i][j - 1 : j + 1] = [
                            "".join(poem_letters[i][j - 1 : j + 1])
                        ]  # Ex: 'ಳ' + '್' = 'ಳ್'
                        letters_count = letters_count - 1
                    else:
                        poem_letters[i][j - 1 : j + 2] = [
                            "".join(poem_letters[i][j - 1 : j + 2])
                        ]  # Ex: 'ಳ' + '್' + 'ದ' = 'ಳ್ದ'
                        letters_count = letters_count - 2
                elif poem_letters[i][j] in alphabets:
                    poem_letters[i][j - 1 : j + 1] = [
                        "".join(poem_letters[i][j - 1 : j + 1])
                    ]  # Ex: 'ಷ' + ''ಂ' = 'ಷಂ'
                    letters_count = letters_count - 1
                else:
                    j = j + 1

            i = i + 1

        self._poem_kannada_letters = poem_letters
