# projekt_2.py: druhý projekt do Engeto Online Python Akademie
# author: Michaela Hruskova
# email: michaela.siruckova@seznam.cz
# discord: Misa H #9905

def nazev_hry() -> None:
    '''
    Popis:
    Funkce vypise a privita uzivatele. 
    Nazev hry se vypise velkym pismenem a zarovna se na stred.
    '''
    uvitani ='Vitejte u hry piskvorky'.upper().center(70)
    oddelovac = '=' * len(uvitani)
    print(oddelovac,uvitani,oddelovac,sep='\n')


def pravidla_hry() -> None:
    '''
    Popis:
    Vypise pravidla hry piskvorky. 
    Po vypsani pravidel pouzije oddelovac na delku nazvu hry.
    '''
    nadpis = 'Pravidla hry:'.upper()
    oddelovac = '-' * len(nadpis)
    oddelovac_2 = '=' * 70
    pravidla_hry = '''
    Hraci pole je 5x5 a 6x6.
    Hraje se vzdy dvema hraci, zpravidla jednim s krizky a druhym s kolecky.
    Hraci stridave umistuji sve symboly na volne pozice v hracim poli. 
    Prvni hrac zacina a umistuje svůj symbol na libovolne misto v poli.
    Cilem je umistit ctyri sve symboly vedle sebe v radku, 
    sloupci nebo diagonale(horizontalne, vertikalne nebo diagonalne).
    Hra konci, kdyz jeden z hracu dosahne ciloveho postaveni svych symbolu
    nebo kdyz dojde k remize, coz nastane, pokud se na hracim poli 
    nenajde volne misto pro dalsi tah a zadny z hracu nedosahne ciloveho 
    postaveni.Pokud jeden z hracu dosahne ciloveho postaveni svych symbolu, 
    stava se vitezem. Pokud dojde k remize, nikdo nevyhrava a hra konci.
    '''
    print(nadpis,oddelovac,pravidla_hry,oddelovac_2,sep='\n')


def vytvor_hraci_pole() ->None:
    '''
    Popis:
    Funkce vytvori hraci pole 4x4 a vytiskne ho.

    Priklad:
    >>> vytvor_hraci_pole()
    +_____+_____+_____+_____+
    |     |     |     |     |
    +_____+_____+_____+_____+
    |     |     |     |     |
    +_____+_____+_____+_____+
    |     |     |     |     |
    +_____+_____+_____+_____+
    |     |     |     |     |
    +_____+_____+_____+_____+
    '''
    pole = [[" ", " ", " "," "], [" ", " ", " "," "],
            [" ", " ", " "," "],[" "," "," "," "]]
    for radek in pole:
        print("+_____+_____+_____+_____+")
        print("|  {}  |  {}  |  {}  |  {}  |".format(radek[0], radek[1], \
                                            radek[2], radek[3]))
    print("+_____+_____+_____+_____+")


def tiskni_pole(pole) -> None:
    '''
    Popis:
    Tiskne hraci pole s oddelovaci pomoci znaku +, | a -.

    Parametry:
    pole -- seznam seznamu, kde kazdy vnitrni seznam 
    reprezentuje radek hraciho pole.

    Priklad:
    >>> tiskni_pole([["O", " ", "X"], [" ", "X", "O"], ["O", " ", "X"]])
    +-----+-----+-----+
    |  O  |     |  X  |
    +-----+-----+-----+
    |     |  X  |  O  |
    +-----+-----+-----+
    |  O  |     |  X  |
    +-----+-----+-----+
    """
    '''
    sloupce = len(pole[0])
    print("+-----"*sloupce+"+")
    for i in range(sloupce):
        print("|  " + "  |  ".join(pole[i][j] for j in range(sloupce)) + "  |")
        print("+-----"*sloupce+"+")


def vyzva_velikost_pole() ->int:
    '''
    Popis:
    Funkce se zepta na velikost pole a overi, zda input hrace je 
    cele cislo 5 nebo 6 a prevede na integer.
    '''
    while True:
        velikost_pole = input('Zadej velikost pole: ')
        if (velikost_pole.isdigit() and
            (int(velikost_pole) == 5 or int(velikost_pole) == 6)):
            return int(velikost_pole)
        print('Velikost pole muze byt 5 nebo 6.')
    

