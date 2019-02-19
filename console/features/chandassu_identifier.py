from chandassu import chandassu_types


class ChandassuIdentifier:
    _poem_letters = []
    _prastara_symbol = []
    _prastara_value = []
    _chandassu_type = None

    @classmethod
    def set_poem_letters(cls, poem_letters):
        cls._poem_letters = poem_letters

    @classmethod
    def set_prastara_symbol(cls, prastara_symbol):
        cls._prastara_symbol = prastara_symbol

    @classmethod
    def set_prastara_value(cls, prastara_value):
        cls._prastara_value = prastara_value

    @classmethod
    def chandassu_type(cls):
        return cls._chandassu_type

    @classmethod
    def identify(cls):
        for chandassu_type in chandassu_types:
            chandassu_type.set_poem_letters(cls._poem_letters)
            chandassu_type.set_prastara_symbol(cls._prastara_symbol)
            chandassu_type.set_prastara_value(cls._prastara_value)

            if chandassu_type.identified():
                cls._chandassu_type = chandassu_type
                return
