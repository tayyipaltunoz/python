names = ['Ali','Yağmur','Hakan','Deniz']
years= [1998,2000,1998,1997]

#1-Cenk ismini listenin sonuna ekleyiniz
names.append('Cenk')    ;   print(f'1- {names}')

#2-Sena ismini listenin başına ekleyiniz
names.insert(0,'Sena')  ;   print(f'2- {names}')

#3-Deniz ismini listeden siliniz
#names.remove('Deniz')   ;   print(f'3- {names}') #pop ile index verilerekte siline bilir

#4- Deniz ismini indexi nedir
deniz=names.index('Deniz') ; print(f'4- Denizin bulunduğu index : {deniz}')

#5- Ali listenin bir elemanı mıdır
ali=names.index('Ali') ; ali1='Ali' in names;   print(f'5- {ali} yada {ali1}')

#6-Liste elemanlarını ters çevirin
names.reverse() ; print(f'6- Liste elemanları ama tersten: {names}')

#7-liste elemanları  alfabetik olarak sıralayınız
names.sort() ; print(f'7- alfabetik sıralandı: {names}')

#8- years listesini rakamsal olarak sıralayınız
years.sort() ; print(f'8- years rakamsal olarak sıralandı : {years}')

#9- str='Chevrolet,Dacia' karekter dizisini listeye çeviriniz?
str='Chevrolet,Dacia' ; str=str.split(',')  ; print(f'9- str listeye çevrildi = {str}')

#10- years dizisinin en büyük ve en küçük elemanı nedir
enb=max(years) ; print(f'10-years listesinin en büyük elemanı : {enb}')
enk=min(years) ; print(f'10-years listesinin en küçük elemanı : {enk}')

#11- years dizisinde kaç tane 1998 var
kactane=years.count(1998) ; print(f'11- kaç tane 1998 var ?  bu kadar : {kactane}')

#12- years dizisinin tüm elemanlarını siliniz
years.clear() ; print(f'12 silindi {years}')

#13- Kullanıcıdan alacağınız  3 tane marka bilgisinin  bir listede saklayınız
markalar = []

marka=input('marka: ')  ; markalar.append(marka) ; marka=input('marka: ')  ; markalar.append(marka) ;marka=input('marka: ')  ; markalar.append(marka) ; print(f'Markalar : {markalar}')
