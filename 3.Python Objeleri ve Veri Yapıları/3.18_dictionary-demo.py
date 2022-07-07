students = {}


number = input ('numara: ')
name = input ('adı: ')
surname = input ('soyadı: ')
phoneNumber = input ('telefon: ')

# students[number]= {
#     'adı':name,
#     'soyadı':lastname,
#     'telefon':phoneNumber
# }

students.update({
    number:{
        'adı':name,
        'soyadı':surname,
        'telefon':phoneNumber
    },
})

print(students)
print('*'*50)
ogrenci = input ('Öğrenci numaranızı giriniz: ' )
 
ogrenci = students[number]

print(f"öğrenci adı : {ogrenci['adı']} öğrencini soyadı : {ogrenci['soyadı']} öğrencini numarası : {ogrenci['telefon']}")