
website="www.tayyipaltunoz.com"
course= "Python Kursu: Baştan Sonra Python Programlama Rehberiniz (40 saat)"

#1- 'course'' karekter dizisinde kaç karekter vardır.
print ("1-  "+str(len(course)))
#2- 'website' içinden www karekterlerini alın
print ('2- '+ website[0:3])
#3- website içinden com karekterini alın
lenght=len(website)
result=website[lenght-3:lenght]
print ('3- '+ result)
#4- course içinden ilk 15 ve son 15 karekteri alın
result4=course[:15]
result41=course[-15:]
print ('4- ik15:' + result4 +' son15: '+ result41 )
#5- 'course ifadesindeki karekterleri tersten yazdırın'
print ('5-'+ course[::-1])

name, surname , age , job = 'Tayyip', 'Altunöz',26,'developer'
#6- Yukarıda verilen değişkenler ile  ifadeyi(Benim adım Tayyip Altunöz yaşım 26 mesleğim developer.)  yazdırın.
print('6- ' + 'Benim adım ' + name +' ' + surname + ' yaşım '+ str(age) +" mesleğim "+ job+'.') #daha kolay bir yolu var format
result6='Benim adım {} {} yaşım {} mesleğim {}.'.format(name,surname,age,job);print(result6) #başka bir yolu daha var :)
result61=f'Benim adım {name} {surname} yaşım {age} mesleğim {job}. f ile yapıldı';print(result61) 
#7- 'Hello world' w harfini W harfi ile değiştirin.
hello='Hello world'
s=hello[:5]+'W'+hello[-4:] ; print('7- '+ s)
s1=hello.replace('w','W') ; print (f'7- {s1} *replace ile yapıldı ')
#8- 'abc' ifadesini yan yana 3 defa yazdırın. 
result8='abc '*3 ; print(result8)