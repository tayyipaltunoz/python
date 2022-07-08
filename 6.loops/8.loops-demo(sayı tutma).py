#random ile 1-100 arasında bir sayı üretin ve aşağı yukarı ifadeleri ile buldurmaya çalışın.
#**100 üzerinden puanlama yapın her soru 20 puan

import random

randomSayi = random.randint(1,100)

print(randomSayi)


hak = int(input ('Aklımdan tuttuğum sayıyı tahmin et 1-100 arasında (Sana kaç hak vereyim): '))
puan=hak
sayac=0

while hak > 0 :
    hak-=1 
    sayac +=1 
    tahmin = int(input('Tahminin nedir ? : '))
    if tahmin==randomSayi:
        print(f'Tebrikler doğru tahmin {tahmin}  {sayac}. hakkında bildin. Puanın: {100 - ((sayac-1)*(100/puan))}')
        break
    elif tahmin>randomSayi:
        print(f'{tahmin}"den daha küçük bir sayı tahmin et')

    else :
        print(f'{tahmin}"den daha büyük bir sayi tahmin et')
        
        
    if hak == 0:
        print(f'Hakkınız bitti. Tutulan sayı : {randomSayi}')
    

    