def zacatek_hry() ->None: 
    '''
    Popis:
    Upozorni hrace, ze hra zacina
    '''
    zacatek = 'Hra zacina:'.upper()
    oddelovac = '-' * len(zacatek)
    print(zacatek,oddelovac,sep='\n')

       
def je_na_hracim_poli(cislo,velikost_pole) -> bool:
    '''
    Popis:
    Funkce overi,zda je cislo validni pro urcite hraci pole.

    Parametry:
    cislo : int
        Zadané cislo, ktere se ma overit.

    velikost_pole : int
        Velikost hraciho pole. Platna cisla jsou v rozmezi
        od 1 do velikost_pole ** 2.

    Vysledek:
    bool:
        True, pokud je zadane cislo platne pro hraci pole.
        False, pokud neni platne.
    '''   
    if cislo >= 1 and cislo <= velikost_pole ** 2:
        print(f'Toto cislo nelze zadat.Musis zadat cislo {velikost_pole}')
        return False
    else:
        return True
    

def validni_input(uziv_vstup,velikost_pole) -> bool:
    '''
    Popis:
    Funkce overuje,zda je vstup od uzivatele pouze numericky a 
    zda je vstup od hrace platny pro danou hraci plochu.

    Vstup:
    - uziv_vstup: vstup od hrace
    - velikost_pole: velikost hraci plochy

    Vysledek:
    bool:
        True, pokud je vstup od hrace platny pro danou hraci plochu.
        False, pokud vstup od hrace neni platny.
    '''
    cislo = uziv_vstup.strip()
    if not cislo.isdigit():
        print('Muzes zadat pouze cislo.')
        return False
    
    cislo = int(cislo)
    if not (1 <= cislo <= velikost_pole ** 2):
        print('Zadane cislo musi byt v rozmezi 1 a {}'
              .format(velikost_pole ** 2))
        return False
    
    return True


def jiz_obsazene_pole(pole) -> bool:
    '''
    Popis:
    Funkce upozorni uzivatele, pokud je jiz pozice obsazena.

    Parametry:
    pole: reprezentuje herní pole

    Vystup:
    True: pokud je pozice obsazena
    False: pokud je pozice volná
    '''
    if not pole == ' ':
        print('Pole je jiz obsazene')
        return True
        
    else:
        return False


def dosazeni_do_volneho_pole(pole,pozice,prvek) ->None:
    '''
    Popis:
    Funkce umoznuje dosazeni prvku na urcenou pozici v hernim poli, 
    pokud je tato pozice volna (tj. neni jiz obsazena jiným prvkem). 
   
    Parametry:
    pole: reprezentuje herni pole, do ktereho bude dosazovan prvek
    pozice: index pozice, na kterou bude dosazovan prvek 
            (pocatecni index je 0)
    prvek: hodnota, ktera bude dosazena na pozici

    Vystup:
    Vraci herni pole se zmenenou hodnotou na dane pozici. 
    Pokud pozice nebyla volna a nedoslo k zadne zmene herniho pole, 
    funkce vrati puvodni pole.
    '''
    if pole[pozice] == ' ':
        pole[pozice] = prvek
    return pole


def vyzva_hrace(hrac) -> str:
    '''
    Popis:
    Funkce slouzi k ziskani pozice na hernim poli od hrace X nebo O.

    Parametry:
    hrac: urcuje hrace, ktery je na tahu a 
          ktery bude zadavat pozici na hernim poli

    Vystup:
    Vraci pozici, kterou zadal hrac (vstup_hrace), pokud je spravne
    zadaná. Pokud hrac zada neplatnou pozici, funkce vrati upozorneni
    a bude opetovne zadat o spravny vstup.
    '''
    oddelovac = '=' * 70
    print(oddelovac)
    while True:
        vstup_hrace = input(f'Hrac {hrac} | Prosim vloz pozici: ')
        if not vstup_hrace.isdigit():
            print('Pozice musi byt cislo.')
        else:
            return vstup_hrace


def zmena_hrace(hrac_na_tahu) ->int:
    '''
    Popis:
    Funkce prepina mezi hraci

    Parametry:
    hrac_na_tahu: označuje hrace, ktery prave hraje

    Vystup:
    Funkce vraci cislo hrace (1 nebo 2), ktery ma byt na tahu
    pri dalsim tahu.
    '''
    if hrac_na_tahu == 1:
        return 2
    else:
        return 1


