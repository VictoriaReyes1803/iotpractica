# ... (definición de clases y código anterior)

# Tu diccionario
data = [{'arreglo': [], 'num': 1, 'nombre': 'CineCity', 'ubi': 'Centro', 'capacidad': 300, 'numero_salas': 5, 'clasificacion': 'A', 'salas': [{'arreglo': [], 'numero_sala': 1, 'capacidad': 50, 'formato_pantalla': '3D', 'sonido': 'Dolby Atmos', 'tipo': 'VIP', 'funciones': [{'arreglo': [], 'nf': 1, 'hora_inicio': '18:00', 'duracion': '2 horas', 'tipo_proyeccion': 'Digital', 'precio_entrada': 10.5, 'pelicula': 'Spider-Man: No Way Home'}]}]}, {'arreglo': [], 'num': 2, 'nombre': 'CineStar', 'ubi': 'Sur', 'capacidad': 200, 'numero_salas': 3, 'clasificacion': 'B', 'salas': [{'arreglo': [], 'numero_sala': 2, 'capacidad': 40, 'formato_pantalla': '2D', 'sonido': 'DTS', 'tipo': 'Regular', 'funciones': [{'arreglo': [], 'nf': 2, 'hora_inicio': '20:30', 'duracion': '2.5 horas', 'tipo_proyeccion': 'IMAX', 'precio_entrada': 15.0, 'pelicula': 'Gwen Stacy: Into the Spider-Verse'}]}]}]

# Crear instancias de la clase Cines
cines_list = []
for cine_data in data:
    cine_instance = Cines(
        num=cine_data['num'],
        nombre=cine_data['nombre'],
        ubi=cine_data['ubi'],
        capacidad=cine_data['capacidad'],
        numero_salas=cine_data['numero_salas'],
        clasificacion=cine_data['clasificacion']
    )

    # Crear instancias de la clase Salas y agregarlas al cine
    for sala_data in cine_data['salas']:
        sala_instance = Salas(
            numero_sala=sala_data['numero_sala'],
            capacidad=sala_data['capacidad'],
            formato_pantalla=sala_data['formato_pantalla'],
            sonido=sala_data['sonido'],
            tipo=sala_data['tipo']
        )

        # Crear instancias de la clase Funciones y agregarlas a la sala
        for funcion_data in sala_data['funciones']:
            funcion_instance = Funciones(
                nf=funcion_data['nf'],
                hora_inicio=funcion_data['hora_inicio'],
                duracion=funcion_data['duracion'],
                tipo_proyeccion=funcion_data['tipo_proyeccion'],
                precio_entrada=funcion_data['precio_entrada'],
                pelicula=funcion_data['pelicula']
            )

            sala_instance.funciones.agregar(funcion_instance)

        cine_instance.salas.agregar(sala_instance)

    cines_list.append(cine_instance)

# Ahora, cines_list contiene instancias de la clase Cines con toda la estructura de datos del diccionario convertida en objetos.
