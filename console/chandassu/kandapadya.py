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

