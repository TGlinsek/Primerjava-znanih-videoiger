# sprejme html (prvo stran seznama iger), prebere informacije o vseh žanrih, ki se lahko pojavijo, vrne seznam slovarjev s podatki o žanrih

import re


def vrni_slovar_žanrov_iz_niza(niz):  # iz seznama
    vzorecŽanriZačetek = re.compile(
        # r'<label>Genre:</label>'
        r'<option value="0" selected="selected"> - All Categories - </option>',
        flags=re.DOTALL
    )

    vzorecŽanriKonec = re.compile(
        r'<select id="mygames_ranking_type" name="list_type">',  # veliko izbire, kaj bomo dali sem (in na sploh v mejne vzorce)
        flags=re.DOTALL
    )
    
    vzorecŽanri = re.compile(
        r'<option value=' 
        r'"(?P<id_zanra>\d.*?)">'
        r'(?P<zanr1>[\w\s\-\'/]*?) '
        r'('
            r''
            r'|'
            r'&gt;&gt; '
            r'(?P<zanr2>[\w\s\-\'/]*?) '
            r'('
                r''
                r'|'
                r'&gt;&gt; '
                r'(?P<zanr3>[\w\s\-\'/]*?) '
                r'('
                    r''
                    r'|'
                    r'&gt;&gt; '
                    r'(?P<zanr4>[\w\s\-\'/]*?) '
                r')'
            r')'
        r')'
        r'</option>',
        flags=re.DOTALL
    )

    začetekŽanrov = vzorecŽanriZačetek.search(niz).end()
    konecŽanrov = vzorecŽanriKonec.search(niz).start()

    seznamŽanrov = []
    števecŽanrov = 0

    for zadetek in vzorecŽanri.finditer(niz, začetekŽanrov, konecŽanrov):
        # print(zadetek.groupdict())
        seznamŽanrov.append(zadetek.groupdict())
        števecŽanrov += 1
    # print(števecŽanrov)
    return seznamŽanrov