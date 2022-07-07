# Identity Operator : is

x = y = [1, 2, 3]

z = [1,2,3]

print(x==y)
print(x==z)
print(x is y)
print(x is z)   # false aynı yerde tutulmadığından value -reference type konusu

print (x is not z)

# Membership Operator : in

a = ['banana' ,'apple']

print('banana' in a)
print('banana' not in  a)