# prebere zanri.csv in ustvari slovar, ki ima žanre (torej, nabore podžanrov) za ključe in idje za vrednosti

import os, sys, inspect

sys.path.insert(1, os.path.join(sys.path[0], '../..'))

import delo_s_csvji


def vrni_slovar():
    nov_slovar = {}
    seznam_slovarjev = delo_s_csvji.preberi_csv("zanri.csv")
    for slo in seznam_slovarjev:
        nov_slovar[(slo["zanr1"], slo["zanr2"], slo["zanr3"], slo["zanr4"])] = slo["id_zanra"]
    return nov_slovar
