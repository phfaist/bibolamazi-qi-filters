
from ..jab import mkrx, mkrxs, words, conjunctions
from ..jab import sep_pat as s


replacement_pairs = [
    #
    # Abbreviate APS Physical Review journals
    #
    ( 'Physical Review Letters',
      'Phys. Rev. Lett.' ),
    ( 'Physical Review A',
      'Phys. Rev. A' ),
    ( 'Physical Review B',
      'Phys. Rev. B' ),
    ( 'Physical Review C',
      'Phys. Rev. C' ),
    ( 'Physical Review D',
      'Phys. Rev. D' ),
    ( 'Physical Review E',
      'Phys. Rev. E' ),
    ( 'Physical Review X',
      'Phys. Rev. X' ),
    ( 'Reviews of Modern Physics',
      'Rev. Mod. Phys.' ),

]
