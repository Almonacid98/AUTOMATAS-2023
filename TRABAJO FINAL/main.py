from engine import Engine

# Menú principal
def menu():
    engine = Engine()
    archivo = "Listado_temas_2023.csv"
    valid_columns = ["Likes", "Comments", "Views", "Duration_ms", "Stream"]
    
    while True:
        print("\nMenú:")
        print("1. Listar Top 5 de canciones por distintos parametros")
        print("2. Obtener Top 5 de ratio")
        print("3. Buscar canción por nombre")
        print("4. Agregar nueva canción")
        print("5. Obtener Top 10 de canciones por duración")
        print("6. Obtener Top 10 de artistas")
        print("7. Guardar cambios y salir")
        print("8. Salir")
        opcion = input("Ingrese la opción: ")

        if opcion == "1":
            print("\nSelect any of the following columns:")
            for i, selection in enumerate(valid_columns):
                print(f"{i+1}. {selection}")
            print("0. Exit")
            selection = int(input("Ingrese la opción: "))
            
            if selection not in range(len(valid_columns) + 1):
                print(f"Error: La opción {selection} no es válida.")
                continue
            elif selection == 0:
                break
            else:
                engine.list_top5(valid_columns[selection - 1])

        elif opcion == "2":
            engine.list_for_ratio()
        elif opcion == "3":
            parte_nombre = input("Ingrese parte del nombre de la canción: ")
            engine.buscar_cancion()
        elif opcion == "4":
            engine.agregar_nueva_fila()
        elif opcion == "5":
            engine.obtener_top10_duracion()
        elif opcion == "6":
            engine.obtener_top10_artistas()
        elif opcion == "7":
            engine.escribir_archivo_csv(archivo, )  # Guardar cambios antes de salir
            break
        elif opcion == "8":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
