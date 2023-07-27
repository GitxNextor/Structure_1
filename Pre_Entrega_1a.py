# =============================================================================
#                P R I M E R A   P R E   E N T R E G A   V A
# =============================================================================

# 1. Declaro diccionario "base" que actúa como base de datos
# 2. Función Registro_de_datos, que recibe el diccionario "base" y almacena la
#    info de usuario y clave.
# 3. Función leer datos, recibe el diccionario "base" y lo imprime por pantalla
# 4. Función Guardar_Archivo, almacena el diccionario base en un .txt en DRIVE
# 5. Función LogIn recibe el diccionario "base" y valida con respecto a la en-
#    trada por teclado.


base = {}


def get_sth(x: str, what: str):
    # Toma una entrada del usuario y verifica que no esté vacía
    welcome = f'\nIngrese {what} o zz para salir: : '
    while x == '':
        print(f'No ingresaste nada')
        x = input(welcome)
    else:
        return x


def registro(bd):
    # Recibe los valores ingresados por el usuario y los almacena en un
    # diccionario como usuario: clave

    quit_char = 'zz'
    print(f'=========================')
    print(f'    INGRESO DE DATOS')
    print(f'=========================')
    welcome_usr = f'\nIngrese Usr o zz para salir: '
    welcome_pwd = f'\nIngrese Pwd: '

    kbd = input(welcome_usr)
    while kbd.lower() != quit_char:
        usr = get_sth(kbd, "Usr")

        kbd = input(welcome_pwd)
        pwd = get_sth(kbd, "pwd")

        bd.update({usr: pwd})

        kbd = input(welcome_usr)
    else:
        print(f'\nTerminó el ingreso de datos\n')

    #  TEST BLOCK
    # for key, value in bd.items():
    #     print(f'{key}: {value}')


def get_user(bd):
    # Verifica que los datos ingresados sean de un usuario válido
    quit_char = 'zz'
    welcome_usr = f'\nIngrese Usr o {quit_char.lower()} para salir: '
    welcome_back = f'\nIngreso no válido\nIngrese Usr o {quit_char.lower()} para salir: '
    print(f'\n=========================')
    print(f'         LOG IN')
    print(f'=========================')
    kbd = input(welcome_usr)
    while kbd.lower() != quit_char:
        usr = get_sth(kbd, "Usr")
        if usr in bd:
            break
        else:
            kbd = input(welcome_back)
    else:
        print(f'\nTerminó el ingreso SIN datos')
        exit(0)
    return usr, bd.get(usr)


def leer(bd):
    print(f'Los datos registrados son:')
    for key, value in bd.items():
        print(f'{key}: {value}')
    print()


def guardar(bd):
    # Recibe el diccionario que registró usuario y clave
    # y lo guarda como .txt
    ruta = "C:\\Users\\User\\PycharmProjects\\pythonCODERHOUSE\\"
    file = "datos.txt"
    with open(ruta + file, 'w') as f:
        for key in bd.keys():
            cadena = f'{key}: {bd[key]}\n'
            f.write(cadena)
    print(f'=================================\n'
          f'Los datos registrados se grabaron \n'
          f'en el archivo: datos.txt\n'
          f'=================================')


def bienvenida():
    # Solicita primer ingreso de clave
    return input(f'Ingrese Password: ')


def cantidad(i):
    #  Verifica cantidad de intentos
    max_intento = 3
    return True if i < max_intento else False


def clave(key, cl):
    # Verifica la clave. Si necesito cambiar la clave
    # modifico el valor de password en esta función
    return True if key != cl else False


def clave_incorrecta(num: int):
    # Informa clave incorrecta, ofrece nuevo ingreso
    # Devuelve valor ingresado
    max_intento = 3
    if num > 1:
        msg = f'(Te queda {max_intento - num} intento):  '
    else:
        msg = f'(Te quedan {max_intento - num} intentos): '
    return input(f"\nContraseña Incorrecta,\n"                 
                 f"Ingrese nuevamente "
                 f"{msg}")


def pwd(cl):
    # Función que verifica que la clave sea la correcta dentro de la cantidad
    # de intentos permitidos
    acceso_permitido: str = "\nAcceso Concedido"
    acceso_denegado: str = "\nDemasiados Intentos, Acceso Denegado"
    intentos: int = 1

    entrada = bienvenida()
    while cantidad(intentos) and clave(entrada, cl):
        entrada = clave_incorrecta(intentos)
        intentos += 1

    print(acceso_denegado) if clave(entrada, cl) else print(acceso_permitido)


def login(bd):
    # Función LogIn
    usuario = get_user(bd)
    pwd(usuario[1])


registro(base)
leer(base)
guardar(base)
login(base)
