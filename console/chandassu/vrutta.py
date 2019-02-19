from .chandassu import Chandassu
from utils.constant import Constant


class Vrutta(Chandassu):
    _name = Constant.chandassu_names.get("vrutta").get("vrutta")
    _total_lines = 4

    _line_pattern = None

    @classmethod
    def identified(cls):
        if len(cls._prastara_values) == 0:
            return False

        if cls._line_pattern == None:
            return False

        if len(cls._prastara_values) == cls._total_lines:
            for prastara_line in cls._prastara_values:
                prastara_line_pattern = "".join(str(value) for value in prastara_line)
                if prastara_line_pattern != cls._line_pattern:
                    return False

            cls._form_ganas()
            return True
        else:
            return False

    @classmethod
    def _form_ganas(cls):
        cls._poem_letters_ganas = []
        cls._prastara_symbols_ganas = []

        if len(cls._poem_letters) == 0 or len(cls._prastara_symbols) == 0:
            return
        elif len(cls._poem_letters) != len(cls._prastara_symbols):
            return

        LAGHU_SYMBOL = Constant.prastara_info.get("laghu").get("symbol")
        GURU_SYMBOL = Constant.prastara_info.get("guru").get("symbol")

        lines_count = len(cls._poem_letters)
        i = 0
        while i < lines_count:
            cls._poem_letters_ganas.append([cls._gana_symbol])
            cls._prastara_symbols_ganas.append([cls._gana_symbol])

            letters_count = len(cls._poem_letters[i])

            aksharas_count = 3
            current_aksharas_count = 0

            j = 0
            while j < letters_count:
                poem_letter = cls._poem_letters[i][j]
                prastara_symbol = cls._prastara_symbols[i][j]

                cls._poem_letters_ganas[i].append(poem_letter)
                cls._prastara_symbols_ganas[i].append(prastara_symbol)

                if prastara_symbol == LAGHU_SYMBOL or prastara_symbol == GURU_SYMBOL:
                    current_aksharas_count += 1

                if current_aksharas_count != aksharas_count:
                    j = j + 1
                    continue

                cls._poem_letters_ganas[i].append(cls._gana_symbol)
                cls._prastara_symbols_ganas[i].append(cls._gana_symbol)

                current_aksharas_count = 0

                j = j + 1

            if cls._prastara_symbols_ganas[i][-1] != cls._gana_symbol:
                cls._poem_letters_ganas[i].append(cls._gana_symbol)
                cls._prastara_symbols_ganas[i].append(cls._gana_symbol)

            i = i + 1


class UtpalaMala(Vrutta):
    _name = Constant.chandassu_names.get("vrutta").get("utpala_mala")
    _line_pattern = "21121211121121121212"


class ChampakaMala(Vrutta):
    _name = Constant.chandassu_names.get("vrutta").get("champaka_mala")
    _line_pattern = "111121211121121121212"


class ShardulaVikreedita(Vrutta):
    _name = Constant.chandassu_names.get("vrutta").get("shardula_vikreedita")
    _line_pattern = "2221121211122212212"


class MattebhaVikreedita(Vrutta):
    _name = Constant.chandassu_names.get("vrutta").get("mattebha_vikreedita")
    _line_pattern = "11221121211122212212"


class Sragdhara(Vrutta):
    _name = Constant.chandassu_names.get("vrutta").get("sragdhara")
    _line_pattern = "222212211111122122122"


class MahaSragdhara(Vrutta):
    _name = Constant.chandassu_names.get("vrutta").get("maha_sragdhara")
    _line_pattern = "1122212211111122122122"
