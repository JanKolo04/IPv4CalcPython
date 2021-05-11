from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
#widget
    def create_widgets(self):
        self.inst_lbl1 = Label(self, text = "Wprowadź Adres IP:")
        self.inst_lbl1.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        self.inst_lbl2 = Label(self, text = "Wprowadź maskę:")
        self.inst_lbl2.grid(row = 2, column = 0, columnspan = 2, sticky = W)
        #wpis liczby
        self.pw_ent1 = Entry(self)
        self.pw_ent1.grid(row = 1, column = 0, sticky = W)
        self.pw_ent2 = Entry(self)
        self.pw_ent2.grid(row = 3, column = 0, sticky = W)
        #button run
        self.submit_bttn = Button(self, text = "Run", command = self.reveal)
        self.submit_bttn.grid(row = 4, column = 0, sticky = W)
        #rozwiazania
        self.secret_txt1 = Text(self, width=60, height=2, wrap=WORD)
        self.secret_txt1.grid(row=5, column=0, columnspan=2, sticky=W)

        self.secret_txt2 = Text(self, width=60, height=2, wrap=WORD)
        self.secret_txt2.grid(row=6, column=0, columnspan=2, sticky=W)

        self.secret_txt3 = Text(self, width=60, height=2, wrap=WORD)
        self.secret_txt3.grid(row=7, column=0, columnspan=2, sticky=W)

        self.secret_txt4 = Text(self, width=60, height=2, wrap=WORD)
        self.secret_txt4.grid(row=8, column=0, columnspan=2, sticky=W)

        self.secret_txt5 = Text(self, width=60, height=2, wrap=WORD)
        self.secret_txt5.grid(row=9, column=0, columnspan=2, sticky=W)

        self.secret_txt6 = Text(self, width=60, height=2, wrap=WORD)
        self.secret_txt6.grid(row=10, column=0, columnspan=2, sticky=W)

        self.secret_txt7 = Text(self, width=60, height=2, wrap=WORD)
        self.secret_txt7.grid(row=11, column=0, columnspan=2, sticky=W)

#przeliczanie
    def reveal(self):

        adres_IP = self.pw_ent1.get()
        maska = self.pw_ent2.get()

        # oktety
        ip = adres_IP.split('.')
        maska1 = maska.split('.')

        x1 = (int(ip[0]))
        x2 = (int(ip[1]))
        x3 = (int(ip[2]))
        x4 = (int(ip[3]))

        y1 = (int(maska1[0]))
        y2 = (int(maska1[1]))
        y3 = (int(maska1[2]))
        y4 = (int(maska1[3]))

        # ERROR
        if x1 > 255:
            raise ValueError("Liczba jest zbyt wysoka")
        elif x2 > 255:
            raise ValueError("Liczba jest zbyt wysoka")
        elif x3 > 255:
            raise ValueError("Liczba jest zbyt wysoka")
        elif x4 > 255:
            raise ValueError("Liczba jest zbyt wysoka")
        elif y1 > 255:
            raise ValueError("Liczba jest zbyt wysoka")
        elif y2 > 255:
            raise ValueError("Liczba jest zbyt wysoka")
        elif y3 > 255:
            raise ValueError("Liczba jest zbyt wysoka")
        elif y4 > 255:
            raise ValueError("Liczba jest zbyt wysoka")

        # bramka AND
        and1 = x1 & y1
        and2 = x2 & y2
        and3 = x3 & y3
        and4 = x4 & y4

        adres_sieci_int = (f"{and1}.{and2}.{and3}.{and4}")
        adres_sieci_bin = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(and1), int(and2), int(and3), int(and4)))

        # maska i ip mw bin
        ip_bin = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(x1, x2, x3, x4))
        maska_bin = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(y1, y2, y3, y4))

        # bramka NOT
        oktet_neg = []

        for i1 in maska_bin:
            if i1 == '1':
                x1 = i1.replace('1', '0')
            else:
                x1 = i1.replace('0', '1')
            oktet_neg.append(x1)

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
        wynik_not_str = wynik_not.split('.')
        wynik_not_bin = ("{0:08b}.{1:08b}.{2:08b}.{3:08b}".format(wynik_not1, wynik_not2, wynik_not3, wynik_not4))

        # host
        liczenie_zer = maska_bin.count(str(0))
        host_potega = pow(2, liczenie_zer)
        ilosc_hostow = host_potega - 2

        # host max i min
        a = []
        b = []

        if and4 == 0:
            a.append(and4 + 1)

        if wynik_not4 > 0:
            b.append(wynik_not4 - 1)

        a1 = ''.join(map(str, a))
        host_min = int(a1)

        b1 = ''.join(map(str, b))
        host_max = int(b1)

        # wyniki
        Adres_IP_wynik = (f"\nAdres IP: {adres_IP}/{ip_bin}")
        Maska_wynik = (f"Maska: {maska}/{maska_bin}")
        Adres_sieci_wynik = (f"Adres sieci: {adres_sieci_int}/{adres_sieci_bin}")
        Adres_rozg_wynik = (f"Adres rozgłoszeniowy: {wynik_not}/{wynik_not_bin}")
        Ilosc_hostow_wynik = (f"Ilość hostów: {ilosc_hostow}")
        Host_min_wynik = (f"Host min: {and1}.{and2}.{and3}.{host_min}")
        Host_max_wynik = (f"Host max: {wynik_not1}.{wynik_not2}.{wynik_not3}.{host_max}")


        self.secret_txt1.delete(0.0, END)
        self.secret_txt1.insert(0.0, Adres_IP_wynik)

        self.secret_txt2.delete(0.1, END)
        self.secret_txt2.insert(0.1, Maska_wynik)

        self.secret_txt3.delete(0.2, END)
        self.secret_txt3.insert(0.2, Adres_sieci_wynik)

        self.secret_txt4.delete(0.3, END)
        self.secret_txt4.insert(0.3, Adres_rozg_wynik)

        self.secret_txt5.delete(0.4, END)
        self.secret_txt5.insert(0.4, Ilosc_hostow_wynik)

        self.secret_txt6.delete(0.5, END)
        self.secret_txt6.insert(0.5, Host_min_wynik)

        self.secret_txt7.delete(0.6, END)
        self.secret_txt7.insert(0.6, Host_max_wynik)


root = Tk()
root.title("Kalkulator progrmaisty")
root.geometry("430x400")
app = Application(root)
root.mainloop()