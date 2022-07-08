sayilar= [1,3,5,7,9,12,19,21]
#sayılar listesindeki hangi sayılar 3'ün katıdır ?

for sayi in sayilar:
        if (sayi%3==0):
            print(f"sayilar içerisinde bu sayılar '{sayi}' 3'ün katlarıdır")

#sayılar listesinde sayıların toplamı kaçtır ?
toplam = 0
for top in sayilar:
    toplam += top   #toplam = toplam + top
print(f'toplam: {toplam}')

#sayılar içerisinde tek sayıların karesini alınız.

for tek in sayilar:
    if (tek % 2 == 1):
        karesi = tek ** 2
        print(f'tek sayılar {karesi}')

sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

#şehirlerden hangileri en fazla 5 karekterlidir ?

for sehir in sehirler:
    if (len(sehir)<=5):
        print(f'sehir : {sehir}')
        
urunler = [
    {'name':'samsung S6','price':'3000'},
    {'name':'samsung S7','price':'4000'},
    {'name':'samsung S8','price':'5000'},
    {'name':'samsung S9','price':'6000'},
    {'name':'samsung S10','price':'7000'},
]
#ürünlerin fiyatları toplamı nedir ?
toplam=0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print(f'Ürünlerin toplam fiyatı : {toplam}')

#Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?

for urun in urunler:
    if (int(urun['price']) <= 5000) :
        print(f'Fiyatı en fazla 5000 olanlar : {urun}')