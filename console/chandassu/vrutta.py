from .chandassu import Chandassu
from constant import Constant


class Vrutta(Chandassu):
    _name = Constant.chandassu_names.get("vrutta").get("vrutta")
    _total_lines = 4

    _line_pattern = None

    @classmethod
    def identified(cls):
        if len(cls._prastara_values) == 0:
            return False

        if cls._line_pattern == None:
            return False

        if len(cls._prastara_values) == cls._total_lines:
            for prastara_line in cls._prastara_values:
                prastara_line_pattern = "".join(str(value) for value in prastara_line)
                if prastara_line_pattern != cls._line_pattern:
                    return False

            cls._form_ganas()
            return True
        else:
            return False

