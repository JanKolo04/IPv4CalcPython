def main():
    global x1, x2, x3, x4, y1, y2, y3, y4, adres_IP, maska, maska_bin
    adres_IP = (input("Wpisz adres IP: "))
    ip = adres_IP.split('.')

    lista2 = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    x = []
    for i in adres_IP:
        if i not in lista2:
            x.append('nie ma')
        else:
            x.append('siema')

    ile = x.count('siema')
    if ile <= 8:
        raise ValueError("zle wpisanie w IP")

    x1 = (int(ip[0]))
    x2 = (int(ip[1]))
    x3 = (int(ip[2]))
    x4 = (int(ip[3]))

    if x1 > 255:
        raise ValueError("Liczba jest zbyt wysoka w 1 oktecie IP")
    elif x2 > 255:
        raise ValueError("Liczba jest zbyt wysoka w 2 oktecie IP")
    elif x3 > 255:
        raise ValueError("Liczba jest zbyt wysoka w 3 oktecie IP")
    elif x4 > 255:
        raise ValueError("Liczba jest zbyt wysoka w 4 oktecie IP")

    print("\nMaski:")
    print("/0  0.0.0.0")
    print("/1  128.0.0.0")
    print("/2  192.0.0.0")
    print("/3  224.0.0.0")
    print("/4  240.0.0.0")
    print("/5  248.0.0.0")
    print("/6  252.0.0.0")
    print("/7  254.0.0.0")
    print("/8  255.0.0.0")
    print("/9  255.128.0.0")
    print("/10  255.192.0.0")
    print("/11  255.224.0.0")
    print("/12  255.240.0.0")
    print("/13  255.248.0.0")
    print("/14  255.252.0.0")
    print("/15  255.254.0.0")
    print("/16  255.255.0.0")
    print("/17  255.255.128.0")
    print("/18  255.255.192.0")
    print("/19  255.255.224.0")
    print("/20  255.255.240.0")
    print("/21  255.255.248.0")
    print("/22  255.255.252.0")
    print("/23  255.255.254.0")
    print("/24  255.255.255.0")
    print("/25  255.255.255.128")
    print("/26  255.255.255.192")
    print("/27  255.255.255.224")
    print("/28  255.255.255.240")
    print("/29  255.255.255.248")
    print("/30  255.255.255.252")
    print("/31  255.255.255.254")
    print("/32  255.255.255.255")
    print('Jeśli nie ma danej maski w liście to znaczy, że jest ona nie poprawna')
    maska = (input("\nWpisz maske: "))
    maska1 = maska.split('.')

    y = []
    for i in maska:
        if i not in lista2:
            y.append('nie ma')
        else:
            y.append('siema')

    ile = y.count('siema')
    if ile <= 8:
        raise ValueError("zle wpisanie w masce")

    y1 = (int(maska1[0]))
    y2 = (int(maska1[1]))
    y3 = (int(maska1[2]))
    y4 = (int(maska1[3]))

    if y1 > 255:
        raise ValueError("Liczba jest zbyt wysoka w 1 oktecie maski")
    elif y2 > 255:
        raise ValueError("Liczba jest zbyt wysoka w 2 oktecie maski")
    elif y3 > 255:
        raise ValueError("Liczba jest zbyt wysoka w 3 oktecie maski")
    elif y4 > 255:
        raise ValueError("Liczba jest zbyt wysoka w 4 oktecie maski")

    bin_adres_IP = ("{0:08b}.{1:08b}.{2:08b}.{3:08b}".format(x1,x2,x3,x4))
    print(f"\nAdres IP: {adres_IP}/{bin_adres_IP}")
    maska_bin = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(y1, y2, y3, y4))
    print(f"Maska: {maska}/{maska_bin}")


def AND():
    global and1, and2, and3, and4, adres_sieci_int
    and1 = x1 & y1
    and2 = x2 & y2
    and3 = x3 & y3
    and4 = x4 & y4

    adres_sieci_int = (f"{and1}.{and2}.{and3}.{and4}")
    adres_sieci_bin = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(and1),int(and2),int(and3),int(and4)))
    print(f"Adres sieci: {adres_sieci_int}/{adres_sieci_bin}")

