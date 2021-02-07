from pomozno.obdelovanje_html import obdelava_html_zanri
from pomozno import prenos_strani
from pomozno import vrni_link_do_strani

import os, sys, inspect

sys.path.insert(1, os.path.join(sys.path[0], '..'))
import delo_s_csvji


def vpiši_žanre():
    link = vrni_link_do_strani.link()
    html = prenos_strani.prenesi_eno_stran(link)

    vsi_žanri = obdelava_html_zanri.vrni_slovar_žanrov_iz_niza(html)

    prefiltriran_seznam_slovarjev = []
    for slovar in vsi_žanri:
        število_podžanrov = [slovar["zanr1"] is not None, slovar["zanr2"] is not None, slovar["zanr3"] is not None, slovar["zanr4"] is not None].count(True)  # izboljšaj sintakso (TODO)
        if število_podžanrov == 0:
            raise Exception("Ni bilo najdenih žanrov")
        elif število_podžanrov == 1:  # ne bomo vzeli, če je le en žanr, saj nobena igra nima tega
            continue
        prefiltriran_seznam_slovarjev.append(slovar)

    delo_s_csvji.zapisi_csv(prefiltriran_seznam_slovarjev, ["id_zanra", "zanr1", "zanr2", "zanr3", "zanr4"], "zanri.csv")