from .poem import Poem
from .prastara import Prastara
from .chandassu_identifier import ChandassuIdentifier


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
