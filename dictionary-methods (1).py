opelObj = {
    "marka": "Opel",
    "model": "Corsa",
    "yil": 2020
}

sonuc = opelObj["marka"]
sonuc = opelObj.get("marka")

# for x in opelObj:
#     print(x)

# for x in opelObj:
#     print(opelObj[x])

# for x in opelObj.values():
#     print(x)

# for x,y in opelObj.items():
#     print(x,y)

# sonuc = "marka" in opelObj
# sonuc = len(opelObj)
# opelObj["renk"] = "kırmızı"
# opelObj.pop("renk") # pop öğe çıkarmak için kullanılan
# opelObj.popitem()

# del opelObj["marka"]
# del opelObj #kendisini sildik. objenin
# opelObj.clear() #içindeki elemanlar silindi.

obj = opelObj.copy() # referans. kopyaladık. ikisi de aynı adres no tutan iki bilgi. birbirini etkiler.
obj["marka"] = "Mazda"

#update işlemi yapıyorum. değiştirme işlemleri
opelObj.update({
    "marka": "Bmw",
    "renk": "Kırmızı"
})

# print(sonuc)
print(obj)
print(opelObj)