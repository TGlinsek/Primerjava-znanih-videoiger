# Primerjava znanih videoiger

V tej nalogi bom primerjal **oceno**, **težavnost** in **dolžino** nekaterih videoiger na strani [gamefaqs](https://gamefaqs.gamespot.com/games/rankings). Analiziral bom le igre, ki imajo vsaj določeno število glasov od uporabnikov na tej spletni strani (spodnja meja je 100 glasov na posamezno igro, kar trenutno znaša 8580 iger). Za zanimivejšo analizo bom uporabil tudi podatke o konzolah, za katere so posamezne igre bile narejene.

V mapi 'csv_natancnejsi_podatki_o_igrah' so shranjeni programi, ki jih za analizo nisem potreboval, saj se je izkazalo, da stran ne dopusti tako velikega prevzema podatkov. Vseeno so programi na voljo, če bi se našel način za prenos cca 8500 strani.

## Hipoteze

Preizkusiti želim naslednje hipoteze:
1. Ali imajo težje igre v povprečju nižjo oceno?
2. Ali so igre na starejših konzolah v povprečju težje oz. imajo nižjo oceno?
3. Ali imajo arkadne igre v povprečju višjo težavnost?
4. Ali so računalniške igre v povprečju bolje ocenjene od tistih na konzolah ali telefonih?
5. Ali so krajše igre v povprečju slabše ocenjene?

## Podatki za obdelovanje

V csv datotekah so shranjeni podatki o igrah, konzolah, datumi izida konzol in žanri. V datotekah za igre so poleg njihovega imena shranjeni še njihov id, njihova konzola, ocena, težavnost, dolžina in povezava do spletne strani za to igro. Pri konzolah je poleg imena shranjen le še njihov id. Podatkov o žanrih pri analizi nisem uporabil, saj jih nisem mogel pridobiti za dovolj veliko število iger.
