from ..utils.constant import Constant


class Chandassu:
    def __init__(self, poem_letters, prastara_symbols, prastara_values):
        self._poem_letters = poem_letters
        self._prastara_symbols = prastara_symbols
        self._prastara_values = prastara_values

        self._name = Constant.chandassu_names.get("chandassu")
        self._invalid = False
        self._gana_symbol = Constant.gana_symbol

        self._poem_letters_ganas = []
        self._prastara_symbols_ganas = []

        self._poem_chandassu = ""

    def name(self):
        return self._name

    def poem_chandassu(self):
        self._form_poem_chandassu()

        return self._poem_chandassu

    def invalid(self):
        return self._invalid

    def _form_poem_chandassu(self):
        self._poem_chandassu = ""

        if len(self._poem_letters_ganas) == 0 or len(self._prastara_symbols_ganas) == 0:
            return
        elif len(self._poem_letters_ganas) != len(self._prastara_symbols_ganas):
            return

        lines_count = len(self._poem_letters_ganas)
        for i in range(0, lines_count):
            self._poem_chandassu += (
                "".join(self._prastara_symbols_ganas[i])
                + "\n"
                + "".join(self._poem_letters_ganas[i])
                + "\n\n"
            )

    def _form_ganas(
        self,
        first_alternative_matras_count,
        second_alternative_matras_count,
    ):
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
            self._poem_letters_ganas.append([])
            self._prastara_symbols_ganas.append([])

            if (
                first_alternative_matras_count != -1
                and second_alternative_matras_count != -1
            ):
                self._poem_letters_ganas[i].append(self._gana_symbol)
                self._prastara_symbols_ganas[i].append(self._gana_symbol)

            letters_count = len(self._poem_letters[i])

            matras_count = first_alternative_matras_count
            is_first_alternative_matras_count = True
            current_matras_count = 0

            j = 0
            while j < letters_count:
                poem_letter = self._poem_letters[i][j]
                prastara_symbol = self._prastara_symbols[i][j]

                self._poem_letters_ganas[i].append(poem_letter)
                self._prastara_symbols_ganas[i].append(prastara_symbol)

                if prastara_symbol == LAGHU_SYMBOL:
                    current_matras_count += 1
                elif prastara_symbol == GURU_SYMBOL:
                    current_matras_count += 2

                if current_matras_count != matras_count:
                    j = j + 1
                    continue

                self._poem_letters_ganas[i].append(self._gana_symbol)
                self._prastara_symbols_ganas[i].append(self._gana_symbol)

                current_matras_count = 0

                if is_first_alternative_matras_count:
                    matras_count = second_alternative_matras_count
                    is_first_alternative_matras_count = False
                else:
                    matras_count = first_alternative_matras_count
                    is_first_alternative_matras_count = True

                j = j + 1

            if (
                first_alternative_matras_count != -1
                and second_alternative_matras_count != -1
            ):
                if self._prastara_symbols_ganas[i][-1] != self._gana_symbol:
                    self._poem_letters_ganas[i].append(self._gana_symbol)
                    self._prastara_symbols_ganas[i].append(self._gana_symbol)

            i = i + 1

    def identified(self):
        raise NotImplementedError

    def _pattern_matched(
        self,
        total_ganas_per_short_line,
        total_ganas_per_long_line,
        first_alternative_matras_count,
        second_alternative_matras_count,
        first_long_line_index,
        last_long_line_index,
        has_extra_guru,
    ):
        lines_count = len(self._prastara_values)
        i = 0
        while i < lines_count:
            prastara_count = len(self._prastara_values[i])

            if first_long_line_index == -1 or last_long_line_index == -1:
                if has_extra_guru == True:
                    prastara_count = prastara_count - 1

            if i == first_long_line_index or i == last_long_line_index:
                total_ganas = total_ganas_per_long_line

                if has_extra_guru == True:
                    prastara_count = prastara_count - 1
            else:
                total_ganas = total_ganas_per_short_line

            matras_count = first_alternative_matras_count
            is_first_alternative_matras_count = True

            j = 0
            while j < prastara_count:
                matras_count = matras_count - self._prastara_values[i][j]

                if matras_count == 0:
                    total_ganas = total_ganas - 1

                    if is_first_alternative_matras_count:
                        matras_count = second_alternative_matras_count
                        is_first_alternative_matras_count = False
                    else:
                        matras_count = first_alternative_matras_count
                        is_first_alternative_matras_count = True

                    if total_ganas == 0:
                        if (j + 1) != prastara_count:
                            return False
                        else:
                            break
                    elif (j + 1) == prastara_count:
                        return False
                elif matras_count < 0:
                    return False
                elif (j + 1) == prastara_count:
                    return False

                j = j + 1

            i = i + 1

        return True
