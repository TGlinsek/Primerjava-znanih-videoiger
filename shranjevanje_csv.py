import obdelaj_stran
import delo_z_datotekami
import csv
import os
import random


csv_pot = "PROG 1\\Projekt\\Primerjava-znanih-videoiger\\csv_datoteke"


def zapisi_csv(slovarji, imena_polj, imenik, ime_datoteke):
    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
    delo_z_datotekami.pripravi_imenik(ime_datoteke)
    pot = os.path.join(imenik, ime_datoteke)  # pot je sedaj polno ime datoteke
    with open(pot, 'w', encoding='utf-8') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
        writer.writeheader()
        for slovar in slovarji:
            writer.writerow(slovar)


def preberi_strani_in_izpiši_csv():
    vse_igre = []
    # vse_konzole = []
    for i in range(170):
        igre, konzole = obdelaj_stran.vrni_slovar_podatkov_strani(i)
        vse_igre += igre
        # vse_konzole += konzole
        # print(igre)
        # print(konzole)
        """
        vse_konzole1 = copy.deepcopy(vse_konzole)
        for k in konzole:
            for j in vse_konzole:
                if j["id_konzole"] == k["id_konzole"]:
                    continue
                else:
                    vse_konzole1.append(k)
        print(len(vse_konzole1))
        """
    # print(vse_konzole)
    zapisi_csv(vse_igre, ["id_igre", "ime", "konzola", "konzola_kratica","ocena", "tezavnost", "dolzina", "povezava"], csv_pot, "igre.csv")
    # zapisi_csv(vse_konzole, sorted(random.sample(vse_konzole, 1).keys()), csv_pot, "konzole.csv")


preberi_strani_in_izpiši_csv()
