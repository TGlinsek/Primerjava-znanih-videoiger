import os, sys, inspect

sys.path.insert(1, os.path.join(sys.path[0], '../..'))

import delo_s_csvji


def vrni_slovar():
    nov_slovar = {}
    seznam_slovarjev = delo_s_csvji.preberi_csv("konzole.csv")
    for slo in seznam_slovarjev:
        nov_slovar[slo["ime_konzole"]] = slo["id_konzole"]
    return nov_slovar
