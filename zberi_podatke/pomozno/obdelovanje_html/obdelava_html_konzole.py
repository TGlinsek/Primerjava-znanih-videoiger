# sprejme html (seznam iger, prva stran (verjetno)), vrne seznam slovarjev s podatki o vseh konzolah, za katere ima GameFAQs podatke

import re


def vrni_slovar_podatkov_konzol_iz_niza(niz):  # iz seznama
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