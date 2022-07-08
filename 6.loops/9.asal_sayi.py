# girilen bir sayının asal olup olmasığını bulun

sayi = int(input('Bir sayı giriniz : '))

asalmi = True

if sayi == 1:
    asalmi = False

for i in range(2,sayi):
    if ( sayi % i == 0):
        asalmi = False
        break
    
if asalmi == True:
    print(f'{sayi} asaldır.' )
else:
    print(f'{sayi} asal değildir.')