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

