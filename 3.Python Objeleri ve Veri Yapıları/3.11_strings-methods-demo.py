website="www.tayyipaltunoz.com"
course= "Python Kursu: Baştan Sonra Python Programlama Rehberiniz (40 saat)"

#1- ' Hello World ' karekterinin başındaki ve sonundaki boşluk karekterleri silin.
helloworld=' Hello World ' ; helloworld=helloworld.strip() ; print(helloworld)
#2- 'www.tayyipaltunoz.com' içerisindeki tayyipaltunoz haricindeki bütün değerleri sil
ta='www.tayyipaltunoz.com' ; ta=ta.lstrip('www.').rstrip('.com') ; print(ta) 
ta='www.tayyipaltunoz.com' ; ta=ta.strip('w.com') ; print(ta)
#3- 'course' karekter dizisinin tüm karekterlerini küçük harf yapın.
course=course.lower() ; print(course)
#4- 'website içinde kaç tane a karekteri vardır.
kactaneavar=website.count('a') ; print(kactaneavar)
#5- 'website' www ile başlayıp .com ile bitiyor  mu?
kontrol=website.startswith('www'),website.endswith('.com') ; print(kontrol)
#6- 'website' içerisinde .com ifadesi var mı?
bul=website.find('.com') ; print(f'6- {bul}')
#7- 'course' içindeki karakterler alfabetik mi? (isalpha,isdigit)
alfa=course.isalpha() ; print(alfa)
#8- 'Contents' ifadesini satırada 50 karekter içine yerleştirip sağ ve soluna * ekleyiniz.
icerik='Contents' ; icerik=icerik.center(50,'*') ; print(icerik)
#9- 'course' karekter dizisindeki boşlukları '-' ile değiştiriniz.
tire=course.replace(' ','-') ; print(tire)
#10- 'course karekter dizisini boşluklarından ayır'
ayir=course.split(' ') ; print(ayir)