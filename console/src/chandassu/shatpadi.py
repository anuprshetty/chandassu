from .chandassu import Chandassu
from ..utils.constant import Constant


class Shatpadi(Chandassu):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("shatpadi").get("shatpadi")
        self._total_lines = 6

        self._first_long_line_index = 2
        self._last_long_line_index = 5

        self._total_ganas_per_short_line = None
        self._total_ganas_per_long_line = None

        self._first_alternative_matras_count = None
        self._second_alternative_matras_count = None

        self._gana_should_not_occur_1 = None
        self._gana_should_not_occur_2 = None

    def identified(self):
        if len(self._prastara_values) == 0:
            return False

        if (
            self._total_ganas_per_short_line == None
            or self._total_ganas_per_long_line == None
            or self._first_alternative_matras_count == None
            or self._second_alternative_matras_count == None
            or self._gana_should_not_occur_1 == None
            or self._gana_should_not_occur_2 == None
        ):
            return False

        if len(self._prastara_values) != self._total_lines:
            return False

        GURU_VALUE = Constant.prastara_info.get("guru").get("value")
        self._prastara_values[self._first_long_line_index][-1] = GURU_VALUE
        self._prastara_values[self._last_long_line_index][-1] = GURU_VALUE

        for line_index in range(0, len(self._prastara_values)):
            prastara_line = self._prastara_values[line_index]

            if line_index == 2 or line_index == 5:
                total_matras_per_line = (self._total_ganas_per_long_line / 2) * (
                    self._first_alternative_matras_count
                    + self._second_alternative_matras_count
                ) + 2

            else:
                total_matras_per_line = (self._total_ganas_per_short_line / 2) * (
                    self._first_alternative_matras_count
                    + self._second_alternative_matras_count
                )

            if sum(prastara_line) != total_matras_per_line:
                return False

        if not self._pattern_matched(
            self._total_ganas_per_short_line,
            self._total_ganas_per_long_line,
            self._first_alternative_matras_count,
            self._second_alternative_matras_count,
            self._first_long_line_index,
            self._last_long_line_index,
            has_extra_guru=True,
        ):
            return False

        if self._special_conditions_met():
            GURU_SYMBOL = Constant.prastara_info.get("guru").get("symbol")
            self._prastara_symbols[self._first_long_line_index][-1] = GURU_SYMBOL
            self._prastara_symbols[self._last_long_line_index][-1] = GURU_SYMBOL

            self._form_ganas(
                self._first_alternative_matras_count,
                self._second_alternative_matras_count,
            )

            return True
        else:
            return False

    def _special_conditions_met(self):
        if self._gana_should_not_occur_1 == "" or self._gana_should_not_occur_2 == "":
            return True

        matras = []
        gana = ""

        lines_count = len(self._prastara_values)
        i = 0
        while i < lines_count:
            matras_count = self._first_alternative_matras_count
            is_first_alternative_matras_count = True

            prastara_count = len(self._prastara_values[i])
            if (
                i == 2 or i == 5
            ):  # if shatpadi line is a long line (i.e., at line index 2 and 5), then there will always be an extra_guru at the end of the line.
                prastara_count = prastara_count - 1

            j = 0
            while j < prastara_count:
                matras.append(self._prastara_values[i][j])
                gana = gana + str(self._prastara_values[i][j])

                if sum(matras) != matras_count:
                    j = j + 1
                    continue

                if (
                    gana == self._gana_should_not_occur_1
                    or gana == self._gana_should_not_occur_2
                ):
                    return False

                if is_first_alternative_matras_count:
                    matras_count = self._second_alternative_matras_count
                    is_first_alternative_matras_count = False
                else:
                    matras_count = self._first_alternative_matras_count
                    is_first_alternative_matras_count = True

                matras = []
                gana = ""

                j = j + 1

            i = i + 1

        return True


class Shara(Shatpadi):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("shatpadi").get("shara")

        self._total_ganas_per_short_line = 2
        self._total_ganas_per_long_line = 3

        self._first_alternative_matras_count = 4
        self._second_alternative_matras_count = 4

        self._gana_should_not_occur_1 = "121"
        self._gana_should_not_occur_2 = "121"


class Kusuma(Shatpadi):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("shatpadi").get("kusuma")

        self._total_ganas_per_short_line = 2
        self._total_ganas_per_long_line = 3

        self._first_alternative_matras_count = 5
        self._second_alternative_matras_count = 5

        self._gana_should_not_occur_1 = "1211"
        self._gana_should_not_occur_2 = "122"


class Bhoga(Shatpadi):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("shatpadi").get("bhoga")

        self._total_ganas_per_short_line = 4
        self._total_ganas_per_long_line = 6

        self._first_alternative_matras_count = 3
        self._second_alternative_matras_count = 3

        self._gana_should_not_occur_1 = "12"
        self._gana_should_not_occur_2 = "12"


class Bhamini(Shatpadi):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("shatpadi").get("bhamini")

        self._total_ganas_per_short_line = 4
        self._total_ganas_per_long_line = 6

        self._first_alternative_matras_count = 3
        self._second_alternative_matras_count = 4

        self._gana_should_not_occur_1 = "12"
        self._gana_should_not_occur_2 = "121"


class Vardhaka(Shatpadi):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("shatpadi").get("vardhaka")

        self._total_ganas_per_short_line = 4
        self._total_ganas_per_long_line = 6

        self._first_alternative_matras_count = 5
        self._second_alternative_matras_count = 5

        self._gana_should_not_occur_1 = "1211"
        self._gana_should_not_occur_2 = "122"


class Parivardhini(Shatpadi):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("shatpadi").get("parivardhini")

        self._total_ganas_per_short_line = 4
        self._total_ganas_per_long_line = 6

        self._first_alternative_matras_count = 4
        self._second_alternative_matras_count = 4

        self._gana_should_not_occur_1 = "121"
        self._gana_should_not_occur_2 = "121"
