import re


def vrni_slovar_podatkov_iger_iz_niza(niz):
    # najprej najdemo zgornjo in spodnjo mejo iskanja, da se izognemo morebitnim neželenim zadetkom
    vzorecZačetek = re.compile(
        r'[^/]tbody>',
        flags=re.DOTALL
    )
    vzorecKonec = re.compile(
        r'</tbody>.*'
        r'<div class="totalresults">(?P<stevilo_iger>\d*) games in results</div>',
        flags=re.DOTALL
    )
    vzorec = re.compile(
        r'</b></td>\s*?'
        r'<td class="rmain">(?P<konzola_kratica>.*?)</td>'

        r'\s*?'
        r'<td class="rmain"><a href="'

        r'('
        r'?P<povezava>/'
        r'(?P<konzola>.*?)'
        r'/'
        r'(?P<id_igre>.*?)'
        r'-.*?'
        r')'

        r'">'

        r'(?P<ime>.*?)</a></td>\n'

        r'.*?<td class="rmain">'
        r'(?P<ocena>.*?)'
        r'</td>'

        r'.*?<td class="rmain">'
        r'(?P<tezavnost>.*?)'
        r'</td>'

        r'.*?<td class="rmain">'
        r'(?P<dolzina>.*?)'
        r'</td>',
        flags=re.DOTALL
    )

    začetek = vzorecZačetek.search(niz).end()
    konec = vzorecKonec.search(niz).start()

    seznam_zadetkov = []
    
    števec = 0  # za preverjanja števila vnosov
    for zadetek in vzorec.finditer(niz, začetek, konec):
        # print(zadetek.groupdict())
        seznam_zadetkov.append(zadetek.groupdict())
        števec += 1
    # print(števec)
    return seznam_zadetkov