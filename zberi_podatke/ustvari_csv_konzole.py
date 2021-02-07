# prenese eno stran (prvo stran seznama), prebere informacije o konzolah, jih shrani v konzole.csv

from pomozno.obdelovanje_html import obdelava_html_konzole
from pomozno import prenos_strani
from pomozno import vrni_link_do_strani

import os, sys, inspect

sys.path.insert(1, os.path.join(sys.path[0], '..'))
import delo_s_csvji


def vpiši_konzole():
    link = vrni_link_do_strani.link()
    html = prenos_strani.prenesi_eno_stran(link)
    vse_konzole = obdelava_html_konzole.vrni_slovar_podatkov_konzol_iz_niza(html)
    delo_s_csvji.zapisi_csv(vse_konzole, ["id_konzole", "ime_konzole"], "konzole.csv")