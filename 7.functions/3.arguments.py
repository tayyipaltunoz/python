# def change(n):
#     n[0] = 'istanbul'
    
# sehirler=['ankara','izmir']

# change(sehirler)

# n = sehirler[:] #slicing  parçalama işlemi n değişkeni string olarak atar

# n[0]='ankara'

# print(sehirler)
# print(n)


# def add(a,b):
#     return sum((a,b))

# print(add(5,6))

def add(*params):  # * yıldıztuple tipinde listede verileri tutar
    print(params[2])
    return(sum((params)))

print(add(8,5,6,2,5))

def displayUser(**args): # ** yıldız dictionary type inde verileri tutar
    for key,value in args.items():
        print(f'{key} is {value}')
        
        
displayUser(name = 'Tayyip', age = 26, city = 'istanbul')
displayUser(name = 'Taha', age = 16, city = 'ankara',email='taha@gmail.com')
        