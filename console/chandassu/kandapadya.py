from .chandassu import Chandassu
from constant import Constant


class Kandapadya(Chandassu):
    _name = Constant.chandassu_names.get("kandapadya")

    _total_lines = 4

    _first_long_line_index = 1
    _last_long_line_index = 3

    _total_ganas_per_short_line = 3
    _total_ganas_per_long_line = 5

    _matras_count = 4

    _gana_should_not_occur = "121"

    @classmethod
    def identified(cls):
        if len(cls._prastara_values) == 0:
            return False

        if len(cls._prastara_values) != cls._total_lines:
            return False

        if (
            sum(cls._prastara_values[0]) != 12
            or sum(cls._prastara_values[2]) != 12
            or sum(cls._prastara_values[1]) != 20
            or sum(cls._prastara_values[3]) != 20
        ):
            return False

        if not cls._pattern_matched(
            cls._total_ganas_per_short_line,
            cls._total_ganas_per_long_line,
            cls._matras_count,
            cls._matras_count,
            cls._first_long_line_index,
            cls._last_long_line_index,
            has_extra_guru=False,
        ):
            return False

        if cls._special_conditions_met():
            cls._form_ganas(cls._matras_count, cls._matras_count)

            return True
        else:
            return False

