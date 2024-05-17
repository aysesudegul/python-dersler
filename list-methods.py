sayilar = [1,5,8,9,3,45,77,5]
harfler = ['a','b','e','s','a','y']

sonuc = min(sayilar) #0 bilgisi gelir
sonuc = max(sayilar) #77 gelir
sonuc = min(harfler) #a gelir
sonuc = max(harfler) #y gelir

# ekleme
#append = liste icine ekleme yapar
sayilar.append(10) 
#insert = herhangi bir konuma ekleme yapar
sayilar.insert(3,5) #3 numaralı indekse 5 değerini ekler
sayilar.insert(-1,50) #-1. indekse gelir -1in önüne eklenmiş olur
sayilar.insert(len(sayilar),150)

# silme
sayilar.pop() #listenin en sonundan eleman sil
sayilar.pop(0) #indks no vererek 1i silerim
sayilar.remove(45) #45 değerini silerim
harfler.remove('y') #y harfini silerim

# sıralama
sayilar.sort() 
harfler.sort()
sayilar.reverse() #ters bi sekilde getirir. 

# print(sayilar.count(5))
# print(harfler.count('a'))

print(sayilar.index(3)) #3 sayısının indeksini arıyoruz. kaçıncı indekste?
sayilar.clear() #liste elemanlarının hepsini sil.

sonuc = sayilar
# sonuc = harfler

print(sonuc)