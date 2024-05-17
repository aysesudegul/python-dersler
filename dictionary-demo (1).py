# 1- 3 ürün bilgisini (id,ad,fiyat) kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
# 2- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.


urunler = {
            '100': {'ad': 'IPhone 8', 'fiyat': '5000'}, 
            '101': {'ad': 'IPhone X', 'fiyat': '6000'}, 
            '102': {'ad': 'IPhone XR', 'fiyat': '7000'}
        }

# id = input('id: ')
# ad = input('ad: ')
# fiyat = input('fiyat: ')

# urunler[id] = {
#     "ad": ad,
#     "fiyat": fiyat
# }

# id = input('id: ')
# ad = input('ad: ')
# fiyat = input('fiyat: ')

# urunler[id] = {
#     "ad": ad,
#     "fiyat": fiyat
# }


# id = input('id: ')
# ad = input('ad: ')
# fiyat = input('fiyat: ')

# urunler[id] = {
#     "ad": ad,
#     "fiyat": fiyat
# }

id = input('aramak istediğiniz ürün id: ')
urun = urunler[id]


#Python'da, f-string (format string) ifadeleri, metin içinde değişkenlerin veya ifadelerin değerlerini doğrudan yerleştirmeyi sağlayan bir formattır. Bu, daha önceki Python sürümlerinde kullanılan % operatörü veya str.format() metodu yerine daha okunaklı ve kullanımı kolay bir yöntem sunar.
print(f'id: {id} ürün adı: {urun["ad"]} ürün fiyatı: {urun["fiyat"]}')
# print(urunler)

