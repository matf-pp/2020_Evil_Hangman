import pygame
import random

pygame.init()
visina_prozora = 680
sirina_prozora = 1350
prozor=pygame.display.set_mode((sirina_prozora, visina_prozora))

CRNA = (0, 0, 0)

slike = [pygame.image.load('il2.png'), pygame.image.load('il3.png'), pygame.image.load('il4.png'), pygame.image.load('il5.png'), pygame.image.load('il6.png'), pygame.image.load('il7.png'), pygame.image.load('il1.png')]

rec = ''
buttons = []
#font dugmadi
font_dugmad = pygame.font.SysFont("courier", 20)

pokusana_slova = []
#font ispisa
font_pogodak = pygame.font.SysFont("courier", 24)

sound = 'hangman.mp3'
pygame.mixer.init()
pygame.mixer.music.load(sound)
pygame.mixer.music.play(-1, 0.0)

#font za ispis reci na kraju igre
font_kraj = pygame.font.SysFont('courier', 45)

#inicijalizacija za deo slike, na pocetku je iscrtavanje samo prve slike u nizu
delovi = 0
#ovom funkcijom iscrtavamo prozor igre
def crtanje_prozora():
    global slike
    global delovi
    global pokusana_slova
    SVETLOZELENA=(208,240,192)
    prozor.fill(SVETLOZELENA)
    
    #dodavanje dugmadi - odredjivanje oblika(kvadrat), fonta slova na njima, pozicije u prozoru - pozicija mozda nije dobra, gledacemo ponovo
    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.rect(prozor, CRNA, (buttons[i][1], buttons[i][2], buttons[i][3], buttons[i][3]),4)
            pygame.draw.rect(prozor, buttons[i][0], (buttons[i][1], buttons[i][2], buttons[i][3], buttons[i][3]))
            label = font_dugmad.render(chr(buttons[i][5]), 1, CRNA)
            prozor.blit(label, (buttons[i][1] + (label.get_width()/1.5), buttons[i][2] + (label.get_height() / 6)))
      
    #dodavanje labele za ispis slova na prozoru
    label1 = font_pogodak.render(ispis(rec,pokusana_slova), 1, CRNA)
    rect = label1.get_rect() #izmena, uzimamo dimenzije prozora
    duzina = rect[2] #y koordinata
    prozor.blit(label1,(sirina_prozora/3 - duzina/3, 450)) #da ne bi bilo fiksno i ako je predugacka rec, izlazi van prozora, ovako ce polozaj da se menja u zavisnosti od duzine reci
    
    labela_broj = font_kraj.render("Broj preostalih reci: " + str(len(preostale_reci)), 1, CRNA)
    prozor.blit(labela_broj ,(50, 550)) #labela koliko je ostalo reci
    
    #dodavanje dugmeta za pomoc
    if greenbutton:
        greenbutton.draw(prozor)
    
    slika = slike[delovi]
    prozor.blit(slika, (sirina_prozora/15 - slika.get_width()/3 +10, 100))#ovaj deo pomera sliku
    pygame.display.update()
    
#definisem funkciju koja ce da ispisuje slova reci na prozoru - crtice su na pocetku jer nije bilo pogodaka
def ispis(rec, pogodak=[]): 
    pog_slova= pogodak
    r_ispis = ''
    for x in range(len(rec)):
        r_ispis += '__ ' #stavicu onoliko crtica(dve crtice za jedno slovo) koliko imam slova u reci koju pogadjam
        for i in range(len(pog_slova)): 
            if rec[x] == pog_slova[i]: #ako je slovo reci koje se pogadja bas ono koje smo izabrali..
                r_ispis = r_ispis[:-3] # ovo radim da bih izbisala dve crtice i belinu, i umesto nje dodala slovo
                r_ispis += rec[x].upper() + '  ' # .. ovde zamenim crticu velikim slovom koje smo izabrali (moze i malo, ali deluje mi lepse da je veliko :))

    return r_ispis    

#funkcija koja na osnovu koordinata koje dobije vraca koja dugme(odnosno slovo) kliknuli
def klik_dugme(x, y):
    for i in range(len(buttons)):
        if x < buttons[i][1] + 25 and x > buttons[i][1] - 25:
            if y < buttons[i][2] + 24 and y > buttons[i][2] - 24:
                return buttons[i][5]
    return None



