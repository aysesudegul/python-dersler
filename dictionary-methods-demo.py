'''
    player 1: 
        id           => 1
        name         => Cristiano Ronaldo
        yearOfBirth  => 1985
        nationality  => Portugal
        current_team => Portugal
        history      => Juventus,Real Madrid,Portugal

    player 2: 
        id           => 2
        name         => Lionel Messi
        yearOfBirth  => 1987
        nationality  => Argentina
        current_team => Barcelona,
        history      => Barcelona,Argentina,Portugal
'''
players = {
    '2':
    {
        'name': 'Lionel Messi', 'yearOfBirth': '1987', 'nationality': 'Argentina', 'current_team': 'Barcelona', 'history': ['Barcelona', 'Argentina', 'Portugal']
     },
    
    '1':
        {
        'name': 'Cristiano Ronaldo', 'yearOfBirth': '1985', 'nationality': 'Portugal', 'current_team': 'Portugal', 'history': ['Juventus', 'Real Madrid', 'Portugal']
         }
         }


# # 1- Yukarıda verilen bilgileri liste içerisinde saklayınız.
# players = {}
# id = input('oyuncu id: ')
# name = input('oyuncu ad: ')
# nationality = input('ülke: ')
# yearOfBirth = input('doğum yılı: ')
# current_team = input('takım: ')
# history = input('oynadığı yerler: ')

# #gelen bilgileri kaydedecegiz
# players.update({
#     id : {
#         "name": name,
#         "yearOfBirth" : yearOfBirth,
#         "nationality" : nationality,
#         "yearOfBirth" : yearOfBirth,
#         "current_team" : current_team,
#         "history" : history.split(',') #virgullerle ayırarak içine at. split
#     }
# })


print(players)

# 2- id' e göre arama yapınız.

# id = input('aramak istediğiniz oyuncu id: ')
# player = players.get(id)
# print(f'name: {player.get("name")}')
#ÇIKTI:
#aramak istediğiniz oyuncu id: 1
# name: Cristiano Ronaldo


# 3- id' e göre bilgi kayıt siliniz.
id = input('silmek istediğiniz oyuncu id: ')
players.pop(id)
#sadece 2 numaralı kaydı getirir.1'i siler
print(players)

