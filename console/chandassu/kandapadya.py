from .chandassu import Chandassu
from utils.constant import Constant


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

    @classmethod
    def _special_conditions_met(cls):
        matras = []
        gana = ""
        current_gana = 0

        lines_count = len(cls._prastara_values)
        i = 0
        while i < lines_count:
            prastara_count = len(cls._prastara_values[i])
            j = 0
            while j < prastara_count:
                matras.append(cls._prastara_values[i][j])
                gana = gana + str(cls._prastara_values[i][j])

                if sum(matras) != cls._matras_count:
                    j = j + 1
                    continue

                current_gana = current_gana + 1

                if (current_gana == 6 or current_gana == 14) and (
                    gana != "1111" and gana != "121"
                ):
                    return False
                if (current_gana == 8 or current_gana == 16) and (
                    gana != "22" and gana != "112"
                ):
                    return False
                if ((current_gana % 2) != 0) and (gana == cls._gana_should_not_occur):
                    return False

                matras = []
                gana = ""

                j = j + 1

            i = i + 1

        return True
