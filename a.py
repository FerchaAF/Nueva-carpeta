lista_rut = []
lista_sl = []
sl = 0
entra = 0
cant_hijos = 0
while entra == 0:
    sb = int(input('Ingresa sueldo base\n'))
    while(sb<=0):
        print('error')
        sb = int(input('Ingresa sueldo base\n'))
 
    sl = (sb * 0.9) + (cant_hijos * 20000)
    lista_sl.append(sl)
    entra = int(input('0 para salir, otro número para continuar'))