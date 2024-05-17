diller = ["Python","C#","Java","Javascript","React"]

sonuc = diller
sonuc = type(diller)
sonuc = diller[0]

#0dan basla 2ye kdr al(2dahil olmaz)
sonuc = diller[0:2]

#2den basla(dahil) sonuna kadar al
sonuc = diller[2:]

#baslangıctan 3e kadar al
sonuc = diller[:3]

sonuc = diller[-1] #react bilgisi gelir.

sonuc = [diller[-4:-1]] #c#dan baslar javascript dahil alır. son index dahil degil

#React bilgisi HTML olarak degistirdik.
diller[-1]="HTML"
sonuc = len(diller) #liste kaç elemanlı?

#liste üzerine iki tane eleman ekledik
sonuc = diller + ["Angular","Vuejs"]

#bir değer liste içinde mi değil mi
#if bloğu = koşul ifadeleri
if "Python" in diller:
    print("değer listenin bi elemanı")

#döngüler
for x in diller: 
    print(x)

#bir elemanı liste icinden nası sileriz
del diller[0]

sonuc = diller

print(sonuc)