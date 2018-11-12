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

