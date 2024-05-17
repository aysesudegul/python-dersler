# list
# tuple eleman ekleme iht. yoksa kullanılır.
# dictionary #acıklanabilir. key value
# sets => indekslenemez, sıralanamaz
#sıralama onemli değilse,ekleme çıkarma yapmak istiyorsak ancak var olanı değiştirmek istemiyorsak



meyveler = {"elma","kiraz","kavun","üzüm"}
sebzeler = {"bezelye","soğan"}

# sonuc = meyveler[0] #hata verir.indekslenemez
sonuc = "elma" in meyveler #True bilgisi gelir
meyveler.add("karpuz") #karpuz ekledim
meyveler.update(["vişne","kavun"])
#kavun ztn var var olan bilgi yineden eklenmez

sonuc = len(meyveler) #kac eleman var
# meyveler.remove("karpuz") #karpuz bilgisini sildik


# sonuc = meyveler.pop()
# meyveler.clear() #elemanları sildik

meyveler.union(sebzeler) #meyveler ve sebzeleri birleştirdik


sonuc = meyveler

#elemanları tek tek yazdırdık.
for x in meyveler:
    print(x)


print(sonuc)

