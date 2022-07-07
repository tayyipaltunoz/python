#dictionary = {'key' : value}

plakalar = {'İstanbul' : 34,'Tokat' : 60}

print(plakalar['Tokat'])     # burada 60 sonucu verir

plakalar['Ankara'] = 6  ; print(plakalar)  #dictionary yeni değer ekleme

plakalar['Ankara'] = '06'  ; print(plakalar)



users = {
    'tayyipaltunoz': {
        'age' : 26,
        'roles' : ['admin','user'],
        'email':'tayyip@gmail.com',
        'adress' :'istanbul',
        'phone' : '123456789'
    },
    'turanaltunoz': {
        'age' : 58,
        'email':'turan@gmail.com',
        'adress' :'kayaşehir',
        'phone' : '897564321'
    }
}

print(f'tüm userlar : {users} tayyipaltunoz userı : {users["tayyipaltunoz"]}')
print(users['tayyipaltunoz']['age'])   #tayyipaltunoz userının yaşını verir

print(users["tayyipaltunoz"]['roles'][0])  #dictionary içindeki userın içindeki rolelerden 0 indexi yazdır