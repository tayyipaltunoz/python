from logging.config import valid_ident


numbers = [1,8,10,5,10,6,9]
letters = ['a','g','y','c','u','i']

val=min(numbers)
val=max(numbers)
val=max(letters)

numbers.append(49) #dizinin sonuna 49 elamanını ekler

numbers.insert(3,79) #3. indexe 79 sayısını ekler
numbers.insert(-1,44) #en sondaki elmanı kaydırıp 44 sayısını ekler

numbers.pop(0) #0. indexdeki elemaını siler
numbers.remove(44) #silmek istediğim karekteri bulup siler

#numbers.sort() # liste sayısal büyüklük olarak sıralanır
letters.sort() #liste alfabetik olarak sıralanır

numbers.reverse() #listeyi sayısal olarak tersten listeler

print(numbers.count(10)) #numbers içersinde kaç tane 10 var

print(f'numbers: {numbers} \nletters: {letters}')