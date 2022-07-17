# Gönderilen bir kelimeyi belirtilen kez ekranda yazdırma.

# def tekrarla(kelime,adet):
#     print(kelime*adet )
        
# tekrarla('Merhaba\n',5)

# Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon

# def listeyeCevir(*params):
#     liste = []

#     for param in params:
#         liste.append(param)
        
#     return liste
#     print(params)
    
# result = listeyeCevir('tayyip','Altunöz',10,50)
# print(result)

# Gönderilen iki sayı arasındaki tüm asal sayıları bulun

# def asalBul(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi > 1:
#             for i in range(2,sayi):
#                 if sayi % i == 0:
#                     break
#             else:
#                 print(sayi)
    
    
# sayi1 = int(input('sayi 1: '))
# sayi2 = int(input('sayi 2: '))

# asalBul(sayi1,sayi2)


#Kendisine gönderilen  bir sayının tam bölenlerini  bir liste şeklinde dönen fonksiyon

def tamBolenleriBul(sayi):
     tamBolenler = []
     for i in range(1,sayi):
         if sayi % i == 0 :
             tamBolenler.append(i)
             
     return tamBolenler
    
 
 

print(tamBolenleriBul(25))