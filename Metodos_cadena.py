email = input("Ingrese su correo: ")
#live shared

while(email[0]=='@' or email.count('@')!=1 or email[-1]=='@' ):
    email = input("Ingrese su correo: ")
