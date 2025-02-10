import csv
alumnos = []
with open(r"C:/Users/dorado.gumoi24_trian/Desktop/Python/MoisesDorado_Python_Ej2/notas.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        notas = {key: int(value) for key, value in row.items() if key not in ["Nombre", "Apellidos", "Curso"]}
        alumnos.append({"nombre": row["Nombre"], "apellidos": row["Apellidos"], "curso": row["Curso"], "notas": notas})

print(alumnos)