def overeni_vyhra(pole, hrac) -> bool:
    '''
    Popis:
    Tato funkce overi,zda hrac horizontalne,vertikalne,
    diagonalne zprava a zleva dolu nedosahl cile hry a nedosahl
    na 4 shodne symboly.

    Parametry:
    pole: pole, na kterem se hraje
    hrac: symbol hrace, ktery ma byt overen

    Vystup:
    Funkce vraci hodnotu `True`, pokud hrac dosahl vitezstvi 
    na hernim poli, jinak vraci hodnotu `False`.

    Test:
    pole = [['X', 'O', ' ', ' ', ' '],
        ['X', 'O', ' ', ' ', ' '],
        ['X', 'O', 'O', 'X', ' '],
        ['X', ' ', 'O', ' ', ' '],
        ['O', ' ', 'X', ' ', ' ']]

    hrac = 'X'
    vitezstvi = overeni_vyhra(pole, hrac)
    print(vitezstvi) # očekávaný výstup: True

    '''
    pocet_radku = len(pole)
    pocet_sloupcu = len(pole[0])

    for i in range(pocet_radku):
        for j in range(pocet_sloupcu - 3):
            if all(pole[i][j+k] == hrac for k in range(4)):
                return True

    for i in range(pocet_radku - 3):
        for j in range(pocet_sloupcu):
            if all(pole[i+k][j] == hrac for k in range(4)):
                return True

    for i in range(pocet_radku - 3):
        for j in range(pocet_sloupcu - 3):
            if all(pole[i+k][j+k] == hrac for k in range(4)):
                return True

    for i in range(pocet_radku - 3):
        for j in range(3, pocet_sloupcu):
            if all(pole[i+k][j-k] == hrac for k in range(4)):
                return True

    return False    


def remiza(pole) ->bool:
    '''
    Popis:
    Funkce zjistuje, zda doslo k remize, tedy zda nejsou na hernim poli
    zadna volna mista.

    Vystup:
    bool: Vraci True, pokud na hernim poli nejsou zadna volna mista, 
    jinak False.
    Funkce zjisti, zda doslo k remize.
    '''
    for radek in pole:
        if " " in radek:
            return False
    return True


def pokracovani_hry(hra_bezi) -> None:
    '''
    Popis:
    Funkce se zepta hrace, zda chce zacit novou hru ci nikoliv.

    Parametry:
    hra_bezi (bool): Hodnota True, pokud hra stale bezi 
    False, pokud hra skoncila.
    '''
    if hra_bezi == False:
        dotaz = input('Chces zacit novou hru? Pro prokracovani napis "ano" ' 
                      'pro ukonceni zmackni libovolnou klavesu ')
        if dotaz == 'ano':
            piskvorky()
        else:
            print('Ukoncuji program')
            quit()  


def piskvorky ():
    '''
    Hlavni funkce,hra
 
    '''
    nazev_hry()
    pravidla_hry()
    zacatek_hry()
    vytvor_hraci_pole()

    hra_bezi = True
    hrac_na_tahu = 1
    velikost_pole = vyzva_velikost_pole()
    pole = [[" " for i in range(velikost_pole)] for j in range(velikost_pole)]

    while hra_bezi:
        hrac = 'x' if hrac_na_tahu == 1 else 'o'
        volba_hrace = vyzva_hrace(hrac)

        while not validni_input(volba_hrace, velikost_pole):
            volba_hrace = vyzva_hrace(hrac)
        pozice = int(volba_hrace) - 1
        radek = pozice // velikost_pole
        sloupec = pozice % velikost_pole

        while jiz_obsazene_pole(pole[radek][sloupec]):
            volba_hrace = vyzva_hrace(hrac)
            pozice = int(volba_hrace) - 1
            radek = pozice // velikost_pole
            sloupec = pozice % velikost_pole
        pole[radek][sloupec] = hrac
        tiskni_pole(pole)

        if overeni_vyhra(pole, hrac):
            print(f'Gratulujeme, hrac {hrac} vyhral!')
            hra_bezi = False
            pokracovani_hry(hra_bezi) 
        elif remiza(pole):
            print('Remiza!')
            hra_bezi = False
            pokracovani_hry(hra_bezi)  
        else:
            hrac_na_tahu = zmena_hrace(hrac_na_tahu)
            continue


if __name__ == '__main__':
    piskvorky()
