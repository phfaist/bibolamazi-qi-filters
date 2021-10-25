import json

import bs4


with open('ubc-ca-sci-eng-jour-abbrev.js') as f:
    d = json.loads(f.read()[1:-2])

html = d['html']

soup = bs4.BeautifulSoup(html)

jabbrev = {}
for tr in soup.find_all('tr'):
    tds = list(tr.find_all(lambda tag: tag.name == 'td' and not tag.has_attr('class')))
    if tds is None or len(tds) == 0:
        continue
    if len(tds) != 2:
        print("Expected 2 <td>'s: ", tds)
        continue
    if tds[0].string:
        jabbrev[ tds[1].string.strip() ] = tds[0].string.strip()


#
# Correct some entries manually:
#
jabbrev.update(dict([
    ('Physical Review B', 'Phys. Rev. B'),
    ('Physical Review C', 'Phys. Rev. C'),
    ('Physical Review D', 'Phys. Rev. D'),
    ('Physical Review E', 'Phys. Rev. E'),

    ('Physical Review A: Atomic, Molecular, and Optical Physics', 'Phys. Rev. A'),
    ('Physical Review B: Condensed Matter', 'Phys. Rev. B'),
    ('Physical Review C: Nuclear Physics', 'Phys. Rev. C'),
    ('Physical Review D: Particles and Fields', 'Phys. Rev. D'),
    ('Physical Review E: Statistical, Nonlinear, and Soft Matter Physics', 'Phys. Rev. E'),
    ('Physical Review E: Statistical Physics, Plasmas, Fluids, and Related Interdisciplinary Topics', 'Phys. Rev. E'),
]))




with open('ubc_ca_sci_eng_jour_abbrev.py', 'w') as f:
    f.write("""

# Thanks https://woodward.library.ubc.ca/research-help/journal-abbreviations/ !

replacement_pairs = [\n""")
    for pair in jabbrev.items():
        f.write("""    ({!r}, {!r}),\n""".format(*pair))
    f.write("""]\n""")
