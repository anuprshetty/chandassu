import os
from poem import Poem
from prastara import Prastara
from chandassu_identifier import ChandassuIdentifier


class ChandassuType:
    @classmethod
    def get_chandassu_type(cls, input_poem):
        Poem.set_poem(input_poem)
        Poem.cleanup()

        Prastara.set_poem_letters(Poem.letters())
        Prastara.identify()

        ChandassuIdentifier.set_poem_letters(Poem.letters())
        ChandassuIdentifier.set_prastara_symbol(Prastara.poem_prastara_symbol())
        ChandassuIdentifier.set_prastara_value(Prastara.poem_prastara_value())
        ChandassuIdentifier.identify()

        chandassu_type = ChandassuIdentifier.chandassu_type()

        return chandassu_type


def form_output(chandassu_type):
    write_output_to_file(chandassu_type)

    write_output_to_console(chandassu_type)


def write_output_to_console(chandassu_type):
    print(f"Chandassu Name: {chandassu_type.name()}")
    print(f"Chandassu Info: \n{chandassu_type.poem_chandassu()}")




def main():
    input_poem_file_path = os.path.join(
        os.path.dirname(__file__), "input_kannada_poem.txt"
    )
    with open(input_poem_file_path, "r") as input_poem_fd:
        input_poem = input_poem_fd.read()

    chandassu_type = ChandassuType.get_chandassu_type(input_poem)

    form_output(chandassu_type)


if __name__ == "__main__":
    main()
