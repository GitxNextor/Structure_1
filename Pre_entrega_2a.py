# =============================================================================
#                S E G U N D A   P R E   E N T R E G A   V A
# =============================================================================

# 1. Clase CLIENTE:
# 2. 4 Atributos
# 3. 2 Métodos
# 4. Paquete Re-distribuible
# 5.


class Cliente:
    # Atributos de Clase
    atrib_clase_1 = "Reservado"
    atrib_clase_2 = 'Reservado'

    # Constructor
    # Atributos de Instancia
    def __init__(self, name, last, ssn, addr, phone):
        self.nombre = name
        self.set_apellido(last)
        self.set_dni(ssn)
        self.set_email(addr)
        self.set_tele(phone)

    # Método especial str
    def __str__(self):
        return 'Nombre: ' + self.nombre + "\nApellido: " + \
            self.__apellido + "\nD.N.I: " + self.__dni + \
            "\nMail: " + self.__email + "\nTelfono: " +self.__tele

    # Seteo de atributos de instancia
    def set_apellido(self, ape):
        self.__apellido = ape

    def set_dni(self, num):
        self.__dni = num

    def set_email(self, dire):
        self.__email = dire

    def set_tele(self, num):
        if len(num) == 8:
            self.__tele = num
        else:
            print(f'Número incorrecto, se asigna uno por default')
            self.__tele = 'Default Nr'

    # Get de algunos atributos PRIVADOS
    def get_apellido(self):
        return self.__apellido

    def get_mail(self):
        return self.__email

    def get_tele(self):
        return self.__tele


cliente_1 = Cliente('Edmundo ', 'Dantes', '96876875', 'e.dantes@gmail.com', '53829360')

print('\n=================')
print(cliente_1)
print('=================\n')

print(f'Mi apellido es: {cliente_1.get_apellido()}')
print(f'Mi mail es: {cliente_1.get_mail()}')
print(f'Mi teléfono es: {cliente_1.get_tele()}')