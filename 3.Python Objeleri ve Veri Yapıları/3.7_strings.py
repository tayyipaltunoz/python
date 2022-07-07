name = 'Tayyip'
surname = "Altunöz"
age = 36

greeting =  ('My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old')

print (greeting)
print (greeting[0]) #greeting ifadesini 0 indexi ekrana basar

print (len(greeting)) # greeting ifadesinin kaç karekter olduğunu söyler

print (greeting[-1]) #greeting ifadesinin son karekterini verir

print (greeting[3:7]) # greeting ifadesinin 3 den 7 ekadar olan karekterleri verir

print (greeting[:17]) # greeting ifadesinin 17dan sonara  karekterleri verir


print (greeting[3:40:2]) # greeting ifadesinin 3den 40 a kadar 1 atlayarak verir 