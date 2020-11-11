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


def slovarja_enaka(slo1, slo2):
    if not (type({}) == type(slo1) == type(slo2)):
        raise ValueError
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
    return komplement


def preberi_strani_in_izpiši_csv():
    vse_igre = []
    vse_konzole = []
    for i in range(170):
        igre, konzole = obdelaj_stran.vrni_slovar_podatkov_strani(i)
        vse_igre += igre
        vse_konzole += vsi_slovarji_ki_so_v_sez2_in_ne_v_sez1(vse_konzole, konzole)

    zapisi_csv(vse_igre, ["id_igre", "ime", "konzola", "konzola_kratica", "ocena", "tezavnost", "dolzina", "povezava"], csv_pot, "igre.csv")
    zapisi_csv(vse_konzole, ["id_konzole", "ime_konzole"], csv_pot, "konzole.csv")


preberi_strani_in_izpiši_csv()
