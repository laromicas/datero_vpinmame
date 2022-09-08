"""
    TranslatedEnglish Dat class to parse different types of dat files.
"""
import re

from datero.repositories.dat import XMLDatFile
from datero.commands import config


class VPinMameDat(XMLDatFile):
    """ Translated English Dat class. """
    seed: str = 'vpinmame'

    def initial_parse(self):
        # pylint: disable=R0801
        """ Parse the dat file. """
        name = 'VPinMAME' in name.startswith('VPinMAME')

        self.company = None
        self.system = 'VPinMAME'
        self.suffix = None

        self.overrides()

        if self.modifier or self.system_type:
            self.preffix = config.get('PREFFIXES', self.modifier or self.system_type, fallback='Pinball')
        else:
            self.preffix = None

        return [self.preffix, self.company, self.system, self.suffix, self.get_date()]

