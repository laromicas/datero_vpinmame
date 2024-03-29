"""
    TranslatedEnglish Dat class to parse different types of dat files.
"""

from datero.repositories.dat import XMLDatFile
from datero.configuration import config


class VPinMameDat(XMLDatFile):
    """ Translated English Dat class. """
    seed: str = 'vpinmame'

    def initial_parse(self):
        # pylint: disable=R0801
        """ Parse the dat file. """
        self.company = None
        self.system = 'VPinMAME' if self.name.startswith('VPinMAME') else self.name
        self.suffix = None

        self.overrides()

        if self.modifier or self.system_type:
            self.preffix = config.get('PREFFIXES', self.modifier or self.system_type, fallback='Pinball')
        else:
            self.preffix = None

        return [self.preffix, self.company, self.system, self.suffix, self.get_date()]
