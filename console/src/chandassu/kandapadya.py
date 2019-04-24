from .chandassu import Chandassu
from ..utils.constant import Constant


class Kandapadya(Chandassu):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("kandapadya")

        self._total_lines = 4

        self._first_long_line_index = 1
        self._last_long_line_index = 3

        self._total_ganas_per_short_line = 3
        self._total_ganas_per_long_line = 5

        self._matras_count = 4

        self._gana_should_not_occur = "121"

    def identified(self):
        if len(self._prastara_values) == 0:
            return False

        if len(self._prastara_values) != self._total_lines:
            return False

        if (
            sum(self._prastara_values[0]) != 12
            or sum(self._prastara_values[2]) != 12
            or sum(self._prastara_values[1]) != 20
            or sum(self._prastara_values[3]) != 20
        ):
            return False

        if not self._pattern_matched(
            self._total_ganas_per_short_line,
            self._total_ganas_per_long_line,
            self._matras_count,
            self._matras_count,
            self._first_long_line_index,
            self._last_long_line_index,
            has_extra_guru=False,
        ):
            return False

        if self._special_conditions_met():
            self._form_ganas(self._matras_count, self._matras_count)

            return True
        else:
            return False

    def _special_conditions_met(self):
        matras = []
        gana = ""
        current_gana = 0

        lines_count = len(self._prastara_values)
        i = 0
        while i < lines_count:
            prastara_count = len(self._prastara_values[i])
            j = 0
            while j < prastara_count:
                matras.append(self._prastara_values[i][j])
                gana = gana + str(self._prastara_values[i][j])

                if sum(matras) != self._matras_count:
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
                if ((current_gana % 2) != 0) and (gana == self._gana_should_not_occur):
                    return False

                matras = []
                gana = ""

                j = j + 1

            i = i + 1

        return True
