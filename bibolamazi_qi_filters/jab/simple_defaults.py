

from ..jab import mkrx, mkrxs, words, conjunctions
from ..jab import sep_pat as s


replacement_pairs = [
    #
    # known journal names
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
    ( 'New Journal of Physics',
      'N. J. Phys.' ),
    ( 'Journal of High Energy Physics',
      'J. Hi. En. Phys.' ),
    ( 'Nature Communications',
      'N. Comm.' ),
    ( 'Nature Physics',
      'N. Phys.' ),
    ( 'Nature',
      'Nat.' ),
    ( 'Optics Express',
      'Opt. Ex.' ),
    ( 'IEEE Transactions on Information Theory',
      'IEEE Tr. Inf. Theo.' ),
    ( 'Proceedings of the National Academy of Sciences',
      'Proc. Nat. Ac. Sci.' ),
    ( 'IBM Journal of Research and Development',
      'IBM J. Res. Dev.' ),
    ( mkrxs('Studies in History and Philosophy of Science', start='.*', end='.*'),
      'St. H. Phil. Sci.' ),
    ( mkrxs('Studies in History and Philosophy of Modern Physics', start='.*', end='.*'),
      'St. H. Phil. Sci.' ), # hack this one, too
    ( 'Science',
      'Sci.' ),
    ( 'Physics',
      'Phys.' ),
    ( mkrxs('Proceedings of the Royal Society A', end='.*'),
      'Proc. Roy. Soc. A' ),
    ( 'Communications in Mathematical Physics',
      'Comm. Mat. Phys.' ),
    ( 'International Journal of Theoretical Physics',
      'Int. J. Theo. Phys.' ),
    ( 'Advances in Theoretical and Mathematical Physics',
      'Adv. Theo. Mat. Phys.' ),
    ( 'Annual Review of Condensed Matter Physics',
      'Ann. Rev. Cond. Mat. Phys.' ),
    ( 'Entropy',
      'Ent.' ),
    ( 'Nature Physical Science',
      'Nat. Phys. Sci.' ),
    ( 'International Journal of Modern Physics D',
      'Int J. Mod. Phys. D' ),
    ( mkrxs('Journal of Physics A', end=r'(\s*:.*)?'),
      'J. Phys. A' ),
    ( 'Reports on Progress in Physics',
      'Rep. Prog. Phys.' ),
    ( 'Society for Industrial and Applied Mathematics',
      'Soc. Ind. App. Mat.' ),
    ( mkrx(r'((' + words['Society'] + s + conjunctions['for'] + words['Industrial'] + s
           + conjunctions['and'] + words['Applied'] + s + words['Mathematics'] + r')|(SIAM))'
           + r'(\s|[;:,.])*'
           + words['Journal'] + s + conjunctions['on'] + words['Computing']),
      'Soc. Ind. App. Mat. J. Comp.'),
    ( 'Contemporary Physics',
      'C. Phys.' ),
    ( 'Fortschritte der Physik',
      'Prog. Phys.'), # Progress of Physics
    ( 'Progress of Physics',
      'Prog. Phys.'), # Progress of Physics
    ( 'Quantum Information and Computation',
      'Qu. Inf. Comp.' ),
    ( 'Quantum',
      #'Qu.'),
      'Quantum'),
    ( mkrxs('Quantum Information', start=r'NPJ'+s),
      'NPJ Qu. Inf.' ),


    # known conference/workshop/etc. names
    ( mkrx(r'.*(?P<year>(?:19|20)\d\d).*\(\s*TASI\s*\).*', flags=0), # not ignorecase
      r'TASI \g<year>' ),
    ( mkrx(r'.*\(\s*TQC\s*(?P<year>(?:19|20)\d\d)\s*\).*', flags=0), # not ignorecase
      r'TQC \g<year>' ),
    ( mkrx(r'.*(?P<year>(?:19|20)\d\d).*\(\s*P[iI]TP\s*\).*', flags=0), # not ignorecase
      r'PiTP \g<year>' ),
    

    # known publishers
    ( 'Taylor and Francis',
      'Taylor \& Francis' ),
    ( mkrxs('Oxford University Press', end='.*'),
      r'Oxford U. Press' ),

]
