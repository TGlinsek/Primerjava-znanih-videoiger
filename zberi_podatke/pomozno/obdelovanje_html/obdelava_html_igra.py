import re


meseci = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}


def pretvori_datum(niz):
    # niz je oblike November 23, 1998
    # ciljna oblika: 1998-11-23
    členi_datuma = niz.split()  # tu ne sme bit niz.split(" "), kr se lahk zgodi, da mamo dvojne presledke v stringu (split() ima za take primere to že vgrajeno)
    if len(členi_datuma) == 3:
        mesec, dan, leto = členi_datuma
        dan = dan[:-1]
        mesec = str(meseci[mesec])
        return "-".join([leto, mesec, dan])
    elif len(členi_datuma) == 2:
        mesec, leto = členi_datuma
        mesec = str(meseci[mesec])
        return "-".join([leto, mesec])
    elif len(členi_datuma) == 1:
        leto = členi_datuma[0]
        return leto
    else:
        raise Exception("Datum " + niz + " ni ustrezen.")
    

def vrni_vrednost_dveh_ekvivalentnih(a, b):
    if type(a) != bool or type(b) != bool:
        raise Exception("Argumenta morata biti tipa bool.")
    if a != b:
        raise Exception("Argumenta nista enaka!")  # argumenta si nista ekvivalentna
    return a


def poenostavi_slovar(slovar):
    """
        Ločimo primera, kjer sta razvijalec in izdajatelj posebej napisana oz. skupaj
        Pogrupiramo žanre
        Prevedemo datum
    """
    nov_slovar = {}

    # Developer, publisher
    razvijalec = slovar["razvijalec"]
    izdajatelj = slovar["izdajatelj"]
    if vrni_vrednost_dveh_ekvivalentnih(razvijalec is None, izdajatelj is None):
        nov_slovar["razvijalec"] = slovar["razvijalecInIzdajatelj"]
        nov_slovar["izdajatelj"] = slovar["razvijalecInIzdajatelj"]
    else:
        nov_slovar["razvijalec"] = razvijalec
        nov_slovar["izdajatelj"] = izdajatelj
    
    # Žanri
    # najprej preverimo, ali sta vsaj dve komponenti žanra
    število_podžanrov = [slovar["zanr1"] is not None, slovar["zanr2"] is not None, slovar["zanr3"] is not None, slovar["zanr4"] is not None].count(True)  # izboljšaj sintakso (TODO)
    if število_podžanrov == 0:
        raise Exception("Ni bilo najdenega žanra. Slovar je tak:\n" + str(slovar))
    elif število_podžanrov == 1:
        raise Exception("Le en žanr je bil najden. To se ne bi smelo zgoditi. Slovar je tak:\n" + str(slovar))
    
    # nov_slovar["zanr"] = (slovar["zanr1"], slovar["zanr2"], slovar["zanr3"], slovar["zanr4"])
    seznam_podžanrov = sorted([slovar["zanr1"], slovar["zanr2"], slovar["zanr3"], slovar["zanr4"]], key=lambda x: x is None)  # če imamo žanr ("Action Adventure", None, None, "Open-World"), ga spremeni v ("Action Adventure", "Open-World", None, None)
    # tuki bi morda lahko bil drugačen format (odstranimo vse pojavitve od None)
    # morda lahko tu odstranimo eno komponento, saj ne obstaja igre, ki bi imela le zanr1 (ampak verjetno je vseen fajn obdržat vse žanre)

    nabor_podžanrov = tuple(['' if x is None else x for x in seznam_podžanrov])


    nov_slovar["zanr"] = nabor_podžanrov

    for i in slovar:
        if i not in ["razvijalec", "izdajatelj", "razvijalecInIzdajatelj", "zanr1", "zanr2", "zanr3", "zanr4"]:
            if i == "datum":
                nov_slovar["datum"] = pretvori_datum(slovar["datum"])
            else:
                nov_slovar[i] = slovar[i]
    
    return nov_slovar


def vrni_slovar_podatkov_iz_posamezne_strani_igre(niz):
    vzorec = re.compile(
        r'Platform:</b> <a href="[^"]*?">(?P<igralna_konzola>[^<>"]+?)</a> </li>'
        r'(\s)*?'  # ne rabimo oklepajev tam okoli
        r'<li><b>'

        # r"""Genre:</b> (<a href="[^"]*?">(?P<zanr1>[^<>"]+?)</a>)+?( &raquo; <a href="[^"]*?">(?P<zanr2>[^<>"]+?)</a>)*?( &raquo; <a href="[^"]*?">(?P<zanr3>[^<>"]+?)</a>\s{2})*?"""
        r"""Genre:</b> (<a href="[^"]*?">(?P<zanr1>[^<>"]+?)</a>)+?( &raquo; <a href="[^"]*?">(?P<zanr2>[^<>"]+?)</a>)*?( &raquo; <a href="[^"]*?">(?P<zanr3>[^<>"]+?)</a>)*?( &raquo; <a href="[^"]*?">(?P<zanr4>[^<>"]+?)</a>\s{2})*?"""  # lahko so tudi štiri komponente podatka o žanru
        r'(\s)*?'
        r'<li><b>'

        r'('
            r'Developer:</b> <a href="[^"]*?">(?P<razvijalec>[^<>"]+?)</a></li>'
            r'(\s)*?'
            r'<li><b>'
            r'Publisher:</b> <a href="[^"]*?">(?P<izdajatelj>[^<>"]+?)</a></li>'
            r'|'
            r'Developer/Publisher: </b><a href="[^"]*?">(?P<razvijalecInIzdajatelj>[^<>"]+?)</a></li>'
        r')'
        r'(\s)*?'
        r'<li><b>'

        r'Release:</b> <a href="[^"]*?">(?P<datum>[^<>"]+?)</a></li>'
        r'('
            r'(\s)*?'
            r'<li><b>'
            r'Expansions:</b> <a href="[^"]*?">([^<>"]+?)</a></li>'
            r'|'
            r''
        r')'
        r'('
            r'(\s)*?'
            r'<li><b>'
            r'Also Known As:</b> <i>[^<>"]+?</i>'
            r'|'
            r''
        r')'
        r'(\s)*?'
        r'<li><b>'

        r'('
            r'('
                r'Franchise:</b>&nbsp;(\s)*?<a href="[^"]*?">'
                r'|'
                r'Franchises:</b>&nbsp;(\s)*?<a href=(.*?)<a href="[^"]*?">'
            r')'
            r'(?P<franšiza>[^<>"]+?)</a>(\s)*?</li>(\s)*?</ul>'
            r'(\s)*?'
            r'</div>'
            r'|'
            r''
        r')'
        ,
        flags=re.DOTALL
    )
    seznam_zadetkov = []
    števec = 0
    for zadetek in vzorec.finditer(niz):
        seznam_zadetkov.append(zadetek.groupdict())
        števec += 1
    if števec != 1:
        raise Exception("Napačen števec! Števec: " + str(števec))
    return poenostavi_slovar(seznam_zadetkov[0])
