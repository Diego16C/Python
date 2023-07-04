 
def comprobarContra(contra):
    largo = False
    mayus = False
    numer = False
    if len(contra) > 8:
        largo = True
    for i in range(len(contra)):
        if contra[i] .isupper():
            mayus = True
        if contra[i] .isupper():
            numer = True
    
    if largo and mayus and numer:
        return True
    else:
        return False

contra = input("Ingrese una contraseña: ")
verificacion = comprobarContra(contra)

if verificacion:
    print("la contrseña es segura")
else: 
    print("La contraseña no es segura")
