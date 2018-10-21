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

