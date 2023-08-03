
# =============================================================================
#                             H P 4 K   S N I P E T ' s
# =============================================================================


# -----------------------------------------------------------------------------
#                           G L O B A L   VA R I A B L E S
# -----------------------------------------------------------------------------
# "C:\NÉXTOR\Documents\OLD DATA\RED_PEN\Inventario\Data\Base_27_01_17.txt"
# "C:\Users\User\PycharmProjects\pythonCODERHOUSE\HP4K\Base_1_Aug_23.txt"

path = r'C:\Users\User\PycharmProjects\pythonCODERHOUSE\HP4K'
file = r'\Base_1_Aug_23.txt'
sa = 'M2 1 ADD-SA:VCE'
aun = 'M2 1 ADD-AUN:'
scsu = 'M2 1 ADD-SCSU'
tacsu = 'M2 1 ADD-TACSU'
con = '&'
x = 0
raw_data = []
aun0 = {}

# -----------------------------------------------------------------------------
#                              S A   S N I P E T S
# -----------------------------------------------------------------------------


def get_sa_line(p, f, ra):
    with open(p + f) as fi:
        for line in fi:
            if line.startswith(sa):
                ra.append(trim_sa_line(line))


def trim_sa_line(ln_sa):
    cd, tipo, sta_rng = (1, 4, 5)
    colon, comma = (':', ',')
    halves = (ln_sa.split(colon))
    sa_lst = halves[1].split(comma)
    fields = [sa_lst[cd], sa_lst[tipo], sa_lst[sta_rng]]
    return fields


def imprimir_sa(lista):
    print(f'\nListado Grupos de HUNT')
    print('=' * 70)
    for linea in lista:
        print(f'HT Group: {linea[0].rjust(4)}, '
              f'{linea[1].rjust(3)}, '
              f'{linea[2].split("&")}')
    print('=' * 70)
    print(f'Encontré: {len(lista)} grupos')

# -----------------------------------------------------------------------------
#                              A U N   S N I P E T S
# -----------------------------------------------------------------------------


def get_aun_line(p, f, ra):
    with open(p + f) as fi:
        for line in fi:
            if line.startswith(aun):
                ra.append(trim_aun_line(line))


def trim_aun_line(ln_aun):
    grp, sta_rng = (0, 3)
    colon, comma = (':', ',')
    halves = (ln_aun.split(colon))
    aun_lst = halves[1].split(comma)
    # fields = [aun_lst[grp], aun_lst[sta_rng]]
    # return fields
    collect_stations(aun_lst[grp], aun_lst[sta_rng])


def collect_stations(gr, sta):
    # Agrupa todos los internos de un mismo grupo que vienen separados por \n
    # para poder armar un diccionario
    if gr in aun0.keys():
        buffer = aun0[gr] + con + sta
        aun0.update({gr: buffer})
    else:
        aun0.update({gr: sta})


def rework_aun(dictio):
    for key, value in dictio.items():
        nu_val = check_range(value)
        dictio.update({key: nu_val})


def check_range(ln):
    # Busca la ocurrencia del token '&&' que identifica un rango de
    # números consecutivos.
    # La función expand(bu) reemplaza el str por el rango efectivo.
    link, coin, ran = ('&', '&&', 'to')
    if coin in ln:
        buffer0 = ln.replace(coin, ran)
        # print(buffer0)
        buffer1 = buffer0.split(link)
        # print(buffer1)
        # for item in buffer1:
        #     print(item)
        return expand(buffer1)
    else:
        buffer1 = ln.split(link)
        return buffer1


def expand(buf):
    # Recibe un:str, y lo convierte en una lista de internos, además cuando
    # encuentra el separador 'to' expande los miembros del rango.
    # Ej.: recibe "7801to7807" y expande el str a una lista como:
    # ['7801', '7802', '7803', '7804', '7805', '7806', '7807']
    # La lista queda ordenada porque viene así de origen
    expanded = []
    coin = 'to'
    for item in buf:
        if coin not in item:
            expanded.append(item)
        else:
            lista = item.split(coin)
            desde = int(lista[0])
            hasta = int(lista[1])+1
            for m in range(desde, hasta):
                expanded.append(str(m))
    return expanded


