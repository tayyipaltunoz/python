name = "Tayyip"
surname = "Altunöz"
age= 26

print ('My name is {} {}'.format(name,surname))
print ('My name is {1} {0}'.format(name,surname)) #index numaralarını değiştirdik önce surname yazacak 0'dan başlar
print ('My name is {s} {n}'.format(n=name,s=surname)) #index tanımladığımınz isimler üzerinden listeledik
print ("My name is {} {} and I'am {} yerars old.".format(name,surname,age)) 
print (f"My name is {name} {surname} and I'am {age} yerars old.") # f string ile aynı örneği gerçekleştirdik başına f yazıyoruz

result = 200 / 750

print ("the result is {}".format(result))
print ("the result is {r:2.5}".format(r=result)) #burada r değişkenine 2 karekter boşluk bırakıp virgülden sonra 5 karekter yazmasını istedik
