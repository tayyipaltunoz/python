email='tayyip@gmail.com'
password='1234'

girilen_email = input('email : ')
girilen_password = input('password : ')

isEmail= ( email == girilen_email.lower() )
isPassword = (password == girilen_password)

print(f'email: {isEmail} password: {isPassword}')