def imprimir_aun(dixie):
    print(f'\nListado Grupos de PICK UP')
    print('=' * 70)
    for k, v in dixie.items():
        print(f'\nAUN Group: {k.rjust(2)}')
        for sta in v:
            print(sta, end=' ')
        print()
    print('=' * 70)
    print(f'Encontré: {len(dixie)} grupos')


# -----------------------------------------------------------------------------
#                              S C S U   S N I P E T S
# -----------------------------------------------------------------------------


def get_scsu_line(p, f, ra):
    with open(p + f) as fi:
        for line in fi:
            if line.startswith(scsu):
                ra.append(trim_scsu_line(line))
        print(f'\nEncontré: {len(ra)} internos')


def trim_scsu_line(ln_sa):
    sta, pen = (0, 1)
    colon, comma = (':', ',')
    halves = (ln_sa.split(colon))
    sa_lst = halves[1].split(comma)
    # fields = [sa_lst[sta], sa_lst[pen]]
    # return fields
    print(sa_lst[sta], sa_lst[pen].rjust(11))


# -----------------------------------------------------------------------------
#                              T A C S U   S N I P E T S
# -----------------------------------------------------------------------------
k = []


def get_tacsu_line(p, f, ra):
    with open(p + f) as fi:
        for line in fi:
            if line.startswith(tacsu):
                ra.append(trim_tacsu_line(line))
        print(f'\nEncontré: {len(k)} Troncales')


def trim_tacsu_line(ln_sa):
    pen, tgrp, num, board = (0, 10, 12, 31)
    colon, comma = (':', ',')
    e1_teco, e1_tasa = ('10', '49')
    halves = (ln_sa.split(colon))
    tacsu_lst = halves[1].split(comma)
    # fields = [sa_lst[sta], sa_lst[pen]]
    # return fields
    pla = tacsu_lst[num].replace('"', '')
    if tacsu_lst[tgrp] == e1_teco or tacsu_lst[tgrp] == e1_tasa:
        pass
    else:
        print(tacsu_lst[pen].rjust(10), tacsu_lst[tgrp].rjust(3),
              pla.strip().rjust(12), tacsu_lst[board].rjust(10))
        k.append(tacsu_lst[tgrp])

    # for half in tacsu_lst:
    #     print(half, end=' ')


# -----------------------------------------------------------------------------
#                          E X C E C U T I O N   A R E A
# -----------------------------------------------------------------------------


def welcome():
    return input(f'\nIngrese la opción, o "Enter" para salir : ')


def please_enter():
    return input(f'\nAgain, ingrese una opción válida o "Enter" : ')


def right_answer(dato, dato1):
    print(f'El número {dato} es {dato1}\nGracias')


def wrong_answer(dato, dato1):
    print(f'El número {dato} NO es {dato1}')


def whatsup(w):
    match w:
        case 1:
            get_aun_line(path, file, raw_data)
            rework_aun(aun0)
            imprimir_aun(aun0)
        case 2:
            get_sa_line(path, file, raw_data)
            imprimir_sa(raw_data)
        case 3:
            get_scsu_line(path, file, raw_data)
        case 4:
            get_tacsu_line(path, file, raw_data)


def start():
    print(f'\nGroups Menu')
    print('-' * 11)
    print(f'1. Pick Up Groups\n2. Hunt Groups\n3. SCSU Table\n4. TACSU Table')

    # wrong_input = f'La entrada no es numérica:'
    # probar con el formato anterior a f''
    farewell = f'Gracias!'

    entrada = welcome()
    while entrada != '':
        if entrada.isnumeric():
            #  right answer
            num = int(entrada)
            whatsup(num)
            break
        else:
            # wrong_answer
            print(f'La opción {entrada} NO es válida', end='\r')
            entrada = please_enter()
    else:
        print(farewell)


start()
