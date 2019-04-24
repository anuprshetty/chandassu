from .chandassu import Chandassu
from ..utils.constant import Constant


class Ragale(Chandassu):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("ragale").get("ragale")

        self._min_lines = 4

        self._scenarios = None

        self._gana_should_not_occur_1 = None
        self._gana_should_not_occur_2 = None

    def identified(self):
        if len(self._prastara_values) == 0:
            return False

        if (
            self._scenarios == None
            or self._gana_should_not_occur_1 == None
            or self._gana_should_not_occur_2 == None
        ):
            return False

        if len(self._prastara_values) < self._min_lines:
            return False

        for scenario in self._scenarios:
            if self._check_for(scenario):
                first_alternative_matras_count = scenario.get(
                    "first_alternative_matras_count"
                )
                second_alternative_matras_count = scenario.get(
                    "second_alternative_matras_count"
                )

                self._form_ganas(
                    first_alternative_matras_count, second_alternative_matras_count
                )

                return True

        return False

    def _check_for(self, scenario):
        total_matras_per_line = scenario.get("total_matras_per_line")
        total_ganas_per_line = scenario.get("total_ganas_per_line")
        first_alternative_matras_count = scenario.get("first_alternative_matras_count")
        second_alternative_matras_count = scenario.get(
            "second_alternative_matras_count"
        )
        has_extra_guru = scenario.get("has_extra_guru")

        for prastara_line in self._prastara_values:
            if sum(prastara_line) != total_matras_per_line:
                return False

        if not self._pattern_matched(
            total_ganas_per_line,
            total_ganas_per_line,
            first_alternative_matras_count,
            second_alternative_matras_count,
            first_long_line_index=-1,
            last_long_line_index=-1,
            has_extra_guru=has_extra_guru,
        ):
            return False

        return self._special_conditions_met(
            first_alternative_matras_count,
            second_alternative_matras_count,
            has_extra_guru=has_extra_guru,
        )

    def _special_conditions_met(
        self,
        first_alternative_matras_count,
        second_alternative_matras_count,
        has_extra_guru,
    ):
        if self._gana_should_not_occur_1 == "" or self._gana_should_not_occur_2 == "":
            return True

        matras = []
        gana = ""

        lines_count = len(self._prastara_values)
        i = 0
        while i < lines_count:
            matras_count = first_alternative_matras_count
            is_first_alternative_matras_count = True

            prastara_count = len(self._prastara_values[i])
            if has_extra_guru:
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
                    matras_count = second_alternative_matras_count
                    is_first_alternative_matras_count = False
                else:
                    matras_count = first_alternative_matras_count
                    is_first_alternative_matras_count = True

                matras = []
                gana = ""

                j = j + 1

            i = i + 1

        return True


class Utsaha(Ragale):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("ragale").get("utsaha")

        self._scenarios = [
            {
                "total_matras_per_line": 24,
                "total_ganas_per_line": 8,
                "first_alternative_matras_count": 3,
                "second_alternative_matras_count": 3,
                "has_extra_guru": False,
            },
            {
                "total_matras_per_line": 12,
                "total_ganas_per_line": 4,
                "first_alternative_matras_count": 3,
                "second_alternative_matras_count": 3,
                "has_extra_guru": False,
            },
            {
                "total_matras_per_line": 11,
                "total_ganas_per_line": 3,
                "first_alternative_matras_count": 3,
                "second_alternative_matras_count": 3,
                "has_extra_guru": True,
            },
        ]

        self._gana_should_not_occur_1 = "12"
        self._gana_should_not_occur_2 = "12"


class Mandanila(Ragale):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)

        self._name = Constant.chandassu_names.get("ragale").get("mandanila")

        self._scenarios = [
            {
                "total_matras_per_line": 16,
                "total_ganas_per_line": 4,
                "first_alternative_matras_count": 4,
                "second_alternative_matras_count": 4,
                "has_extra_guru": False,
            },
            {
                "total_matras_per_line": 16,
                "total_ganas_per_line": 4,
                "first_alternative_matras_count": 3,
                "second_alternative_matras_count": 5,
                "has_extra_guru": False,
            },
        ]

        self._gana_should_not_occur_1 = "12"
        self._gana_should_not_occur_2 = "12"


class Lalita(Ragale):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)

        self._name = Constant.chandassu_names.get("ragale").get("lalita")

        self._scenarios = [
            {
                "total_matras_per_line": 20,
                "total_ganas_per_line": 4,
                "first_alternative_matras_count": 5,
                "second_alternative_matras_count": 5,
                "has_extra_guru": False,
            }
        ]

        self._gana_should_not_occur_1 = "1211"
        self._gana_should_not_occur_2 = "122"
