sayilar = [1,3,5,7,9,12,19,21]

# sayilar listesini  while ile ekrana yazdırın.

# i = 0
# while i < len(sayilar):
#     print(sayilar[i])
#     i += 1
    
#2 başlangış ve bitiş değerlerini kullanıcıdan alıp  aradaki tüm tek sayıları  ekrana yazdırın.

# baslangic = int(input('Başlangıç değeri : '))
# bitis = int(input('Bitiş değeri : '))

# x = baslangic

# while x < bitis:
#     x += 1
#     if (x % 2 == 1):
#         print(x)

# 1-100 arasındaki  sayıları  azalan şekilde yazdırın

# z=99 

# while z > 1:
#     print(f'1-100 arası tersten : {z}')
#     z = z - 1
    
#  Kullanıcıdan aldığımız  5 sayıyı sıralı bir şekilde yazdırın

# numbers = []
# y=0
# while y < 5:
#     sayi = int(input('sayi giriniz : '))
#     numbers.append(sayi)
#     y+=1

# numbers.sort()
# print(numbers)

#Kullanıcıdan  alacağınız  sınırsız ürün bilgisini  urunler  listesi içinde  saklayınız
#**Ürün sayısını kullanıcıya sorun 
#**dictionary listesi yapısı (name,price) şeklinde olsun
#ürün ekleme bittiğinde ürünleri while ile listeleyin

urunler = []
adet = int(input('Ürün sayısını giriniz : '))

u=0
while adet>u:
    name = input('Ürün ismini giriniz : ')
    price = input('Ürün fiyatını giriniz : ')
    
    urunler.append({
        'name':name,
        'price':price
    })
    u+=1
    
for urun in urunler:
    print(f'ürün adı : {urun["name"]} ürün fiyatı : {urun["price"]}')   