# Bankamatik Uygulaması

tayyipHesap={
    'ad': 'Tayyip',
    'hesapNo':'123456789',
    'bakiye':3000,
    'ekHesap':2000
}
turanHesap={
    'ad': 'Turan',
    'hesapNo':'923456789',
    'bakiye':2000,
    'ekHesap':1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    
    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz')
        bakiyeSorgulama(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if toplam >= miktar:
            ekHesapKullanimi = input ('ek hesap kullanılsın mı ? (e/h)')
            if (ekHesapKullanimi == 'e'):
                hesap['bakiye'] = 0
                ekHesapKullanilacakMiktar= miktar - hesap['bakiye']
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('paranızı alabilirsiniz')
                bakiyeSorgulama(hesap)
            else:
                print(f'ek hesap kullanılamadı {hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} yeterli bakiye yok')
    
        else:
            print('üzgünüz bakiye yetersiz')
            bakiyeSorgulama(hesap)
    
    

def bakiyeSorgulama(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bakiye bulunmaktadır. Ek hesabınızda {hesap['ekHesap']} TL bakiye bulunmaktadır.")


def paraYatir(hesap,miktar):
    
    if miktar > 0:
        hesap['bakiye'] += miktar
        print(f'bakiye {hesap["bakiye"]} TL yatıralan miktar {miktar} TL')

paraCek(tayyipHesap,1500)
paraCek(tayyipHesap,1000)

paraYatir(tayyipHesap,2000)
