import json

import bs4


with open('ubc-ca-sci-eng-jour-abbrev.js') as f:
    d = json.loads(f.read()[1:-2])

html = d['html']

soup = bs4.BeautifulSoup(html)

jabbrev = []
for tr in soup.find_all('tr'):
    tds = list(tr.find_all(lambda tag: tag.name == 'td' and not tag.has_attr('class')))
    if tds is None or len(tds) == 0:
        continue
    if len(tds) != 2:
        print("Expected 2 <td>'s: ", tds)
        continue
    if tds[0].string:
        jabbrev.append( ( tds[1].string.strip(), tds[0].string.strip() ) )


with open('ubc_ca_sci_eng_jour_abbrev.py', 'w') as f:
    f.write("""

# Thanks https://woodward.library.ubc.ca/research-help/journal-abbreviations/ !

replacement_pairs = [\n""")
    for pair in jabbrev:
        f.write("""    ({!r}, {!r}),\n""".format(*pair))
    f.write("""]\n""")
