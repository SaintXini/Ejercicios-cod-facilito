num_user = int(input("INGRESE LA CANTIDAD DE USUARIOS A INGRESAR: "))
user_new = []

for i in range(num_user):
    
    name = input("Ingrese su nombre: ")
    if len(name) < 5 or len(name) > 50:
        print("RANGO DE DATOS ENTRE 5 A 50")
        continue
        
    last_name = input("Ingrese su apellido: ")
    if len(last_name) < 5 or len(name) > 50:
        print("RANGO DE DATOS ENTRE 5 A 50")
        continue
        
    cel = input("INGRESE SU #: ")
    if len(cel) != 8:
        print("EL NÚMERO DEBE CONTENER 10 DÍGITOS")
        continue
        
    correo = input("INGRESE SU CORREO: ")
    if len(correo) < 5 or len(correo) > 50:
        print("RANGO ENTRE 5 A 50")
        continue
    
        
    user_new.append((name, last_name, cel, correo))
    print("USUARIO AGREGADO CON EXITO")
    print("")

print("") 
print("Estos son los datos agregados:")
for i, dates in enumerate(user_new, start = 1):
    print(f"No. Usuario: {i} ")
    print("Nombre: ", dates[0])
    print("Apellido: ", dates[1])
    print("Correo: ", dates[3])
    print("Cel: ", dates[2])
    print("")
