#Ödev cevaplar
from queue import PriorityQueue


cars=['BMW','Mercedes','Opel','Mazda']
print(f'2-listede kaç elaman var ? :  {len(cars)}') 
print(f'3-Listenin ilk ve son elemanları : {cars[0],cars[-1]}')

cars[3]='Toyota' ; print(f'4-Mazda değerini Toyota il değiştirin sonuç: {cars[3]}')

merso='Mercedes' in cars ; print(f'5-Mercedes listenin bir elemanı mı? {merso}') 

print(f'6-Listenin 2. indeksi : {cars[2]}')
print(f'7-Listenin ilk 3 elamını : {cars[:3]}')

cars[-2:]=['Toyota','Renault']  ; print(f'8-Listenin son 2 elmanı yerine Toyota ve Renault yazıldı : {cars}')

result=cars + ['Audi', 'Nissan']  ;  print(f'9-Listeye Audi ve Nissan  eklendi : {result}')

del cars[-1] ; result  = cars ;  print(f'listenin son elemanı silindi : {result}')
result= cars[::-1] ;  print(f'listenin elemanlarını tersten yazdırdık :  {result}')

studentA=['Şüheda','Altunöz',1998,[70,60,70]]
studentB=['Mücahit','Altunöz',1993,[50,60,40]]
studentC=['Merve','Altunöz',1992,[90,80,100]]

aResult=studentA[0] ;print(f'studentA nın 0 indexi : {aResult}')
bResult=studentB[3] ; print(f'studentB nın 3 indexi : {bResult}')
bResult=studentB[3][0] ; print(f'studentB nın 3 indexin 0 indexi : {bResult}')

ortalama = f'{studentA[0]} {studentB[1] } yaş {2022-studentA[2]} not ortalaması: {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}' ;print(ortalama) 