from tokenize import triple_quoted


list = [1,'iki',3]

#tuple liste ile aynı kullanı sahip ama tuple'da daha önceden oluşturulan elaman değiştirilemez silinemez
tuple = 1,'iki',3

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

#tuple[0]='tayyip' ; print(tuple[0])  #tuple da bu işlemi gerçekleştiremeyiz