import os


def vrni_pot_do_imenika_odprtega_v_vsc():
    return os.getcwd()


def vrni_trenutno_pot():  # pot do datoteke, v kateri je izveden ta ukaz
    return os.path.dirname(os.path.realpath(__file__))


def vrni_vsebino_poti(pot):
    return os.listdir(pot)


def pridobi_starševski_imenik_glede_na_podano_pot(pot=vrni_trenutno_pot()):
    # obstaja malce boljši način, kjer uvozimo knjižnico Path, ampak zaenkrat bom uporabil le os knjižnico
    return os.path.abspath(os.path.join(pot, os.pardir))
