# def square(num) : return num ** 2 

numbers = [2,5,9,11]

# result = list(map(square,numbers))      # aşağıda lambda expression ile ayın işlemi yapacağız


result = list(map(lambda num: num ** 2 , numbers))

print(result)



mod  = lambda num : num % 3

result2 = mod()

print(result2)