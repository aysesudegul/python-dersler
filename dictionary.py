# key - value

# 41 => Kocaeli
# 34 => İstanbul

sehirler = ['kocaeli','istanbul']
plakalar = [41,34]

# print(plakalar[0],sehirler[0])
# print(plakalar[1],sehirler[1])

#İstanbul'un plaka kodu nedir? 
# print(plakalar[sehirler.index('istanbul')]) #34 
# print(plakalar[sehirler.index('kocaeli')]) #41

# plakalar = {"kocaeli" : 41, "istanbul": 34}
# print(plakalar["kocaeli"])
# print(plakalar["istanbul"])

# plakalar['rize'] = 53
# plakalar['tekirdağ'] = 58
# plakalar['tekirdağ'] = 59
#direkt değiştiriyor. 
# print(plakalar)

ogrenciler = {
    100: {
        "ad" : "Ayşe",
        "soyad" : "Gül",
        "yas" : 23,
        "notlar" : [75,80,70]
    },
    101: {
        "ad": "Simge",
        "soyad" : "Nur",
        "yas" : 20,
    
    }
}

sonuc = ogrenciler[100]
sonuc = ogrenciler[101]["ad"]
sonuc = ogrenciler[101]["soyad"]
sonuc = ogrenciler[100]["notlar"][0]

#sudenin not ortalaması
sonuc = (ogrenciler[100]["notlar"][0] + ogrenciler[100]["notlar"][1] + ogrenciler[100]["notlar"][2]) / 3


print(sonuc)

# print(ogrenciler[100]) # cıktı Sude olur

