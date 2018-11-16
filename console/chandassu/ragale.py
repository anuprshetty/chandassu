from .chandassu import Chandassu
from constant import Constant


class Ragale(Chandassu):
    _name = Constant.chandassu_names.get("ragale").get("ragale")

    _min_lines = 4

    _scenarios = None

    _gana_should_not_occur_1 = None
    _gana_should_not_occur_2 = None

    @classmethod
    def identified(cls):
        if len(cls._prastara_values) == 0:
            return False

        if (
            cls._scenarios == None
            or cls._gana_should_not_occur_1 == None
            or cls._gana_should_not_occur_2 == None
        ):
            return False

        if len(cls._prastara_values) < cls._min_lines:
            return False

        for scenario in cls._scenarios:
            if cls._check_for(scenario):
                first_alternative_matras_count = scenario.get(
                    "first_alternative_matras_count"
                )
                second_alternative_matras_count = scenario.get(
                    "second_alternative_matras_count"
                )

                cls._form_ganas(
                    first_alternative_matras_count, second_alternative_matras_count
                )

                return True

        return False

    @classmethod
    def _check_for(cls, scenario):
        total_matras_per_line = scenario.get("total_matras_per_line")
        total_ganas_per_line = scenario.get("total_ganas_per_line")
        first_alternative_matras_count = scenario.get("first_alternative_matras_count")
        second_alternative_matras_count = scenario.get(
            "second_alternative_matras_count"
        )
        has_extra_guru = scenario.get("has_extra_guru")

        for prastara_line in cls._prastara_values:
            if sum(prastara_line) != total_matras_per_line:
                return False

        if not cls._pattern_matched(
            total_ganas_per_line,
            total_ganas_per_line,
            first_alternative_matras_count,
            second_alternative_matras_count,
            first_long_line_index=-1,
            last_long_line_index=-1,
            has_extra_guru=has_extra_guru,
        ):
            return False

        return cls._special_conditions_met(
            first_alternative_matras_count,
            second_alternative_matras_count,
            has_extra_guru=has_extra_guru,
        )

    @classmethod
    def _special_conditions_met(
        cls,
        first_alternative_matras_count,
        second_alternative_matras_count,
        has_extra_guru,
    ):
        if cls._gana_should_not_occur_1 == "" or cls._gana_should_not_occur_2 == "":
            return True

        matras = []
        gana = ""

        lines_count = len(cls._prastara_values)
        i = 0
        while i < lines_count:
            matras_count = first_alternative_matras_count
            is_first_alternative_matras_count = True

            prastara_count = len(cls._prastara_values[i])
            if has_extra_guru:
                prastara_count = prastara_count - 1

            j = 0
            while j < prastara_count:
                matras.append(cls._prastara_values[i][j])
                gana = gana + str(cls._prastara_values[i][j])

                if sum(matras) != matras_count:
                    j = j + 1
                    continue

                if (
                    gana == cls._gana_should_not_occur_1
                    or gana == cls._gana_should_not_occur_2
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
    _name = Constant.chandassu_names.get("ragale").get("utsaha")

    _scenarios = [
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

    _gana_should_not_occur_1 = "12"
    _gana_should_not_occur_2 = "12"

