from .chandassu import Chandassu
from ..utils.constant import Constant


class Vrutta(Chandassu):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("vrutta").get("vrutta")
        self._total_lines = 4

        self._line_pattern = None

    def identified(self):
        if len(self._prastara_values) == 0:
            return False

        if self._line_pattern == None:
            return False

        if len(self._prastara_values) == self._total_lines:
            for prastara_line in self._prastara_values:
                prastara_line_pattern = "".join(str(value) for value in prastara_line)
                if prastara_line_pattern != self._line_pattern:
                    return False

            self._form_ganas()
            return True
        else:
            return False

    def _form_ganas(self):
        self._poem_letters_ganas = []
        self._prastara_symbols_ganas = []

        if len(self._poem_letters) == 0 or len(self._prastara_symbols) == 0:
            return
        elif len(self._poem_letters) != len(self._prastara_symbols):
            return

        LAGHU_SYMBOL = Constant.prastara_info.get("laghu").get("symbol")
        GURU_SYMBOL = Constant.prastara_info.get("guru").get("symbol")

        lines_count = len(self._poem_letters)
        i = 0
        while i < lines_count:
            self._poem_letters_ganas.append([self._gana_symbol])
            self._prastara_symbols_ganas.append([self._gana_symbol])

            letters_count = len(self._poem_letters[i])

            aksharas_count = 3
            current_aksharas_count = 0

            j = 0
            while j < letters_count:
                poem_letter = self._poem_letters[i][j]
                prastara_symbol = self._prastara_symbols[i][j]

                self._poem_letters_ganas[i].append(poem_letter)
                self._prastara_symbols_ganas[i].append(prastara_symbol)

                if prastara_symbol == LAGHU_SYMBOL or prastara_symbol == GURU_SYMBOL:
                    current_aksharas_count += 1

                if current_aksharas_count != aksharas_count:
                    j = j + 1
                    continue

                self._poem_letters_ganas[i].append(self._gana_symbol)
                self._prastara_symbols_ganas[i].append(self._gana_symbol)

                current_aksharas_count = 0

                j = j + 1

            if self._prastara_symbols_ganas[i][-1] != self._gana_symbol:
                self._poem_letters_ganas[i].append(self._gana_symbol)
                self._prastara_symbols_ganas[i].append(self._gana_symbol)

            i = i + 1


class UtpalaMala(Vrutta):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("vrutta").get("utpala_mala")
        self._line_pattern = "21121211121121121212"


class ChampakaMala(Vrutta):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("vrutta").get("champaka_mala")
        self._line_pattern = "111121211121121121212"


class ShardulaVikreedita(Vrutta):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("vrutta").get("shardula_vikreedita")
        self._line_pattern = "2221121211122212212"


class MattebhaVikreedita(Vrutta):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("vrutta").get("mattebha_vikreedita")
        self._line_pattern = "11221121211122212212"


class Sragdhara(Vrutta):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("vrutta").get("sragdhara")
        self._line_pattern = "222212211111122122122"


class MahaSragdhara(Vrutta):
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        super().__init__(poem_letters, prastara_symbols, prastara_values)
        self._name = Constant.chandassu_names.get("vrutta").get("maha_sragdhara")
        self._line_pattern = "1122212211111122122122"
