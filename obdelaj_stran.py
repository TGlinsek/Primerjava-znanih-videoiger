import delo_z_datotekami
import re


# število_vnosov_na_stran = 50  # to mora vedno biti 50


def vrni_slovar_podatkov_konzol_iz_niza(niz):
    vzorecKonzoleZačetek = re.compile(
        r'<optgroup label="All Platforms">',
        flags=re.DOTALL
    )

    vzorecKonzoleKonec = re.compile(
        r'</optgroup>\s*?<[^o]',
        flags=re.DOTALL
    )
    
    vzorecKonzole = re.compile(
        r'<option value=' 
        r'"(?P<id_konzole>\d.*?)">'
        r'(?P<ime_konzole>.*?)'
        r'</option>',
        flags=re.DOTALL
    )

    začetekKonzol = vzorecKonzoleZačetek.search(niz).end()
    konecKonzol = vzorecKonzoleKonec.search(niz).start()

    seznamKonzol = []
    števecKonzol = 0

    for zadetek in vzorecKonzole.finditer(niz, začetekKonzol, konecKonzol):
        # print(zadetek.groupdict())
        seznamKonzol.append(zadetek.groupdict())
        števecKonzol += 1
    # print(števecKonzol)
    return seznamKonzol


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


def vrni_slovar_podatkov_strani(indeks_strani):
    ime_datoteke = f"stran{indeks_strani}.html"
    vsebina = delo_z_datotekami.preberi_niz("PROG 1\\Projektna_naloga-shranjene_strani", 
                                            ime_datoteke)
    return vrni_slovar_podatkov_iger_iz_niza(vsebina), vrni_slovar_podatkov_konzol_iz_niza(vsebina)


# igre, konzole = vrni_slovar_podatkov_strani(0)

"""
set_imen_konzol = set()
for i in igre:
    set_imen_konzol.add((i["konzola"], i["konzola_kratica"]))
print(sorted(set_imen_konzol))
"""
