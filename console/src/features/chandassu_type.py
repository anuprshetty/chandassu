from .poem import Poem
from .prastara import Prastara
from .chandassu_identifier import ChandassuIdentifier


def get_chandassu_type(input_poem):
    poem = Poem(input_poem)
    poem.cleanup()
    poem_letters = poem.letters()

    prastara = Prastara(poem_letters)
    prastara.identify()
    poem_prastara_symbol = prastara.poem_prastara_symbol()
    poem_prastara_value = prastara.poem_prastara_value()

    chandassu_identifier = ChandassuIdentifier(
        poem_letters, poem_prastara_symbol, poem_prastara_value
    )

    chandassu_identifier.identify()

    chandassu_type = chandassu_identifier.chandassu_type()

    return chandassu_type
