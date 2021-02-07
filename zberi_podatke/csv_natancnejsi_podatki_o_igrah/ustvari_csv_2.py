import slovar_konzol
import slovar_zanrov

import os, sys, inspect

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from pomozno.obdelovanje_html import obdelava_html_igra
from pomozno import prenos_strani
from pomozno import vrni_link_do_strani

sys.path.insert(1, os.path.join(sys.path[0], '../..'))

import delo_s_csvji


# Slovar ima za ključe kratice konzol, kot se pojavijo na seznamih, kot vrednosti pa ima celo ime konzole.
# Tu ni vseh konzol, le tiste, ki se pojavijo na seznamih iger z vsaj 100 ocenami.
konzole = {
    "3D0": "3D0",
    "3DS": "3DS",
    "AND": "Android",
    "ARC": "Arcade Games",
    "ARCH": "Acorn Archimedes",
    "2600": "Atari 2600",
    "C64": "Commodore 64",
    "CDI": "CD-I",
    "DC": "Dreamcast",
    "DS": "DS",
    "FDS": "Famicom Disk System",
    "GB": "Game Boy",
    "GC": "GameCube",
    "GG": "GameGear",
    "GBA": "Game Boy Advance",
    "GBC": "Game Boy Color",
    "GEN": "Genesis",
    "IOS": "iOS (iPhone/iPad)",
    "MAC": "Macintosh",
    "MSX": "MSX",
    "N64": "Nintendo 64",
    "NEO": "Neo Geo",
    "NES": "NES",
    "NGPC": "Neo Geo Pocket Color",
    "PC": "PC",
    "PS": "PlayStation",
    "PS2": "PlayStation 2",
    "PS3": "PlayStation 3",
    "PS4": "PlayStation 4",
    "PSP": "PSP",
    "SAT": "Saturn",
    "32X": "Sega 32X",
    "SCD": "Sega CD",
    "SMS": "Sega Master System",
    "SNES": "Super Nintendo",
    "NS": "Nintendo Switch",
    "TG16": "TurboGrafx-16",
    "TCD": "Turbo CD",
    "VBOY": "Virtual Boy",
    "VITA": "PlayStation Vita",
    "WEB": "Online/Browser",
    "WII": "Wii",
    "WIIU": "Wii U",
    "XBOX": "Xbox",
    "X360": "Xbox 360",
    "XONE": "Xbox One"
}


def združi_dva_slovarja(slo1, slo2):
    nov_slo = {}
    for i in slo1:
        nov_slo[i] = slo1[i]
    for j in slo2:
        nov_slo[j] = slo2[j]
    return nov_slo


def presekaj_slovar_s_ključi(slo, sez_ključev):
    return {ključ : slo[ključ] for ključ in sez_ključev}


def vpiši_igre():
    obrnjen_slovar_konzol = slovar_konzol.vrni_slovar()
    obrnjen_slovar_žanrov = slovar_zanrov.vrni_slovar()

    sez_slojev = delo_s_csvji.preberi_csv()

    vse_igre = []
    try:
        for i, slo in enumerate(sez_slojev):
            print(i)
            link = "https://gamefaqs.gamespot.com" + slo["povezava"]
            html = prenos_strani.prenesi_eno_stran(link)
            slovar_posamezne_igre = obdelava_html_igra.vrni_slovar_podatkov_iz_posamezne_strani_igre(html)
            print(slovar_posamezne_igre)

            # to bi lahko tudi zamenjali po združevanju. Vseeno je
            slovar_posamezne_igre["zanr"] = obrnjen_slovar_žanrov[slovar_posamezne_igre["zanr"]]   # zamenjamo id žanra
            
            združen_slo = združi_dva_slovarja(slo, slovar_posamezne_igre)
            
            # zamenjamo konzolo s šifro
            združen_slo["konzola"] = obrnjen_slovar_konzol[konzole[združen_slo["konzola_kratica"]]]

            presekan_slovar = presekaj_slovar_s_ključi(združen_slo, ["id_igre", "ime", "konzola", "razvijalec", "izdajatelj", "datum", "franšiza", "zanr", "ocena", "tezavnost", "dolzina", "povezava"])
            print(presekan_slovar)
            vse_igre.append(presekan_slovar)
    except Exception as e:  
        print(e)


        
        # če je več franšiz, se vzame le ena, btw.
        delo_s_csvji.zapisi_csv(vse_igre, ["id_igre", "ime", "konzola", "razvijalec", "izdajatelj", "datum", "franšiza", "zanr", "ocena", "tezavnost", "dolzina", "povezava"], "igre2.csv")
