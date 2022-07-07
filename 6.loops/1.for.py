numbers= [1,2,3,4,5]

for num in numbers:
    print(f"numbers {num}")
    

names=['tayyip','turan','merve','mücahit','semiha','şüheda']

for name in names:
    print(f'my name is {name}')
    
name = 'Tayyip Altunöz'

for n in name :
    print(f'karekter {n}')
    
tuple = [(1,2),(3,4),(5,6)]

for a,b in tuple:   #liste içindeki tuple elemanları ayrı ayrı yazdırır
    print(a,b)
    
d = {'k1':1,'k2':2,'k3':3}   #dictonary

for key,value in d.items():   #dictionary key value beraber yazdırmak için bu yöntem kullanılır
    print(key, value)