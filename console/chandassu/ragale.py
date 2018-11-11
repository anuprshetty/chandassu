from .chandassu import Chandassu
from constant import Constant


class Ragale(Chandassu):
    _name = Constant.chandassu_names.get("ragale").get("ragale")

    _min_lines = 4

    _scenarios = None

    _gana_should_not_occur_1 = None
    _gana_should_not_occur_2 = None

