# =============================================================================
#                             H P 4 K   S N I P E T ' s
# =============================================================================


# -----------------------------------------------------------------------------
#                         G L O B A L   V A R I A B L E S
# -----------------------------------------------------------------------------
# "C:\NÉXTOR\Documents\OLD DATA\RED_PEN\Inventario\Data\Base_27_01_17.txt"
# "C:\Users\User\PycharmProjects\pythonCODERHOUSE\HP4K\Base_1_Aug_23.txt"

path = r'C:\Users\User\PycharmProjects\pythonCODERHOUSE\HP4K'
file = r'\Base_1_Aug_23.txt'

raw_data = []
expanded = []
sbcsu_trimmed = []

aun0 = {}

colon, comma, empty = (':', ',', '')
sep_s, sep_d, to, right = ("&", '&&', 'to', 1)
tacsu_k = []
block = dict(sa='M2 1 ADD-SA:VCE', aun='M2 1 ADD-AUN:', scsu='M2 1 ADD-SCSU',
             sbcsu='M2 1 ADD-SBCSU', tacsu='M2 1 ADD-TACSU')
init_sa = dict(cd=1, tipo=4, sta_rng=5)
init_aun = dict(grp=0, sta_rng=3)
init_scsu = dict(sta=0, pen=1)
init_sbcsu = dict(sta=0, pen=3)
init_tacsu = dict(pen=0, tgrp=10, num=12, board=31, e1_teco=10, e1_tasa=49)
e1 = dict(teco='10', tasa='49')


# -----------------------------------------------------------------------------
#                              S A   S N I P E T S
# -----------------------------------------------------------------------------
def get_sa_line(p, f, ra):
    with open(p + f) as fi:
        for line in fi:
            if line.startswith(block['sa']):
                ra.append(trim_sa_line(line))


def trim_sa_line(ln_sa):
    halves = (ln_sa.split(colon))
    sa_lst = halves[right].split(comma)
    fields = [sa_lst[init_sa['cd']], sa_lst[init_sa['tipo']],
              sa_lst[init_sa['sta_rng']]]
    return fields


def imprimir_sa(lista):
    print(f'\nListado Grupos de HUNT')
    print('=' * 70)
    for linea in lista:
        print(f'HT Group: {linea[0].rjust(4)}, {linea[1].rjust(3)}, '
              f'{linea[2].split("&")}')
    print('=' * 70)
    print(f'Encontré: {len(lista)} grupos')


# -----------------------------------------------------------------------------
#                              A U N   S N I P E T S
# -----------------------------------------------------------------------------
def get_aun_line(p, f, ra):
    with open(p + f) as fi:
        for line in fi:
            if line.startswith(block['aun']):
                ra.append(trim_aun_line(line))


def trim_aun_line(ln_aun):
    halves = (ln_aun.split(colon))
    aun_lst = halves[right].split(comma)
    # fields = [aun_lst[grp], aun_lst[sta_rng]]
    # return fields
    collect_stations(aun_lst[init_aun['grp']],
                     aun_lst[init_aun['sta_rng']])


def collect_stations(gr, sta):
    # Agrupa todos los internos que vienen separados por \n para poder
    # armar un diccionario
    if init_aun['grp'] in aun0.keys():
        buffer = aun0[init_aun['grp']] + sep_s + init_aun['sta_rng']
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
    if sep_d in ln:
        buffer0 = ln.replace(sep_d, to)
        buffer1 = buffer0.split(sep_s)
        # print(buffer1)
        # for item in buffer1:
        #     print(item)
        return expand(buffer1)
    else:
        buffer1 = ln.split(sep_s)
        return buffer1


def expand(buf):
    # Recibe un:str, y lo convierte en una lista de internos, además cuando
    # encuentra el separador 'to' expande los miembros del rango.
    # Ej.: recibe "7801to7807" y expande el str a una lista como:
    # ['7801', '7802', '7803', '7804', '7805', '7806', '7807']
    # La lista queda ordenada porque viene así de origen

    for item in buf:
        if to not in item:
            expanded.append(item)
        else:
            lista = item.split(to)
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
            if line.startswith(block['scsu']):
                ra.append(trim_scsu_line(line))
        print(f'\nEncontré: {len(ra)} internos')


