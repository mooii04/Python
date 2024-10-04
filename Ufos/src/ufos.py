import csv
from datetime import datetime
from math import sqrt
from collections import namedtuple, Counter, defaultdict

Avistamiento = namedtuple('Avistamiento', 'fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud')

# Test de la función lee_avistamientos
def lee_avistamientos(fichero):
    res= []
   
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for x in lector:
            fecha_hora = x[0]
            fechahora = datetime.strptime(fecha_hora, '%m/%d/%Y %H:%M')
            ciudad = x[1]
            estado = x[2]
            forma = x[3]
            duracion = int(x[4])
            comentarios = x[5]
            latitud= float(x[6])
            longitud= float(x[7])
            tupla = Avistamiento(fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud)
            res.append(tupla)

    return res     

#Test de la función duracion_total
def duracion_total(avistamientos, estado):
    duracion = 0
    for a in avistamientos:
        if a.estado == estado:
            duracion += a.duracion
    return duracion

# Test de la función comentario_mas_largo
def comentario_mas_largo(avistamientos, estado):
    comentarios = []
    for a in avistamientos:
        if a.estado == estado:
            comentarios.append(a.comentarios)
    if comentarios:
        return max(comentarios, key=len)
    else:
        return None

# Test de la función indexa_formas_por_mes
def indexa_formas_por_mes(avistamientos):
    res = defaultdict(Counter)
    for a in avistamientos:
        mes = a.fechahora.month
        res[mes][a.forma] += 1
    return res

# Test de la función avistamientos_fechas
def avistamientos_fechas(avistamientos, fecha1, fecha2):
    res = []
    for a in avistamientos:
        if fecha1 <= a.fechahora <= fecha2:
            res.append(a)
    return res

# Test de la función hora_mas_avistamientos
def hora_mas_avistamientos(avistamientos):
    horas = Counter(a.fechahora.hour for a in avistamientos)
    return horas.most_common(1)[0]

# Test de la funcion dicc_estado_longitud_media_comentario
def dicc_estado_longitud_media_comentario(avistamientos):
    dicc = defaultdict(lambda: [0, 0, 0])
    for a in avistamientos:
        dicc[a.estado][0] += 1
        dicc[a.estado][1] += a.longitud
        dicc[a.estado][2] += len(a.comentarios)
    for estado, (n, longitud, comentarios) in dicc.items():
        dicc[estado][1] = longitud / n
        dicc[estado][2] = comentarios / n
    return dicc


