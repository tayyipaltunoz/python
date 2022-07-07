x,y,z=2,5,10

numbers = 1,5,7,10,6

#1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z  toplamını farkı nedir 

sayi1 = int(input('sayı giriniz : ' ) )
sayi2 = int(input('sayı giriniz : ' ) )
sonuc= (sayi1*sayi2)-(x+y+z) ; print(f'sonuc : {str(sonuc)}')  

#y'nin x'e kalansız bölümünü hesaplayınız
kalansiz=y//x
print(f'kalansız bölme {kalansiz}')

#(x,y,z) toplamının  mod  3'ü nedir?
mod=(x+y+z)%3 ; print(f'mod: {mod}')

#y'nin x'inci kuvvetini hesaplayınız
kuvvet=y**x  ; print(f'kuvvet: {kuvvet}')

#5- x,*y,z =numbers işlemine göre z'nin küpü kaçtır
x , *y ,z = numbers 
zninkupu=z**3 ; print(f'znin küpü : {zninkupu}')

#5- x,*y,z =numbers işlemine göre y ninn değerleri toplamı kaçtır

ynindegerleritoplam=y[0] + y[1]+ y[2]  ; print(f'y nin değerleri toplamı: {ynindegerleritoplam}')