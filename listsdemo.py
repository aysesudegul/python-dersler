marka = ["Samsung", "Samsung S6", "Samsung S7", "Samsung S8"]
sonuc = marka
# print(sonuc)

# sonuc = len(marka) #liste kac elemanlı
# print(sonuc)

# print(marka[0]) # listenin ilk elemanı
# print(marka[3]) # son elemanı

#Samsung S5 değerini Samsung S9 ile değiştirdim
 # marka[0] = "Samsung S9" 
 # sonuc = marka


# if "Samsung S6" in marka:
  #  print("evet elemanıdır")

#Listenin -3 indeksindeki değer?
# sonuc = marka[-3]
# print(sonuc) # çıktı Samsung S6

#listenin ilk 2 elemanı;
# sonuc = marka[:2]
# print(sonuc)

#listenin son 2 elemanı yerine "Samsung S9" ve "Samsung S10" değerlerini ekleyin
# sonuc = marka[-2:] = ["Samsung S9","Samsung S10"]
# sonuc = marka
# print(sonuc)

#listenin üzerine "İphone X" ve "İphone XR" değerlerini ekleyin.
# sonuc = marka + ["İphone X","İphone XR"]
# print(sonuc)

#listenin son elemanını silin
# del telefonlar[-1]
# sonuc = marka

#liste elemanlarını tersten yazdırın
# sonuc = marka[::-1]
# print(sonuc)

#liste elemanlarını ekrana yazdır
# for a in marka:
  # print(a)

#asagıdakı verileri 1 liste icinde saklayın
# kullaniciA: Ayşe Sude 2001, (80,90,100)
# kullaniciB: Murat Mutlu 2000, (80,85,95)
# kullaniciC : Simge Tiryaki 2003, (100,85,95)

ogrenciA = ["Ayşe","Sude",2001,[80,90,100]]
ogrenciB = ["Murat","Mutlu",2000,[80,85,95]]
ogrenciC = ["Simge","Tiryaki",2003,[100,85,95]]

ogrenciler = [ogrenciA,ogrenciB,ogrenciC]
#ogrencilerin yasını hesaplayıp getirttik ve notların ortalamalarını buldurttuk
for ogrenci in ogrenciler:
    ad = ogrenci[0]
    soyad = ogrenci[1][3]
    yas = 2024-ogrenci[2]
    ortalama = (ogrenci[3][0] + ogrenci[3][1] + ogrenci[3][2]) / 3

    print(f"{ad} {soyad} {yas} {ortalama}")


print(sonuc)
