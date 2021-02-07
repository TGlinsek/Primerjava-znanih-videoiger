# prenese strani (približno 170 strani seznama, vsaka stran navede 50 iger) in podatke shrani v igre.csv (konzole ohranjajo prvotna imena)

import os, sys, inspect

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from pomozno.obdelovanje_html import obdelava_html_seznam
from pomozno import prenos_strani
from pomozno import vrni_link_do_strani

sys.path.insert(1, os.path.join(sys.path[0], '../..'))

import delo_s_csvji


def preberi_strani_in_izpiši_csv():
    vse_igre = []
    for i in range(172):
        print(i)
        link = vrni_link_do_strani.link(i)
        html = prenos_strani.prenesi_eno_stran(link)

        igre = obdelava_html_seznam.vrni_slovar_podatkov_iger_iz_niza(html)
        vse_igre += igre
    
    delo_s_csvji.zapisi_csv(vse_igre, ["id_igre", "ime", "konzola", "konzola_kratica", "ocena", "tezavnost", "dolzina", "povezava"], "igre.csv")