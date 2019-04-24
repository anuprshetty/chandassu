from ..chandassu import ChandassuTypes


class ChandassuIdentifier:
    def __init__(self, poem_letters, prastara_symbol, prastara_value):
        self._poem_letters = poem_letters
        self._prastara_symbol = prastara_symbol
        self._prastara_value = prastara_value

        self._chandassu_type = None

    def chandassu_type(self):
        return self._chandassu_type

    def identify(self):
        for ChandassuType in ChandassuTypes:
            chandassu_type = ChandassuType(
                self._poem_letters, self._prastara_symbol, self._prastara_value
            )

            if chandassu_type.identified():
                self._chandassu_type = chandassu_type
                return
