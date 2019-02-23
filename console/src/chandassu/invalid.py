from .chandassu import Chandassu
from ..utils.constant import Constant


class Invalid(Chandassu):
    _name = Constant.chandassu_names.get("invalid")

    @classmethod
    def identified(cls):
        cls._form_ganas(
            first_alternative_matras_count=-1, second_alternative_matras_count=-1
        )
        return True
