num_user = int(input("INGRESE LA CANTIDAD DE USUARIOS A INGRESAR: "))
user_new = []

for i in range(num_user):
    
    name = input("Ingrese su nombre: ")
    if len(name) < 5 or len(name) > 50:
        print("RANGO DE DATOS ENTRE 5 A 50")
    else:
        print("DATOS ALMACENADOS EXITOSAMENTE")
        
    last_name = input("Ingrese su apellido: ")
    if len(last_name) < 5 or len(name) > 50:
        print("RANGO DE DATOS ENTRE 5 A 50")
    else:
        print("DATOS ALMACENADOS CORRECTAMENTE")
        
    cel = input("INGRESE SU #: ")
    if len(cel) < 10:
        print("DATOS INSUFICIENTES")
    elif len(cel) > 10:
        print("DATOS EXCEDIDOS")
    else:
        print("DATOS ALMACENADOS CORRECTAMENTE")
        
    correo = input("INGRESE SU CORREO: ")
    if len(correo) < 5 or len(correo) > 50:
        print("RANGO ENTRE 5 A 50")
    else:
        print("DATOS ALMACENADOS CORRECTAMENTE")
    
        
    user_new.append((name, last_name, cel, correo))
    
print("")
print("") 
print("Estos son los datos agregados:")
for dates in user_new:
    print("Nombre: ", dates[0], " Apellido: ", dates[1])
    print("")
