import delo_z_datotekami
import prenesi_strani


naš_url = "https://gamefaqs.gamespot.com/games/rankings"  # url brez query parametrov
query_dodatek = "?page="
destinacija = "PROG 1\\Projektna_naloga-shranjene_strani"


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
        prenesi_in_shrani(naš_url + query_dodatek + str(zamično_število), 
                            destinacija, 
                            f'stran{zamično_število}.html')
