from .chandassu import Chandassu
from constant import Constant


class Shatpadi(Chandassu):
    _name = Constant.chandassu_names.get("shatpadi").get("shatpadi")
    _total_lines = 6

    _first_long_line_index = 2
    _last_long_line_index = 5

    _total_ganas_per_short_line = None
    _total_ganas_per_long_line = None

    _first_alternative_matras_count = None
    _second_alternative_matras_count = None

    _gana_should_not_occur_1 = None
    _gana_should_not_occur_2 = None

    @classmethod
    def identified(cls):
        if len(cls._prastara_values) == 0:
            return False

        if (
            cls._total_ganas_per_short_line == None
            or cls._total_ganas_per_long_line == None
            or cls._first_alternative_matras_count == None
            or cls._second_alternative_matras_count == None
            or cls._gana_should_not_occur_1 == None
            or cls._gana_should_not_occur_2 == None
        ):
            return False

        if len(cls._prastara_values) != cls._total_lines:
            return False

        GURU_VALUE = Constant.prastara_info.get("guru").get("value")
        cls._prastara_values[cls._first_long_line_index][-1] = GURU_VALUE
        cls._prastara_values[cls._last_long_line_index][-1] = GURU_VALUE

        for line_index in range(0, len(cls._prastara_values)):
            prastara_line = cls._prastara_values[line_index]

            if line_index == 2 or line_index == 5:
                total_matras_per_line = (cls._total_ganas_per_long_line / 2) * (
                    cls._first_alternative_matras_count
                    + cls._second_alternative_matras_count
                ) + 2

            else:
                total_matras_per_line = (cls._total_ganas_per_short_line / 2) * (
                    cls._first_alternative_matras_count
                    + cls._second_alternative_matras_count
                )

            if sum(prastara_line) != total_matras_per_line:
                return False

        if not cls._pattern_matched(
            cls._total_ganas_per_short_line,
            cls._total_ganas_per_long_line,
            cls._first_alternative_matras_count,
            cls._second_alternative_matras_count,
            cls._first_long_line_index,
            cls._last_long_line_index,
            has_extra_guru=True,
        ):
            return False

        if cls._special_conditions_met():
            cls._form_ganas(
                cls._first_alternative_matras_count,
                cls._second_alternative_matras_count,
            )
            return True
        else:
            return False

