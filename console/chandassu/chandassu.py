from constant import Constant


class Chandassu:
    _name = Constant.chandassu_names.get("chandassu")
    _gana_symbol = "|"

    _poem_letters = []
    _prastara_symbols = []
    _prastara_values = []

    _poem_letters_ganas = []
    _prastara_symbols_ganas = []

    _poem_chandassu = ""

    @classmethod
    def set_poem_letters(cls, poem_letters):
        cls._poem_letters = poem_letters

    @classmethod
    def set_prastara_symbol(cls, prastara_symbol):
        cls._prastara_symbols = prastara_symbol

    @classmethod
    def set_prastara_value(cls, prastara_value):
        cls._prastara_values = prastara_value

    @classmethod
    def name(cls):
        return cls._name

    @classmethod
    def poem_chandassu(cls):
        cls._form_poem_chandassu()

        return cls._poem_chandassu


    @classmethod
    def _pattern_matched(
        cls,
        total_ganas_per_short_line,
        total_ganas_per_long_line,
        first_alternative_matras_count,
        second_alternative_matras_count,
        first_long_line_index,
        last_long_line_index,
        has_extra_guru,
    ):
        lines_count = len(cls._prastara_values)
        i = 0
        while i < lines_count:
            prastara_count = len(cls._prastara_values[i])

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
                matras_count = matras_count - cls._prastara_values[i][j]

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
