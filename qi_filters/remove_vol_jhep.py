
import re
import logging
logger = logging.getLogger(__name__)

jheprx = re.compile(r'\s*J(our(nal)?|.)?\s*(of\s*)?H(igh|.)?\s*E(nergy?|.)?\s*P(hys(ics)?)?\s*',
                    flags=re.IGNORECASE)

def bib_filter_entry(entry):
    """
    Author: Philippe Faist, (C) 2018 GPL 3+

    Description: Strip "volume" field from all entries that are published in
                 JHEP (Journal of High Energy Physics)

    The volume information is not needed for entries published in JHEP, because
    the volume number is exactly the year.  So this filter will strip the volume
    information of any bibtex entry that is detected to be published in JHEP.
    The journal may be fully spelled out or abbreviated.
    """
    logger.longdebug("remove_vol_jhep: Entry %s ...", entry.key)
    m = jheprx.match( entry.fields.get('journal','') )
    if m is not None:
        logger.longdebug("... clearing volume field")
        entry.fields['volume'] = ""
        
