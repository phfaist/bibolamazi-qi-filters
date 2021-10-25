
import re
import logging
logger = logging.getLogger(__name__)

sep_pat = r'(?:\.[\s~]*|[\s~]+)'


def _wordrxpat(s):
    # "P*hys*ical" -> "P(?:hys(?:ical)?)?"
    cnt = s.count("*")
    return s.replace('*', '(?:') + ')?'*cnt

def _conjunctionrxpat(s):
    # "for" -> "(for" + sep_pat + ")?"
    return "(?:" + s + sep_pat + ")?"




words = {}

conjunctions = {}


def populate_words(d):
    for k, s in d.items():
        words[k] = _wordrxpat(s)

def populate_conjunctions(a):
    for s in a:
        conjunctions[s] = _conjunctionrxpat(s)

class _W:
    Physical = 'P*hys*ical'
    Review = 'R*ev*iew'
    Letters = 'L*ett*ers'
    Reviews = 'R*ev*iews'
    Modern = 'M*od*ern'
    Physics = 'P*hys*ics'
    New = 'N*ew'
    Journal = 'J*our*nal'
    High = 'H*igh'
    Energy = 'En*erg*y'
    Nature = 'N*at*ure'
    Communications = 'C*omm*un*ications'
    Optics = 'O*pt*ics'
    Express = 'E*x*p*r*ess'
    Transactions = 'T*rans*actions'
    Information = 'I*nf*orm*ation'
    Theory = 'T*h*eory'
    Proceedings = 'P*roc*eedings'
    National = 'N*at*ion*al'
    Academy = 'A*c*ad*emy'
    Sciences = 'S*ci*ence*s'
    Research = 'R*es*earch'
    Development = 'D*ev*el*op*ment'
    Studies = 'S*t*ud*ies'
    History = 'H*is*t*ory'
    Philosophy = 'P*h*il*o*sophy'
    Science = 'S*c*i*ence'
    Royal = 'R*oy*al'
    Society = 'S*oc*iety'
    Mathematical = 'M*at*h*em*atical'
    International = 'I*n*t*er*nat*ional'
    Theoretical = 'T*h*eo*r*et*ic*al'
    Advances = 'A*d*v*an*c*es'
    Annual = 'A*n*n*ual'
    Condensed = 'C*on*d*en*sed'
    Matter = 'M*at*t*er'
    Entropy = 'E*nt*r*opy'
    Reports = 'R*ep*ort*s'
    Progress = 'P*r*og*r*ess'
    Industrial = 'I*nd*us*t*r*ial'
    Applied = 'A*p*p*l*ied'
    Mathematics = 'M*at*h*em*atics'
    Computing = 'C*om*p*ut*ing'
    Contemporary = 'C*on*t*em*p*orary'
    Fortschritte = 'F*ort*schritte'
    Physik = 'P*hy*s*ik'
    Quantum = 'Q*u*an*t*um'
    Computation = 'C*o*m*p*ut*ation'
    IEEE = 'IEEE'
    IBM = 'IBM'
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    X = 'X'
    Taylor = 'T*ay*lor'
    Francis = 'F*r*anc*is'
    Oxford = 'O*x*f*ord'
    University = 'U*ni*v*ersity'
    Press = 'P*r*ess'


populate_words(dict([(k,v) for (k, v) in _W.__dict__.items() if not k.startswith('_')]))

populate_conjunctions(['of', 'on', 'the', 'in', 'for', 'der'])

# special case for "and" which may be written as "&", possibly protected in braces
conjunctions['and'] = r'(?:(?:\{\s*)?(?:and\b|\\?\&)(?:\s*\})?\s*)?'


RxObj = type(re.compile(''))


def mkrx(pat, flags=re.IGNORECASE, start='', end='', **kwargs):
    if isinstance(pat, RxObj):
        return s

    return re.compile('^\s*' + start + pat + end + '\s*$', flags=flags, **kwargs)

def mkrxs(s, flags=re.IGNORECASE, **kwargs):
    if isinstance(s, RxObj):
        return s

    wl = s.split()
    pat_parts = []
    for w in wl:
        if w in words and w in conjunctions:
            raise ValueError("j abbrev scheme: word '{}' both a word and a conjunction?".format(w))
        if w in words:
            pat_parts.append(words[w])
            pat_parts.append(sep_pat)
        elif w in conjunctions:
            pat_parts.append(conjunctions[w])
        else:
            # keep the word as is
            pat_parts.append(w)
            #raise ValueError("j abbrev scheme: word '{}' unknown".format(w))
    
    # remove last sep_parts item
    if pat_parts[-1:] == [sep_pat]:
        pat_parts = pat_parts[:-1]

    return mkrx("".join(pat_parts), flags=flags, **kwargs)


def mkvalrepl(s, dot_at_abbrev=True):
    # sanitize replacement value. Replace '.' by '.\@' for abbreviations
    if dot_at_abbrev:
        s = s.replace('.', r'.\@')
    return s


def update_replacement_pairs(replacement_pairs, new_pairs):
    di = dict([(x[0], i) for i, x in enumerate(replacement_pairs)])
    for x in new_pairs:
        logger.debug("Adding pair %r", x)
        k, v = x
        if k in di:
            # replace value
            replacement_pairs[di[k]] = (k, v)
        else:
            # append value
            replacement_pairs.append( (k, v) )
        
