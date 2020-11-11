import requests


def prenesi_eno_stran(url):
    """Argument funkcije je niz, ki predstavlja url spletne strani. Funkcija
    vrne niz z vsebino spletne strani, razen če pride do napake. Takrat vrne None.
    """
    try:
        vsebina_strani = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"})  # fajn je, da uporabiš requests, ne pa urllib
    except Exception as e:  # lahk bi dali tut except ConnectionError, kr je to verjetno edina relevantna napaka, ki se lahko zgodi
        print(f"Napaka pri prenašanju spletne strani! {e}")
        return None

    status = vsebina_strani.status_code  # to vrne npr 200, 404, itd.

    if status == requests.codes.ok:  # requests.codes.ok so vse veljavne kode
        return vsebina_strani.text
    else:
        print("Napaka pri pridobivanju vsebine! Koda: " + str(status))
        return None
