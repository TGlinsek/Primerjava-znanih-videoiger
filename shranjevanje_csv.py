import obdelaj_stran
import delo_z_datotekami
import csv
import os


csv_pot = os.path.join(delo_z_datotekami.vrni_trenutno_pot(), "csv_datoteke")


# Funkcija povzeta po gradivih iz predavanj
def zapisi_csv(slovarji, imena_polj, imenik, ime_datoteke):
    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
    delo_z_datotekami.pripravi_imenik(ime_datoteke)
    pot = os.path.join(imenik, ime_datoteke)  # pot je sedaj polno ime datoteke
    with open(pot, 'w', encoding='utf-8', newline='') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
        writer.writeheader()
        for slovar in slovarji:
            writer.writerow(slovar)


def preberi_csv(ime_datoteke="igre.csv", imenik="PROG 1\\Projekt\\Primerjava-znanih-videoiger\\csv_datoteke"):
    pot = os.path.join(imenik, ime_datoteke)
    with open(pot, 'r', encoding="utf-8") as csv_datoteka:
        bralec = csv.DictReader(csv_datoteka)  # lahko dodaš quotechar='|'
        seznam_slovarjev = []
        for vrstica in bralec:
            seznam_slovarjev.append(dict(vrstica))
    return seznam_slovarjev


# Slovar ima za ključe kratice konzol, kot se pojavijo na seznamih, kot vrednosti pa ima celo ime konzole.
# Tu ni vseh konzol, le tiste, ki se pojavijo na seznamih iger z vsaj 100 ocenami.
konzole = {
    "3D0": "3D0"
    "3DS": "3DS"
    "AND": "Android"
    "ARC": "Arcade Games"
    "ARCH": "Acorn Archimedes"
    "2600": "Atari 2600"
    "C64": "Commodore 64"
    "CDI": "CD-I"
    "DC": "Dreamcast"
    "DS": "DS"
    "FDS": "Famicom Disk System"
    "GB": "Game Boy"
    "GC": "GameCube"
    "GG": "GameGear"
    "GBA": "Game Boy Advance"
    "GBC": "Game Boy Color"
    "GEN": "Genesis"
    "IOS": "iOS (iPhone/iPad)"
    "MAC": "Macintosh"
    "MSX": "MSX"
    "N64": "Nintendo 64"
    "NEO": "Neo Geo"
    "NES": "NES"
    "NGPC": "Neo Geo Pocket Color"
    "PC": "PC"
    "PS": "PlayStation"
    "PS2": "PlayStation 2"
    "PS3": "PlayStation 3"
    "PS4": "PlayStation 4"
    "PSP": "PSP"
    "SAT": "Saturn"
    "32X": "Sega 32X"
    "SCD": "Sega CD"
    "SMS": "Sega Master System"
    "SNES": "Super Nintendo"
    "NS": "Nintendo Switch"
    "TG16": "TurboGrafx-16"
    "TCD": "Turbo CD"
    "VBOY": "Virtual Boy"
    "VITA": "PlayStation Vita"
    "WEB": "Online/Browser"
    "WII": "Wii"
    "WIIU": "Wii U"
    "XBOX": "Xbox"
    "X360": "Xbox 360"
    "XONE": "Xbox One"
}


"""def slovarja_enaka(slo1, slo2):
    if not (type({}) == type(slo1) == type(slo2)):
        raise ValueError("Vsaj eden izmed argumentov funkcije \"slovarja_enaka\" ni slovar.")
    ključi = set(slo1.keys())
    if ključi != set(slo2.keys()):
        return False
    
    for ključ in ključi:
        if slo1[ključ] != slo2[ključ]:
            return False
    return True
    

def vsi_slovarji_ki_so_v_sez2_in_ne_v_sez1(sez1, sez2):
    komplement = []
    for i in sez2:
        for j in sez1:
            if slovarja_enaka(i, j):  # analogno i == j, ni pa isto
                break
        else:
            komplement.append(i)  # če i != j za vsak j
    return komplement"""


def preberi_strani_in_izpiši_csv():
    vse_igre = []
    for i in range(170):
        igre = obdelaj_stran.vrni_slovar_podatkov_o_igrah(i)
        vse_igre += igre

    vse_konzole = obdelaj_stran.vrni_slovar_podatkov_o_konzolah()
    
    zapisi_csv(vse_igre, ["id_igre", "ime", "konzola", "konzola_kratica", "ocena", "tezavnost", "dolzina", "povezava"], csv_pot, "igre.csv")
    zapisi_csv(vse_konzole, ["id_konzole", "ime_konzole"], csv_pot, "konzole.csv")


# preberi_strani_in_izpiši_csv()