class button():
    
    def __init__(self, boja, x,y,sirina,visina, text=''):
        self.color = boja
        self.x = x
        self.y = y
        self.width = sirina
        self.height = visina
        self.text = text
        self.self = True

    def draw(self,win,out=None):
       
        if out:
            pygame.draw.rect(win, out, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('courier', 40)
            text = font.render(self.text, 1, CRNA)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def klik(self, pos):
      
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False



def vrati_duzinu(reci):
    duzine_reci =[]
    for r in reci:
        duz = r.__len__()
        if(duz not in duzine_reci):
            duzine_reci.append(duz) #lista duzina reci
             
    duzine_reci.sort()
    
    duz = duzine_reci[int( random.randint(2,20))]
    return duz

#postavljanje pocetnih stanja reci - zelimo ovom funkcijom da dobijemo odredjen oblik reci koji koristimo da bismo ostigli da bude evil
def postavi_stanje(duzina_reci):
    stanje = ""
    while duzina_reci > 0:
        stanje += "-"
        duzina_reci = duzina_reci- 1 #ovo su zapravo stanja na pocetku, pa su samo crtice, menjacemo ih slovima kasnije u programu, to je ideja
    return stanje

# vrati listu svih reci sa datom duzinom
def postavi_preostale(lines, duzina):
    words = []
    for r in lines:
        if(r.__len__() == duzina):
            words.append(r)
    return words

#azuriranje stanje (dodavanje slova ukoliko je potrebno)
def vrati_stanje(r_familija, pokusana_slova):
    stanje = ""
    for s in r_familija:
        if(s in pokusana_slova):
            stanje += s
        else: 
            stanje += "-"
    return stanje
 
#lista preostalih reci
def vrati_preostale(slovo, preostale_reci, broj_pokusaja, rec_duzina):  
    familije_reci = postavi_familije(preostale_reci, slovo) #reci koje imaju isto stanje

    familija = postavi_stanje(rec_duzina) #pocetno stanje za daru duzinu
    
    if(broj_pokusaja == 0 and familija in familije_reci): 
        familija = postavi_stanje(rec_duzina) #nista nismo pogodili i varacamo (pocetno)stanje reci date duzine
    else:
        familija = vrati_najvecu(familije_reci) # ako jos nismo izgubili vracamo najvecu mogucu familiju reci

    words = postavi_listu(preostale_reci, slovo, familija) #postavljamo listu reci na osnovu familije
    return words
    
#pravimo mapu - status reci(bice to rec koja sadzi crtice  i slova koja smo pogodili)kao kljuc, a vrednost ce biti br reci sa istim statusom(istim oblikom)    
def postavi_familije(preostale_reci, slovo):
    familije_reci = dict() #recnik
    for r in preostale_reci: #preostale reci su reci koje imaju isti br slova kao ona koja je data
        status = "" #na pocetku nista
        for s in r: 
            if(s != slovo):
                status += "-"
            else:
                status += slovo
        #sko takav oblik reci ne postoji u recniku        
        if(status not in familije_reci):
            familije_reci[status] = 1
        else:
            familije_reci[status] = familije_reci[status] + 1 #samo dodajemo br reci sa takvim statusom
    return familije_reci

#pravimo novu listu na osnovu familije koja sadrzi sve reci sa istim stanjem
def postavi_listu(preostale_reci, slovo, familija):
    words = []
    for r in preostale_reci:
        r_familija = ""
        for s in r: #pravimo familiju reci
            if(s == slovo):
                r_familija += slovo
            else:
                r_familija += "-"
         #ako je nasa familija jednaka datoj familiji onda tu rec dodajemo u listu words       
        if(r_familija == familija):
            words.append(r)
    return words

#vracamo onu familiju(one reci koje imaju status kao ona koju pogadjamo) sa najvecim brojem reci u sebi
def vrati_najvecu(familije_reci):
    najveca_familija = "" #inicijalizacija na pocetku, nemamo najvecu, trazimo je u for-u
    maksimum = 0
    for familija in familije_reci:
        if familije_reci[familija] > maksimum:
            maksimum = familije_reci[familija]
            najveca_familija = familija
    return najveca_familija


#iscrtavanje poruke o pobedi ili porazu
def kraj(pobednik, rec):
    global delovi
    ZELENA=(85, 107, 47)
    
    crtanje_prozora()
    pygame.time.delay(1000)
    prozor.fill(ZELENA)

    poruka_poraz = 'Izgubili ste!!'
    poruka_pobeda = 'POBEDA!'
    if pobednik == True:
        label = font_kraj.render(poruka_pobeda, 1, CRNA)
    else:
        #iscrtavamo sliku u slucaju poraza
        label = font_kraj.render(poruka_poraz, 1, CRNA)
        slika = slike[6]
        prozor.blit(slika, (sirina_prozora/15 - slika.get_width()/3 +10, 50))
        
    #ispisivanje trazene reci na kraju igre na prozoru    
    rec_tekst = font_kraj.render(rec.upper(), 1, CRNA)
    poruka_rec = font_kraj.render('Rec je bila: ', 1, CRNA)
    prozor.blit(rec_tekst, (sirina_prozora/2 - rec_tekst.get_width()/2, 295))
    prozor.blit(poruka_rec, (sirina_prozora/2 - poruka_rec.get_width()/2, 245))
    
    prozor.blit(label, (sirina_prozora / 2 - label.get_width() / 2,100))#dodavanje labele za ispis da li smo pobedili ili izgubili
  
    pygame.display.update()
    
    #ponovno pokretanje igre
    again = True
    while again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #ukoliko smo kliknuli na x onda gasim prozor i izlazimo iz igrice 
                pygame.quit()
            if event.type == pygame.KEYDOWN: #ukoliko se unese nesto sa tastature pokrece se nova igra
                again = False
    restart() #pokrecemo novu igru


def restart():
    global rec_duzina
    global broj_pokusaja
    global preostale_reci
    global trenutno_stanje
    global buttons
    global pokusana_slova
    global greenbutton

    rec_duzina = vrati_duzinu(reci)
    broj_pokusaja = 5
    
    preostale_reci = postavi_preostale(reci, rec_duzina)
    trenutno_stanje = postavi_stanje(rec_duzina)
    pokusana_slova =[]       
    
    global rec
    rec=trenutno_stanje
        
    for i in range(len(buttons)):
        buttons[i][4] = True
        
    greenbutton  = button(ZELENA, 900, 200, 300,80,'HELP MEEE')
   
    crtanje_prozora()
    global delovi
    delovi = 0
    global m
    m = 0

# namestanje dugmica
d = round(sirina_prozora / 13) #uvecanje prilikom iscrtavanja kvadratica
ZELENA=(85, 107, 47)
for i in range(27):
    if i < 13:
        y = 40
        x = 25 + (d * i)
    else:
        x = 25 + (d * (i - 13))
        y = 85
    buttons.append([ZELENA, x, y, 30, True, 97 + i])

#citanje reci iz datoteke
with open('reci.txt') as file:
    reci = file.read().splitlines()

# inicijalizacija pre pocetka igre
rec_duzina = vrati_duzinu(reci) #uzimamo random duzinu reci
broj_pokusaja = 5 #ovoliko pokusaja imamo zbog slika

preostale_reci = postavi_preostale(reci, rec_duzina) #pravimolistu reci koje imaju datu duzinu i to nam je pocetna lista
trenutno_stanje = postavi_stanje(rec_duzina) #pocetno stanje 
pokusana_slova =[] #na pocetku je to prazna lista
rec = trenutno_stanje #rec mora da bude trenutno stanje jer ne mozemo da uzimamo random rec iz liste preostale_reci jer ce ta lista stalno da se menja (jer je evil hangman)


     
igra = True
greenbutton  = button(ZELENA, 900, 200, 300, 80,'HELP MEEE')
# m kao brojac pritiska dugmeta za pomoc
m = 0
while igra:
    crtanje_prozora()
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            igra = False    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                igra = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pozicija_misa = pygame.mouse.get_pos()
            if greenbutton and greenbutton.klik(pozicija_misa) and delovi>0:
                delovi -= 1
                m += 1
                if m>=2:
                    greenbutton = False
                    m = 0
            slovo = klik_dugme(pozicija_misa[0], pozicija_misa[1])
            if slovo != None:
                pokusana_slova.append((chr(slovo)))
                buttons[slovo - 97][4] = False
                preostale_reci = vrati_preostale(chr(slovo), preostale_reci, broj_pokusaja, rec_duzina)
                trenutno_stanje = vrati_stanje(preostale_reci[0], pokusana_slova)
                rec = trenutno_stanje
                if chr(slovo) not in trenutno_stanje:
                    if delovi != 5:
                        delovi += 1
                        broj_pokusaja -= 1
                        
                    else:#izgubio
                        kraj(False, preostale_reci[0])
                    
                else:
                    if ispis(trenutno_stanje, pokusana_slova).count('_') == 0:#pobedio
                        kraj(True, trenutno_stanje)


pygame.quit()
