
import re
import logging
logger = logging.getLogger(__name__)

note_series_title_rx = re.compile(r"^Series\s+Title:\s*(?P<series>.*)$", flags=re.MULTILINE)

def bib_filter_entry(entry):
    """
    Author: Philippe Faist, (C) 2019 GPL 3+

    Description: Fix the note={} field added by better bibtex (which tries to
            add stuff like "Series Title: ...." in there

    """
    logger.longdebug("zotero_bbt_fix_note: Entry %s ...", entry.key)
    m = note_series_title_rx.match( entry.fields.get('note','') )
    if m is not None:
        logger.longdebug("... setting series")
        note = entry.fields['note']
        note = note[:m.start()] + note[m.end():]
        if note:
            entry.fields['note'] = note
        else:
            del entry.fields['note']
        entry.fields['series'] = m.group('series')
        
