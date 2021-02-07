import os

def pripravi_imenik(ime_datoteke):
    '''Če še ne obstaja, pripravi prazen imenik za dano datoteko.'''
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)
        

def popravi_ime_datoteke(ime, nedovoljeni_znaki=["<", ">", ":", "\"", "/", "\\", "|", "?", "*"]):
    if len(nedovoljeni_znaki) == 0:
        return ime.replace(" ", "_")
    return popravi_ime_datoteke(ime.replace(nedovoljeni_znaki[0], "-"), nedovoljeni_znaki[1:])


def shrani_niz(niz, imenik, ime_datoteke):
    """Ustvari se nova datoteka na naslovu "imenik"/"ime_datoteke". Nato
    se tja zapiše vsebina parametra "text". Če je vrednost v parametru
    "directory" prazen niz, se datoteka naredi v trenutni mapi.
    """
    # os.makedirs(imenik, exist_ok=True)
    pripravi_imenik(ime_datoteke)
    pot = os.path.join(imenik, ime_datoteke)  # pot je sedaj polno ime datoteke
    with open(pot, 'w', encoding='utf-8') as output:  # utf-8 je obvezen, če črpamo iz kakih ruskih al pa kitajskih strani
        output.write(niz)
    return None


def preberi_niz(imenik="PROG 1\\Projektna_naloga-shranjene_strani", ime_datoteke="poskus pridobivanja html.py"):
    pot = os.path.join(imenik, ime_datoteke)
    with open(pot, "r", encoding='utf-8') as datoteka:  # open vedno išče v imeniku z naslovom os.getcwd()
        vsebina = datoteka.read()
    return vsebina