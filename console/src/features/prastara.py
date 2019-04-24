from ..utils.constant import Constant


class Prastara:
    def __init__(self, poem_letters):
        self._poem_letters = poem_letters

        self._prastara_symbol = []
        self._prastara_value = []

    def poem_prastara_symbol(self):
        return self._prastara_symbol

    def poem_prastara_value(self):
        return self._prastara_value

    def identify(self):
        if len(self._poem_letters) == 0:
            return

        self._form_prastara_value()
        self._form_prastara_symbol()
        self._remove_space_value_from_prastara_value()

    def _form_prastara_value(self):
        self._prastara_value = []

        halant = Constant.kannada_symbols.get("halant")
        halant_letters = Constant.kannada_symbols.get("halant_letters")
        guru_letters = Constant.kannada_symbols.get("guru_letters")

        SPACE_VALUE = Constant.prastara_info.get("space").get("value")
        LAGHU_VALUE = Constant.prastara_info.get("laghu").get("value")
        GURU_VALUE = Constant.prastara_info.get("guru").get("value")

        lines_count = len(self._poem_letters)
        i = 0
        while i < lines_count:
            prastara_line = []

            letters_count = len(self._poem_letters[i])
            j = 0
            while j < letters_count:
                if self._poem_letters[i][j] == " ":
                    prastara_line.append(SPACE_VALUE)
                elif (
                    self._poem_letters[i][j] in halant_letters
                ):  # if the letter like 'ಳ್' exists in the list ['ಳ್'], then
                    if (
                        len(prastara_line) > 0
                    ):  # if the letter like 'ಳ್' is not the first_letter in the line, then
                        prastara_line[
                            -1
                        ] = GURU_VALUE  # then (previous_letter and current_letter) together becomes GURU
                    else:
                        pass  # if the letter like 'ಳ್' is the first_letter in the line, then ignore that letter.
                    prastara_line.append(
                        SPACE_VALUE
                    )  # if the letter is like 'ಳ್', then add a SPACE as a placeholder for that letter.
                elif any(
                    [
                        guru_letter in self._poem_letters[i][j]
                        for guru_letter in guru_letters
                    ]  # if the letter is GURU, then
                ):
                    prastara_line.append(GURU_VALUE)
                elif (
                    j + 1 < letters_count
                ):  # if the letter is not the last_letter in the line, then
                    if (
                        halant
                        in self._poem_letters[i][
                            j + 1
                        ]  # here '್' exists in the next_letter 'ಳ್ದ' (Because 'ಳ' + '್' + 'ದ' = 'ಳ್ದ') and
                        and self._poem_letters[i][j + 1]
                        not in halant_letters  # and the next_letter 'ಳ್ದ' doesn't exist in the list ['ಳ್'].
                    ):  # if the next_letter is like 'ಳ್ದ', then
                        # next_letter_symbols = list(self._poem_letters[i][j + 1])
                        # if (
                        #     len(next_letter_symbols)
                        #     <= 4  # 'ರ್ಗೆ' ('ರ' + '್' + 'ಗ' + "ೆ").
                        #     and next_letter_symbols[0] == "ರ"
                        #     and next_letter_symbols[2] != "ರ"
                        # ):
                        #     prastara_line.append(
                        #         LAGHU_VALUE
                        #     )  # special case of ಒತ್ತಕ್ಷರ 'ರ್ಗ' ('ರ' + '್' + 'ಗ'). In this case ಒತ್ತಕ್ಷರದ ಹಿಂದಿನ ಅಕ್ಷರ ಲಘುವಾಗಿರುತ್ತದೆ.
                        # else:
                        #     prastara_line.append(
                        #         GURU_VALUE
                        #     )  # ಒತ್ತಕ್ಷರದ ಹಿಂದಿನ ಅಕ್ಷರ ಗುರುವಾಗಿರುತ್ತದೆ.

                        prastara_line.append(
                            GURU_VALUE
                        )  # ಒತ್ತಕ್ಷರದ ಹಿಂದಿನ ಅಕ್ಷರ ಗುರುವಾಗಿರುತ್ತದೆ.
                    elif (
                        self._poem_letters[i][j + 1] == " "
                        and halant in self._poem_letters[i][j + 2]
                        and self._poem_letters[i][j + 2] not in halant_letters
                    ):  # if the next_letter is space and next_to_next_letter is like 'ಳ್ದ', then
                        # next_letter_symbols = list(self._poem_letters[i][j + 2])
                        # if (
                        #     len(next_letter_symbols)
                        #     <= 4  # 'ರ್ಗೆ' ('ರ' + '್' + 'ಗ' + "ೆ").
                        #     and next_letter_symbols[0] == "ರ"
                        #     and next_letter_symbols[2] != "ರ"
                        # ):
                        #     prastara_line.append(
                        #         LAGHU_VALUE
                        #     )  # special case of ಒತ್ತಕ್ಷರ 'ರ್ಗ' ('ರ' + '್' + 'ಗ'). In this case ಒತ್ತಕ್ಷರದ ಹಿಂದಿನ ಅಕ್ಷರ ಲಘುವಾಗಿರುತ್ತದೆ.
                        # else:
                        #     prastara_line.append(
                        #         GURU_VALUE
                        #     )  # ಒತ್ತಕ್ಷರದ ಹಿಂದಿನ ಅಕ್ಷರ ಗುರುವಾಗಿರುತ್ತದೆ.

                        prastara_line.append(
                            GURU_VALUE
                        )  # ಒತ್ತಕ್ಷರದ ಹಿಂದಿನ ಅಕ್ಷರ ಗುರುವಾಗಿರುತ್ತದೆ.
                    else:  # otherwise letter is LAGHU.
                        prastara_line.append(LAGHU_VALUE)
                elif (
                    i + 1 < lines_count and len(self._poem_letters[i + 1]) != 0
                ):  # if the letter is the last_letter in the line and current_line is not the last_line, then
                    if (
                        halant in self._poem_letters[i + 1][0]
                        or self._poem_letters[i + 1][0] in halant_letters
                    ):  # if first_letter in the next_line is like 'ಳ್ದ' OR like 'ಳ್', then
                        prastara_line.append(
                            GURU_VALUE
                        )  # then last_letter in the line will be GURU.
                    else:
                        prastara_line.append(
                            LAGHU_VALUE
                        )  # otherwise last_letter in the line will be LAGHU.
                else:  # By default, letter is LAGHU.
                    prastara_line.append(LAGHU_VALUE)

                j = j + 1

            self._prastara_value.append(prastara_line)
            i = i + 1

    def _form_prastara_symbol(self):
        self._prastara_symbol = []

        LAGHU_VALUE = Constant.prastara_info.get("laghu").get("value")
        GURU_VALUE = Constant.prastara_info.get("guru").get("value")

        SPACE_SYMBOL = Constant.prastara_info.get("space").get("symbol")
        LAGHU_SYMBOL = Constant.prastara_info.get("laghu").get("symbol")
        GURU_SYMBOL = Constant.prastara_info.get("guru").get("symbol")

        for line_index, prastara_line in enumerate(self._prastara_value):
            self._prastara_symbol.append([])
            for value in prastara_line:
                if value == LAGHU_VALUE:
                    self._prastara_symbol[line_index].append(LAGHU_SYMBOL)
                elif value == GURU_VALUE:
                    self._prastara_symbol[line_index].append(GURU_SYMBOL)
                else:
                    self._prastara_symbol[line_index].append(SPACE_SYMBOL)

    def _remove_space_value_from_prastara_value(self):
        self._prastara_value = [
            [value for value in prastara_line if value != 0]
            for prastara_line in self._prastara_value
        ]
