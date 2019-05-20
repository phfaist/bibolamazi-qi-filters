

from ..jab import mkrx, mkrxs, words, conjunctions
from ..jab import sep_pat as s
from ..jab import update_replacement_pairs


from .defaults import replacement_pairs as defaults_replacement_pairs

replacement_pairs = list(defaults_replacement_pairs)

update_replacement_pairs(replacement_pairs, [
    #
    # known journal names
    #
    ( 'Physical Review Letters',
      'PRL' ),
    ( 'Physical Review A',
      'PRA' ),
    ( 'Physical Review B',
      'PRB' ),
    ( 'Physical Review C',
      'PRC' ),
    ( 'Physical Review D',
      'PRD' ),
    ( 'Physical Review E',
      'PRE' ),
    ( 'Physical Review X',
      'PRX' ),
    ( 'Reviews of Modern Physics',
      'RMP' ),
    ( 'New Journal of Physics',
      'NJP' ),
    ( 'Journal of High Energy Physics',
      'JHEP' ),
    ( 'IEEE Transactions on Information Theory',
      'IEEE TIT' ),
    ( 'Proceedings of the National Academy of Sciences',
      'PNAS' ),
    ( mkrxs('Proceedings of the Royal Society A', end='.*'),
      'PRSA' ),
    ( 'Communications in Mathematical Physics',
      'CMP' ),
    ( 'International Journal of Theoretical Physics',
      'IJTP' ),
    ( 'Advances in Theoretical and Mathematical Physics',
      'ATMP' ),
    ( 'Annual Review of Condensed Matter Physics',
      'ARCMP' ),
    ( 'International Journal of Modern Physics D',
      'IJMP D' ),
    ( mkrxs('Journal of Physics A', end=r'(\s*:.*)?'),
      'JPA' ),
    ( 'Reports on Progress in Physics',
      'RPP' ),
    ( 'Society for Industrial and Applied Mathematics',
      'SIAM' ),
    ( mkrx(r'((' + words['Society'] + s + conjunctions['for'] + words['Industrial'] + s
           + conjunctions['and'] + words['Applied'] + s + words['Mathematics'] + r')|(SIAM))'
           + r'(\s|[;:,.])*'
           + words['Journal'] + s + conjunctions['on'] + words['Computing']),
      'SIAM JoC'),
    ( 'Fortschritte der Physik',
      'PROP'), # Progress of Physics
    ( 'Progress of Physics',
      'PROP'), # Progress of Physics
    ( 'Quantum Information and Computation',
      'QIC' ),
    ( mkrxs('Quantum Information', start=r'NPJ'+s),
      'NPJQI' ),

])
