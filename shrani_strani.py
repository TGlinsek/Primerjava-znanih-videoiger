import delo_z_datotekami
import shranjevanje_csv
import prenesi_strani

domena = "https://gamefaqs.gamespot.com"

url_razvrščenih_iger = domena + "/games/rankings"  # url brez query parametrov
query_dodatek = "?page="
destinacija = "PROG 1\\Projektna_naloga-shranjene_strani"
destinacija2 = "PROG 1\\Projektna_naloga-shranjene_strani\\test"


def prenesi_in_shrani(stran, imenik, ime_datoteke):
    """Vsebina se shrani v datoteko z naslovom "imenik"/"ime_datoteke"."""
    html = prenesi_strani.prenesi_eno_stran(stran)  # to je niz ali pa None
    if html:
        delo_z_datotekami.shrani_niz(html, imenik, ime_datoteke)
        return True
    return False  # napaka


def prenesi_in_shrani_n_strani(n=170):
    """Večkrat kliče funkcijo "prenesi_in_shrani"."""
    for zamično_število in range(n):  
        prenesi_in_shrani(url_razvrščenih_iger + query_dodatek + str(zamično_število), 
                            destinacija, 
                            f'stran{zamično_število}.html')

def shrani_strani_posameznih_iger(url_igre, ime_igre):
    prenesi_in_shrani(domena + url_igre, destinacija2, ime_igre)


def naloži_prvih_n_iger(n):
    seznam = shranjevanje_csv.preberi_csv()
    for i in range(n):
        shrani_strani_posameznih_iger(seznam[i]["povezava"], delo_z_datotekami.popravi_ime_datoteke(seznam[i]["ime"]))
