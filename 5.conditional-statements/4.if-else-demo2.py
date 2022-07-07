from time import sleep


e = input('mail : ')
p = input('password : ')

email = 'tayyip@gmail.com'
password = '1234'

if email == e :
    if password == p:
        print('giriş yapılıyor')
        sleep(1)
    else:
        print (f'Şifre hatalı! Tekra deneyiniz')
    
    print(f'Giriş başarılı. Hoşgeldin {e}')
else:
    print(f'Hatalı giriş yaptınız. "{e}" böyle bir mail adresi sistemde bulunamadı. Lütfen tekrar deneyiniz.')