msg = "Python Kursumuza Hoş Geldiniz. Ben Sadık Turan.".split()
#split ile her kelime bir index oldu.
#0 dan baslar!


sayilar = [1,3,5,7,9]
sonuc = sayilar[0]
sonuc = sayilar[4]

isimler = ['ahmet','sude','mustafa','gül']
sonuc = isimler[0]
# print(type(isimler[0])) #isimlerin veri tipini ekrana yazdırdık
#cıktı str.

listeAhmet =['ahmet',20]
listeAli =['ali',22]
sonuc = listeAhmet[1] #çıktımız 20 olacak mesela.

# ogrenciler = [["ahmet",20],["ali",22]]
# sonuc = ogrenciler[0][1] #20 çıktısını verir.
# sonuc = ogrenciler[1][1] #22 cıktısını verir.

# yukarıdaki gibi yapmak yerine;
ogrenciler = [listeAhmet,listeAli]
sonuc = ogrenciler[0][0]  #ahmet cıktısını verir.




print(sonuc)


# print(msg[0][0]) #kelimenin kendi içinde 0. indexi getirir

