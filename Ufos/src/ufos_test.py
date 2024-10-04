from ufos import *

# Test de la función lee_avistamientos
Avistamientos = lee_avistamientos('Ufos\data\ovnis.csv')  

for a in Avistamientos[:5]:
    print(a)

#Test de la función duracion_total
print(duracion_total(Avistamientos, 'CA'))
   
# Test de la función comentario_mas_largo
print(comentario_mas_largo(Avistamientos, 'CA'))

#Test de la función indexa_formas_por_mes
print(indexa_formas_por_mes(Avistamientos))

# Test de la función avistamientos_fechas
fecha1 = datetime(2000, 1, 1)
fecha2 = datetime(2000, 12, 31)
print(avistamientos_fechas(Avistamientos, fecha1, fecha2))

# Test de la función hora_mas_avistamientos
print(hora_mas_avistamientos(Avistamientos))

# Test de la funcion dicc_estado_longitud_media_comentario
print(dicc_estado_longitud_media_comentario(Avistamientos))
