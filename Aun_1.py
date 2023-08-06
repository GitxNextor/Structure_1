import csv


def checkline(ln):
    # Evita que la aparición del error IndexError detenga la ejecución
    # Guarda en una lista las líneas que dieron error
    wrong_lines = []
    try:
        'ADD-AUN:' in ln[0]
    except:
        wrong_lines.append(ln)
        return False
    return True


def check_range(ln):
    # Busca la ocurrencia del token '&&' que identifica un rango de
    # números consecutivos.
    # La idea posterior es reemplazar el token por el rango efectivo.
    # Por ahora lo encuentra e imprime los extremos del rango.
    coin = '&&'
    ran = 'to'
    if coin in ln:
        z = ln.replace(coin, ran)
        print(z)
        # y = x.split('&')
        # print(y)
    else:
        # y = ln.split('&')
        # print(y)
        print(ln)


def count_occurrence(sample):
    grupo = {}
    for item in sample:
        if item in grupo:
            grupo[item] += 1
        else:
            grupo[item] = 1
    return grupo


# print(count_occurrence(stream))
path = r'C:\Users\User\PycharmProjects\pythonCODERHOUSE'
file = r'\AUN_2.csv'
xpr = 'ADD-AUN:'
x = 0
aun0 = {}
with open(path + file) as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        print(line)
        # if checkline(line):
        #     if xpr in line[0]:
        #         a = line[0].split(':')
        #         grno = a[1]
        #         stations = line[3]
        #         aun0.update({grno: stations})
        #     else:
        #         continue
        # else:
        #     continue


for k, v in aun0.items():
    print(k, v)
print(f'\nEncontré: {len(aun0)} grupos')

'''Hay veces que la gente, me incluyo, no sabe hasta dónde llegan las
consecuencias (cagadas) de sus actos. Otros, más felices, empujados por 
un sano desinterés o la fortuna, tampoco saben (quizás no sea necesario el
detalle) de hasta dónde llega el bien que movilizan'''