diccionario = {"codigo": ["A-001","A-002", "A-003", "A-004", "A-005"],
             "nombre": ["luis", "gonzalo", "nicolas", "diego", "carlos"],
             "cursos": ["matematica", "comunicacion", "quimica", "historia", "geografia"]}
listadiccionario=[]
promediototal = 0
resp = "s"
while resp == "s":
    codigo = input("ingresar el codigo del alumno")

    cursos = int(input("ingresar la nota"))


    print("el promdio final es:", promediototal)


    f = open("demofile.txt", "w")
    f.write("\n" + cadena)
    f.close()
    f = open("demofile.txt")
    print(f.read())
    f.close()

