# ehliyet alabilme kontrol

def ehliyet():
    name = input('İsminiz : ').upper()
    age = int(input('Yaşınız : '))
    edu_status = input('Eğitim durumunuz : ').lower()


    if (age >= 18) : 
        if(edu_status == 'lise' or (edu_status == 'üniversite' or edu_status == 'lisans')):
            print(f'{name} ehliyet alamaya uygun. Yaş : {age} Eğitim durumu : {edu_status.upper()}')
        else:
            print(f'{name} öğrenim durumunuz "{edu_status.upper()}" ehliyet almaya uygun değil')
    else:
        print(f'{name} yaşınız "{age}" ehliyet alamaya uygun değil.')
#ehliyet()

# ************* öğrencin 2 yazılı bir sözlü ortalamasına göre not durumu hesaplama    0-24=>0 25-44=>1 45-54=>2 55-69=>3 70-84=>4 85-100=>5
def nothesaplama():
    yazili1 = float(input('ilk yazılı : '))
    yazili2 = float(input('ikinci yazılı : ')) 
    sozlu = float(input ('sözlü notu : '))
    
    ort = (yazili1+yazili2+sozlu)/3
    
    if (ort >= 0 and ort <= 24):
        print(f'ortalaması {ort} öğrencini notu 0')
    elif (ort >= 25 and ort <= 44):
        print(f'ortalaması {ort} öğrencini notu 1')
    elif (ort >= 45 and ort <= 54):
        print(f'ortalaması {ort} öğrencini notu 2')
    elif (ort >= 55 and ort <= 69):
        print(f'ortalaması {ort} öğrencini notu 3')
    elif (ort >= 70 and ort <= 84):
        print(f'ortalaması {ort} öğrencini notu 4')
    elif (ort >=85  and ort <= 100):
        print(f'ortalaması {ort} öğrencini notu 0')
    elif (ort < 0 and ort >100):
        print('hatalı değer girdiniz 0-100 arası bir değer giriniz')
    else :
        print('0-100 arasında değer giriniz')
#nothesaplama()

# ********** Trafiğe çıkış tarihi hesapla ve servis zamanlarını bildir

import datetime

def servisZamanı():
    tarih = input('Aracınız hangi tarihte trafiğe çıktı : (2019/8/9)')
    tarih = tarih.split('/')
    trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

    simdi = datetime.datetime.now()
    fark = simdi - trafigeCikis
    days = fark.days

    if days <= 365 :
        print('1. servis zamanı')
    elif ( days > 365  and days <= 365*2 ):
        print ('2. servis aralığı ')
    else :  
        print('3. ve sonraki servis zamanı')
    

servisZamanı()