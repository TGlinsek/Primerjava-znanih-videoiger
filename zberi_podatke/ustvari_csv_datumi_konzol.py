# prebere konzole.csv in shrani starosti konzol (kdaj so izšle) v "datumi_konzol.csv"

import os, sys, inspect

sys.path.insert(1, os.path.join(sys.path[0], '..'))
import delo_s_csvji


datum_izida = {
    "3DO" : '1993-10-04',
    "3DS" : '2011-02-26',
    "Android" : '2008-09-23',
    "Arcade Games" : '1978',  # simbolično leto
    "Acorn Archimedes" : '1987-06',
    "Atari 2600" : '1977-09-11',
    "Commodore 64" : '1990-12',
    "CD-I" : '1991-12-03',
    "Dreamcast" : '1998-11-27',
    "DS" : '2004-11-21',
    "Famicom Disk System" : '1986-02-21',
    "Game Boy" : '1989-04-21',
    "GameCube" : '2001-11-05',
    "GameGear" : '1990-10-06',
    "Game Boy Advance" : '2001-03-21',
    "Game Boy Color" : '1998-10-21',
    "Genesis" : '1988-10-29',
    "iOS (iPhone/iPad)" : '2007-06-29',
    "Macintosh" : '1984-01-24',
    "MSX" : '1983',
    "Nintendo 64" : '1996-06-23',
    "Neo Geo" : '1990-01-31',
    "NES" : '1983-07-15',
    "Neo Geo Pocket Color" : '1999-03-16',
    "Nintendo Switch" : '2017-03-03',
    "PC" : '1970',  # simbolično leto
    "PlayStation" : '1994-12-03',
    "PlayStation 2" : '2000-03-04',
    "PlayStation 3" : '2006-11-11',
    "PlayStation 4" : '2013-11-15',
    "PlayStation 5" : '2020-11-12',
    "PSP" : '2004-12-12',
    "Saturn" : '1994-11-22',
    "Sega 32X" : '1994-11-21',
    "Sega CD" : '1991-12-12',
    "Sega Master System" : '1985-10-20',
    "Super Nintendo" : '1990-11-21',
    "TurboGrafx-16" : '1987-10-30',
    "Turbo CD" : '1988-12-04',
    "Virtual Boy" : '1995-07-21',
    "PlayStation Vita" : '2011-12-17',
    "Online/Browser" : '2000',  # simbolično leto
    "Wii" : '2006-11-19',
    "Wii U" : '2012-11-18',
    "Xbox" : '2013-11-22',
    "Xbox 360" : '2005-11-22',
    "Xbox One" : '2013-11-22'
}
# ne vsebuje vseh konzol, le tiste, ki pridejo v poštev (tiste, za katere obstajajo igre iz seznama, ki so na njih)

def vpiši_konzole():
    seznam_slovarjev = delo_s_csvji.preberi_csv("konzole.csv")
    print(seznam_slovarjev)

    nov_sez = []
    for slovar in seznam_slovarjev:
        ime = slovar["ime_konzole"]
        if ime not in datum_izida:
            continue  # če naletimo na konzolo, ki za nas ni relevantna
        nov_sez.append({
            "id_konzole" : slovar["id_konzole"],
            "datum_konzole" : datum_izida[ime]
        })

    delo_s_csvji.zapisi_csv(nov_sez, ["id_konzole", "datum_konzole"], "datumi_konzol.csv")

