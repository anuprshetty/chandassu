from .chandassu import Chandassu
from ..utils.constant import Constant


class Invalid(Chandassu):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("invalid")

    def identified(self):
        self._invalid = True

        self._form_ganas(
            first_alternative_matras_count=-1, second_alternative_matras_count=-1
        )

        return True
