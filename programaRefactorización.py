def iniciar_programa():
    while True:
        mostrar_menu()
        point = solicitar_opcion()

        if point == 1:
            ingresar_puntuacion_y_comentario()
        elif point == 2:
            comprobar_resultados()
        elif point == 3:
            print('Finalizando')
            break

def mostrar_menu():
    print('Seleccione el proceso que desea aplicar:')
    print('1: Ingresar puntuación y comentario')
    print('2: Comprueba los resultados obtenidos hasta ahora.')
    print('3: Finalizar')
def solicitar_opcion():
    while True:
        point = input("Introduzca una opción (1-3): ")
        if point.isdecimal():
            point = int(point)
            if 1 <= point <= 3:
                return point
        print('Por favor, introduzca un número del 1 al 3')
def ingresar_puntuacion_y_comentario():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            
            if point <= 0 or point > 5:
                print('Por favor, introduzca un valor entre el 1 y 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post} \n')
                break
        else:
            print('Por favor, introduzca la puntuación en números')

def comprobar_resultados():
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", "r") as read_file:
            data = read_file.read()
            if data:
                print(data)
            else:
                print("No hay resultados almacenados aún.")
    except FileNotFoundError:
        print("No hay resultados almacenados aún.")

iniciar_programa()