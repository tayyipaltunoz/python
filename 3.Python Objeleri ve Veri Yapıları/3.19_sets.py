fruits = {'banana','apple','orange'}

#print(fruits[0])  #listeler indexlenemaz
for x in fruits:
    print(x)
    
fruits.add('cherry')
fruits.update(['mango','grape','apple']) # apple zaten var ikinci kere eklenmeyecek

print(fruits)

myList = [1,2,5,4,4,2,1]

print(myList)
print(set(myList))  # set constructer ile tekrarlayan elemanlar gelmeyecek