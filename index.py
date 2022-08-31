
anio = input("Decime un anio: ")
print(anio)

def anio_bisiesto():
    if int(anio) % 400 == 0:
        print("Es bisiesto")
    else:
        if int(anio) % 4 == 0 and int(anio) % 100 != 0:
            print("Es bisiesto")
        else:
            print("No es bisiesto")
    
    
anio_bisiesto()