def NOT():
    global oktet_neg, wynik_not1, wynik_not2, wynik_not3, wynik_not4, wynik_not, wynik_not_bin
    maska_bin = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(y1, y2, y3, y4))
    oktet_neg = []

    for i1 in maska_bin:
        if i1 == '1':
            xa1 = i1.replace('1', '0')
        else:
            xa1 = i1.replace('0', '1')
        oktet_neg.append(xa1)

    negacja1 = ''.join(map(str, oktet_neg))
    negacja_ = negacja1.split('.')

    liczenie_jedynek1 = (negacja_[0].count(str(1)))
    liczenie_jedynek2 = (negacja_[1].count(str(1)))
    liczenie_jedynek3 = (negacja_[2].count(str(1)))
    liczenie_jedynek4 = (negacja_[3].count(str(1)))

    oktet_liczenie1 = []
    oktet_liczenie2 = []
    oktet_liczenie3 = []
    oktet_liczenie4 = []

    if liczenie_jedynek1 == 0:
        oktet_liczenie1.append(0)
    elif liczenie_jedynek1 == 1:
        oktet_liczenie1.append(1)
    elif liczenie_jedynek1 == 2:
        oktet_liczenie1.append(3)
    elif liczenie_jedynek1 == 3:
        oktet_liczenie1.append(7)
    elif liczenie_jedynek1 == 4:
        oktet_liczenie1.append(15)
    elif liczenie_jedynek1 == 5:
        oktet_liczenie1.append(31)
    elif liczenie_jedynek1 == 6:
        oktet_liczenie1.append(63)
    elif liczenie_jedynek1 == 7:
        oktet_liczenie1.append(127)
    elif liczenie_jedynek1 == 8:
        oktet_liczenie1.append(255)

    if liczenie_jedynek2 == 0:
        oktet_liczenie2.append(0)
    elif liczenie_jedynek2 == 1:
        oktet_liczenie2.append(1)
    elif liczenie_jedynek2 == 2:
        oktet_liczenie2.append(3)
    elif liczenie_jedynek2 == 3:
        oktet_liczenie2.append(7)
    elif liczenie_jedynek2 == 4:
        oktet_liczenie2.append(15)
    elif liczenie_jedynek2 == 5:
        oktet_liczenie2.append(31)
    elif liczenie_jedynek2 == 6:
        oktet_liczenie2.append(63)
    elif liczenie_jedynek2 == 7:
        oktet_liczenie2.append(127)
    elif liczenie_jedynek2 == 8:
        oktet_liczenie2.append(255)

    if liczenie_jedynek3 == 0:
        oktet_liczenie3.append(0)
    elif liczenie_jedynek3 == 1:
        oktet_liczenie3.append(1)
    elif liczenie_jedynek3 == 2:
        oktet_liczenie3.append(3)
    elif liczenie_jedynek3 == 3:
        oktet_liczenie3.append(7)
    elif liczenie_jedynek3 == 4:
        oktet_liczenie3.append(15)
    elif liczenie_jedynek3 == 5:
        oktet_liczenie3.append(31)
    elif liczenie_jedynek3 == 6:
        oktet_liczenie3.append(63)
    elif liczenie_jedynek3 == 7:
        oktet_liczenie3.append(127)
    elif liczenie_jedynek3 == 8:
        oktet_liczenie3.append(255)

    if liczenie_jedynek4 == 0:
        oktet_liczenie4.append(0)
    elif liczenie_jedynek4 == 1:
        oktet_liczenie4.append(1)
    elif liczenie_jedynek4 == 2:
        oktet_liczenie4.append(3)
    elif liczenie_jedynek4 == 3:
        oktet_liczenie4.append(7)
    elif liczenie_jedynek4 == 4:
        oktet_liczenie4.append(15)
    elif liczenie_jedynek4 == 5:
        oktet_liczenie4.append(31)
    elif liczenie_jedynek4 == 6:
        oktet_liczenie4.append(63)
    elif liczenie_jedynek4 == 7:
        oktet_liczenie4.append(127)
    elif liczenie_jedynek4 == 8:
        oktet_liczenie4.append(255)

    potegi1 = ''.join(map(str, oktet_liczenie1))
    potegi1a = int(potegi1)
    potegi2 = ''.join(map(str, oktet_liczenie2))
    potegi2a = int(potegi2)
    potegi3 = ''.join(map(str, oktet_liczenie3))
    potegi3a = int(potegi3)
    potegi4 = ''.join(map(str, oktet_liczenie4))
    potegi4a = int(potegi4)

    wynik_not1 = and1 + potegi1a
    wynik_not2 = and2 + potegi2a
    wynik_not3 = and3 + potegi3a
    wynik_not4 = and4 + potegi4a

    wynik_not = (f"{wynik_not1}.{wynik_not2}.{wynik_not3}.{wynik_not4}")
    wynik_not_bin = ("{0:08b}.{1:08b}.{2:08b}.{3:08b}".format(wynik_not1, wynik_not2, wynik_not3, wynik_not4))
    print(f"Adres rzogłoszeniowy: {wynik_not}/{wynik_not_bin}")

def host():
    global ilosc_hostow
    liczenie_zer = maska_bin.count(str(0))
    host_potega = pow(2, liczenie_zer)
    ilosc_hostow = host_potega - 2

    print(f"Ilość hostów: {ilosc_hostow}")


def host_min_max():
    global host_max, host_min
    a = []
    b = []

    if and4 >= 0:
        a.append(and4 + 1)

    if wynik_not4 > 0:
        b.append(wynik_not4 - 1)

    a1 = ''.join(map(str, a))
    host_min = int(a1)

    b1 = ''.join(map(str, b))
    host_max = int(b1)

    print(f"Host min: {and1}.{and2}.{and3}.{host_min}")
    print(f"Host max: {wynik_not1}.{wynik_not2}.{wynik_not3}.{host_max}")

def wyiki():
    main()
    AND()
    NOT()
    host()
    host_min_max()

def whilee():
    while True:
        wyiki()
        y = input("\nCzy chcesz nadal obliczać? y/n: ")
        if y == 'y':
            continue
        elif y == 'n':
            print("Dziękuje za skorzystanie z naszej usługi <3")
            break
        else:
            raise ValueError("cos poszlo nie tak")

if __name__ == '__main__':
    whilee()