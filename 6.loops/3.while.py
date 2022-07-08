x = 0

while x < 100:
    print(x)
    x += 1
print("while döngüsü bitti")

#1-100 arasındaki çift sayıları yazdır

y=0
while y < 100:
    if (y % 2 == 0):
        print(f'çift sayılar : {y}')
    y += 1 
    
    
#ismini girmediği sürece tekrar sonran loops


name = ''  #false

while not name : #yani boşsa  yada true yazabiliriz boş değer false
    name = input("İsminiz :")
    if name == '':
        print('İsim girmeniz zorunludur')
print(f'Merhaba {name}')