def trim_scsu_line(ln_sa):
    halves = (ln_sa.split(colon))
    sa_lst = halves[right].split(comma)
    if sa_lst[init_scsu['pen']] == '':
        ltg, ltu, slot, cct = '', '', '', ''
    else:
        ltg, ltu, slot, cct = sa_lst[init_scsu['pen']].split('-')
    print(sa_lst[init_scsu['sta']],
          ltg.rjust(2), ltu.rjust(2), slot.rjust(2), cct.rjust(2))


# -----------------------------------------------------------------------------
#                              S B C S U   S N I P E T S
# -----------------------------------------------------------------------------
def get_sbcsu_line(p, f, ra):
    with open(p + f) as fi:
        for line in fi:
            if line.startswith(block['sbcsu']):
                ra.append(trim_sbcsu_line(line))
        print(f'\nEncontré: {len(ra)} internos')


def trim_sbcsu_line(ln_sa):
    halves = (ln_sa.split(colon))
    sa_lst = halves[right].split(comma)
    if sa_lst[init_sbcsu['pen']] == '':
        ltg, ltu, slot, cct = '', '', '', ''
    else:
        # PEN Unpacking fo LTG, LTU, SLOT & CCT
        ltg, ltu, slot, cct = sa_lst[init_sbcsu['pen']].split('-')
    # print(sa_lst[init_sbcsu['sta']],
    #       ltg.rjust(2), ltu.rjust(2), slot.rjust(2), cct.rjust(2))
    lista = [sa_lst[init_sbcsu['sta']], ltg, ltu, slot, cct]
    sbcsu_trimmed.append(lista)
    # for linea in lista:
    print(lista)

# -----------------------------------------------------------------------------
#                              T A C S U   S N I P E T S
# -----------------------------------------------------------------------------
def get_tacsu_line(p, f, ra):
    with open(p + f) as fi:
        for line in fi:
            if line.startswith(block['tacsu']):
                ra.append(trim_tacsu_line(line))
        print(f'\nEncontré: {len(tacsu_k)} Troncales')


def trim_tacsu_line(ln_sa):
    halves = (ln_sa.split(colon))
    tacsu_lst = halves[right].split(comma)
    # fields = [sa_lst[sta], sa_lst[pen]]
    # return fields
    if tacsu_lst[init_tacsu['tgrp']] == e1['teco'] \
            or tacsu_lst[init_tacsu['tgrp']] == e1['tasa']:
        pass
    else:
        print(tacsu_lst[init_tacsu['pen']].rjust(10),
              tacsu_lst[init_tacsu['tgrp']].rjust(3),
              # La siguiente línea remueve '"', remueve blancos y ajusta
              # a la derecha
              tacsu_lst[init_tacsu['num']].replace('"', '').strip().rjust(12),
              tacsu_lst[init_tacsu['board']].rjust(10))
        tacsu_k.append(tacsu_lst[init_tacsu['tgrp']])


# -----------------------------------------------------------------------------
#                         E X C E C U T I O N   A R E A
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
            # print(f'Work In Progress')
            get_sbcsu_line(path, file, raw_data)
        case 5:
            get_tacsu_line(path, file, raw_data)
        case 6:
            print(f'Work In Progress')
        case _:
            print(f'Opción fuera de rango')


def start():
    print(f'\nGroups Menu')
    print('-' * 11)
    print(f'1. Pick Up Groups\n2. Hunt Groups\n'
          f'3. SCSU Table\n4. SBCSU Table\n5. TACSU Table\n6. CGWB Table')

    # wrong_input = f'La entrada no es numérica:'
    # probar con el formato anterior a f''
    farewell = f'Gracias!'
    entrada = welcome()
    while entrada != empty:
        if entrada.isnumeric():
            # right answer
            whatsup(int(entrada))
            break
        else:
            # wrong_answer
            print(f'La opción {entrada} NO es válida', end='\r')
            entrada = please_enter()
    else:
        # Exit
        print(farewell)


start()
