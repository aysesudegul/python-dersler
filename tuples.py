#tuple kullanmak uygulamamızı daha performanslı hale getirir.
#vt bilgileri tuple icine aldık. eleman eklemek istiyoruz, kabul edilemez. append remove metodları kullanılamaz
_list = [1,2,3]
_tuple = (1,"iki",True)
_tuple2 = (3,"dört",True)

# print(type(_list)) #<class 'list'> : ÇIKTISI
# print(type(_tuple)) # <class 'tuple'> : ÇIKTISI
 
print(_list[1])
print(_tuple[1])

print(len(_list))
print(len(_tuple))

# _list[0]=5 # BURASI HATALI CUNKU DEGİSTİRİLEMEZ!
_list.append(4)

# _tuple.append(5) #HATA VERİR

print(_tuple.count(1)) #kac tane 1 var saydır ekrana yaz
print(_tuple + _tuple2) #2 tane tuple bilgisi ekrana yazdırır.


#var olan listeyi tuple a çevirmek
_t = tuple([3,4,5])
print(type(_t))
print(_t)

print(_list)
print(_tuple)