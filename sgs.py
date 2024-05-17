website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# sonuc = 'Hello World'.strip()
sonuc = ' Hello World '
sonuc = ' Hello World '.lstrip() #soldaki boslugu sil
sonuc = ' Hello World '.rstrip() #sağdaki boslugu sil
sonuc = website.lstrip('/:pthw.') #URL'nin başındaki '/', ':', 'pthw', ve '.' karakterlerini kaldırır.

# 3- 'kursAdi' karakter dizisinin tüm karakterlerini küçük harf yapın.
sonuc = kursAdi.lower()

# 'website' içinde kaç tane a karakteri vardır? (count('a'))
sonuc = website.count('a') #sonuc 2 verir.
sonuc = website.count('www') #kac tane 'www' vardır. 1

#bu kod, "website" dizesinin 2 ile 15(2 dahil, 15 hariç) arasındaki karakterlerini (indeks 9 dahil, indeks 15 hariç) alır ve bu alt dize içinde "www" alt dizesinin kaç kez geçtiğini sayar
sonuc = website.count('www',2,15)

# 'website' "www" ile başlayıp başlamadığı?
sonuc = website.startswith('www')

# 'website' "www" ile bitip bitmediği?
sonuc = website.endswith('com')

# 'website' içinde '.com' ifadesi var mı?
# Bu ifade, "website" adlı bir dizede ".com" alt dizesinin ilk bulunduğu indeksi döndürür.
sonuc = website.find('.com') # çıktı 21 olur. 0'dan baslar.

sonuc = website.find('com',0,10) # 0 ile 10. indexler arasında 'com' ifadesi yoktur.
# yani çıktı -1

sonuc = kursAdi.find('Python') #'Python' kaçıncı indexte yer alıyor? 0

sonuc = kursAdi.rindex('Python') # bunu anlamadm
# sonuc = kursAdi.index('React') // HATA VERİR CUNKU BOYLE BİR DİZE YOK

sonuc = "abc1".isalpha() # 'kursAdi' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
sonuc = "123".isdigit() #Bu ifade, "123" karakter dizisinin sadece sayısal karakterlerden oluşup oluşmadığını kontrol eder. 

sonuc = 'Contents'.center(50,'*')
# çıktısı *********************Contents*********************

sonuc = 'Sude'.ljust(50,'*') #soluna sudeyi yerlestirir.
sonuc = 'Gül'.rjust(50,'-') # -----------------------------------------------Gül

# 'kursAdi' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin
sonuc = kursAdi.replace('','-') #bosluklara - atandı. çirkin bişi oldu

# 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
# sonuc = 'Hello World'.replace('World','There')
#çıktı : Hello there

# 'kursAdi' karakter dizisini boşluk karakterlerinden ayırın.
kursAdi = kursAdi.lower().replace(':',"")

sonuc = kursAdi.split() # blok blok ayırır. 'python', 'dersleri', 'sıfırdan'.....

print(sonuc)

