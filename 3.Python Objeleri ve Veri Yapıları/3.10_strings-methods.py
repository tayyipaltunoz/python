message= ' Hello There. My name is Tayyip Altunöz '

message1 = message.upper() ;print(message1) #tüm karekterler büyük harfe çevrilir
message2 = message.lower() ;print(message2) #tüm karekterler küçük harfe çevrilir
message3 = message.title() ;print(message3) #her kelimenin baş harfi büyük harfe çevrilir.
message4 = message.capitalize() ;print(message4) #değişkenin ilk harfini büyük yazar
message5 = message.strip() ;print(message5) #kullanıcının girdiği karekterlerin baş ve sondaki boş karekterleri siler
message6 = message.split() ;print(message6) #kelimeleri boşluklardan parçalara böler dizi gibi olur

message7 = message.split('.') ; print(message7) #kelimeleri .'dan parçalara böler 

message8 = ' '.join(message6) ; print(message8) #message 6 da ayırdığımız kelimeleri birleştirip araya boşluk atar

index = message.find('Tayyip') ; print(index) #cümle içerisinde Tayyip arar ve bulduğunda ilk harfin index numarasını döner bulamazsa-1 döner

isFound = message.startswith(' H') ; print(isFound) # cümle ' H' ile mi başlıyor True döner

message9 = message.replace('Tayyip','Turan') ; print(message9) #Tayyip bulur Turan ile değiştirir

message10 = message.center(100) ; print(message10) # 100 karekterlik bir container oluşturur ve verilen ifadeyi ortalar
message10 = message.center(50,'*') ; print(message10) # 50 karekterlik bir container oluşturur ve verilen ifadeyi ortalar ve boşluklara * koyar


# https://docs.python.org/3/library/stdtypes.html#string-methods  or https://www.w3schools.com/python/python_ref_string.asp diğer metodlar için