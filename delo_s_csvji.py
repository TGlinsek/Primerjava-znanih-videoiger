import os
import csv

import delo_z_datotekami

# Funkcija povzeta po gradivih iz predavanj
def zapisi_csv(slovarji, imena_polj, ime_datoteke, imenik="Primerjava-znanih-videoiger\\zberi_podatke\\csv_datoteke"):
    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
    delo_z_datotekami.pripravi_imenik(ime_datoteke)
    pot = os.path.join(imenik, ime_datoteke)  # pot je sedaj polno ime datoteke
    with open(pot, 'w', encoding='utf-8', newline='') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
        writer.writeheader()
        for slovar in slovarji:
            writer.writerow(slovar)


def preberi_csv(ime_datoteke="igre.csv", imenik="Primerjava-znanih-videoiger\\zberi_podatke\\csv_datoteke"):
    pot = os.path.join(imenik, ime_datoteke)
    with open(pot, 'r', encoding="utf-8") as csv_datoteka:
        bralec = csv.DictReader(csv_datoteka)  # lahko dodaš quotechar='|'
        seznam_slovarjev = []
        for vrstica in bralec:
            seznam_slovarjev.append(dict(vrstica))
    return seznam_slovarjev
