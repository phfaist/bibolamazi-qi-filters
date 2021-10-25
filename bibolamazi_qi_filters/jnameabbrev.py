
import re
import os.path
import importlib
import logging

from bibolamazi.core.bibfilter import BibFilter
from bibolamazi.core.bibfilter.argtypes import enum_class
from bibolamazi.core import butils

logger = logging.getLogger(__name__)

from . import jab

# --- help texts ---

HELP_AUTHOR = """
Philippe Faist, (C) 2019, GPL 3+
"""

HELP_DESC = """
Replaces journal names by their short abbreviations
"""

HELP_TEXT = """

You can define your own abbreviation schemes by provinding a fully qualified
python module name for `-sScheme=my.python.jab.module` that provides a
`replacement_pairs` global variable.  See examples at https://github.com/phfaist/bibolamazi-qi-filters/tree/master/bibolamazi_qi_filters/jab .
"""


# --- journal abbrev schemes ---


# thanks https://stackoverflow.com/a/1310912/1694896
import pkgutil
jabbrevmods = [
    name
    for _, name, _ in pkgutil.iter_modules([
            os.path.join(os.path.dirname(__file__), 'jab')
    ])]
_jabbrevmods_pairs = [ (s, i) for i, s in enumerate(jabbrevmods) ]
JAbbrevModule = enum_class('JAbbrevModule', _jabbrevmods_pairs, default_value='defaults')




# --- filter definition ---



class JNameAbbrevFilter(BibFilter):

    # import help texts above here
    helpauthor = HELP_AUTHOR
    helpdescription = HELP_DESC
    helptext = HELP_TEXT

    def __init__(self, scheme=JAbbrevModule('defaults'), dot_at_abbrev=True):
        """
        Arguments:

          * scheme(JAbbrevModule):   Use the given abbreviations scheme.

          * dot_at_abbrev(bool):   If true (the default), then abbreviations are written
                                   e.g. as "Phys.\@ Rev.\@ Lett" which gets the spacing
                                   right in LaTeX (not end of sentence).  Set to false to
                                   keep the simple "Phys. Rev. Lett."

        """

        self.scheme = scheme
        self.dot_at_abbrev = butils.getbool(dot_at_abbrev)

        self.repl = []

        # for a in args:
        #     abbrev, name = a.split('=', 2)
        #     pat = re.sub(sep_pat, sep_pat, name) # "Phys.  Rev. Lett." -> "Phys(\.\s*|\s+)Rev(\.\s*|\s+)Lett"
        #     rx = re.compile(pat, flags=re.IGNORECASE)
        #     self.repl.append( (rx, abbrev) )

        # import the corresponding module
        strscheme = str(scheme)
        if '.' in strscheme:
            mod = importlib.import_module(strscheme)
        else:
            mod = importlib.import_module('bibolamazi_qi_filters.jab.'+strscheme)
        replacement_pairs = mod.__dict__['replacement_pairs']
        for k, v in replacement_pairs:
            # does nothing if k is already a re object:
            self.repl.append( ( jab.mkrxs(k), jab.mkvalrepl(v, dot_at_abbrev=self.dot_at_abbrev) ) )


        logger.debug("JNameAbbrevFilter: repl=%r", self.repl)

    def action(self):
        return BibFilter.BIB_FILTER_SINGLE_ENTRY

    def filter_bibentry(self, entry):

        # write debug messages, which are seen in verbose mode
        logger.debug("jnameabbrev: entry %s", entry.key)

        testfields = [
            'journal',  # journal names
            'booktitle', # conference names for '@inproceedings' types
            'publisher', # publishers for books
        ]
        for fld in testfields:
            if fld in entry.fields:
                for rx, abbrev in self.repl:
                    # replace rx by corresponding abbrev in the field value
                    entry.fields[fld] = rx.sub(abbrev, entry.fields[fld])


def bibolamazi_filter_class():
    return JNameAbbrevFilter    
