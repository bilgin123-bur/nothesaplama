## not hesaplama

AA = 4
AB = 3.7
BA = 3.3
BB = 3
BC = 2.7
CB = 2.3
CC = 2
CD = 1.7
DC = 1.3
DD = 1
FF = 0

anlikortalama = 2 # genel not ortalamanızı girin
toplamalinankredi = 213.5# toplam aldığınız krediyi girin
akts = anlikortalama * toplamalinankredi

#derslerin kredisi * harf notunuzu yazın

ders1 = 7.5 * BB
ders2 = 6 * BB
ders3 = 5 * BB
ders4 = 4 * BB
ders5 = 7 * BB
ders6 = 6.5 * BB
ders7 = 7 * BB

# bu dönem aldığınız toplam kredi sayisini giriniz:
donemkredi = 43 # 43'Ü SİLİP KENDİ KREDİNİZİ YAZİN

akts = akts + ders1 + ders2 + ders3 + ders4 + ders5 + ders6 + ders7
donemakts= ders1 + ders2 + ders3 + ders4 + ders5 + ders6 + ders7
donemortalamasi = donemakts/(donemkredi) #("bu dönem aldığınız ders kredinizi girin")

#bu dönem sonunda alınan toplam kredinizi girin
toplamalinankredi = toplamalinankredi + donemkredi#toplam alınan kredinizi girin


ortalama = akts / toplamalinankredi

print("muhtemelen gno:", ortalama)
print("muhtemelen dno:", donemortalamasi)
