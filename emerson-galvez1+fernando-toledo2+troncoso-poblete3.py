## Integrantes del grupo
## Emerson Galvez
## Fernando Toledo
## Troncoso Poblete

#Ruts
RutIn = 0
Ruts = []
#Sueldo
SueldoBa = 0
SueldoLiq = []
#Hijos
Hijo = 0
Inp = 0

def GuardRut():
    while True:
        
        global RutIn 
        RutIn = int(input('ingrese su rut, escriba nada o 0 si quiere cancelarlo \n'))
        Ruts.append(RutIn)
        if  RutIn == 0:
            del Ruts [-1]
            break

GuardRut()
print(Ruts)

while Inp == 0:
    SueldoBa = int(input('Ingresa el sueldo base\n'))
    while (SueldoBa<= 0):
        print()


