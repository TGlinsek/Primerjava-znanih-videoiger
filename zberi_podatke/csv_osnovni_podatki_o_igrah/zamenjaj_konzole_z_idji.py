import os, sys, inspect

sys.path.insert(1, os.path.join(sys.path[0], '../..'))

import delo_s_csvji

# glej "slovar_konzol.py"
def vrni_slovar():
    nov_slovar = {}
    seznam_slovarjev = delo_s_csvji.preberi_csv("konzole.csv")
    for slo in seznam_slovarjev:
        nov_slovar[slo["ime_konzole"]] = slo["id_konzole"]
    return nov_slovar


def presekaj_slovar_s_ključi(slo, sez_ključev):
    return {ključ : slo[ključ] for ključ in sez_ključev}


# glej "ustvari_csv_2.py"

# Slovar ima za ključe kratice konzol, kot se pojavijo na seznamih, kot vrednosti pa ima celo ime konzole.
# Tu ni vseh konzol, le tiste, ki se pojavijo na seznamih iger z vsaj 100 ocenami.
konzole = {
    "3DO": "3DO",
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
    "PS5": "PlayStation 5",
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

obrnjen_slovar_konzol = vrni_slovar()

nov_seznam = []
seznam_slovarjev = delo_s_csvji.preberi_csv("igre.csv")
for slo in seznam_slovarjev:
    # print(slo)
    slo["konzola"] = obrnjen_slovar_konzol[konzole[slo["konzola_kratica"]]]
    nov_seznam.append(presekaj_slovar_s_ključi(slo, ["id_igre", "ime", "konzola", "ocena", "tezavnost", "dolzina", "povezava"]))

delo_s_csvji.zapisi_csv(nov_seznam, ["id_igre", "ime", "konzola", "ocena", "tezavnost", "dolzina", "povezava"], "igre.csv")
