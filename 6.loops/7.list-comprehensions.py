
from distutils.core import run_setup


numbers = [x for x in range(10,20,2)]   #for döngüsü range methodu ile eleman üretilip  numbers listesine ekleme

print(numbers)


# for x in range(10):  #aşağıda daha iyi bir yöntemi var
#     print(x**2)
    
numbers = [x**2 for x in range(10)]
print(numbers)

numbers = [x*x for x in range(10) if x % 3 == 0]
print(f'1-10 kadar 3 katı olna sayıların karesi : {numbers}')

myString='Hello'
myList = []

for item in myString:
    myList.append(item)
print(f'string elemanlarının listeye dönüşümü :  {myList}')

myList=[x for x in myString]
print(f'string elemanlarının listeye dönüşümü :  {myList}')


result = [sayi if sayi % 2 == 0 else 'TEK'for sayi in range(10)]   #çift sayıları yzdırır tek olanlara tek yazar
print(result)

#içi içe döngüler

result2= []
for x in range(3):
    for y in range(3):
        result2.append((x,y))
print(result2)

result5 = [(x,y) for x in range(3) for y in range(3)]
print(result5)