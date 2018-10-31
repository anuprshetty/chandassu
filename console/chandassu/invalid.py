from .chandassu import Chandassu
from constant import Constant


class Invalid(Chandassu):
    _name = Constant.chandassu_names.get("invalid")

    @classmethod
    def identified(cls):
        return True
