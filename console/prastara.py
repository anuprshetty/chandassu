from constant import Constant


class Prastara:
    _poem_letters = []
    _prastara_symbol = []
    _prastara_value = []

    @classmethod
    def set_poem_letters(cls, poem_letters):
        cls._poem_letters = poem_letters

    @classmethod
    def poem_prastara_symbol(cls):
        return cls._prastara_symbol

    @classmethod
    def poem_prastara_value(cls):
        return cls._prastara_value

    @classmethod
    def identify(cls):
        if len(cls._poem_letters) == 0:
            return

        cls._form_prastara_value()
        cls._form_prastara_symbol()
        cls._remove_space_value_from_prastara_value()

