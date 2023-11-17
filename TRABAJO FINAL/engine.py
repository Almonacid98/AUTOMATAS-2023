import csv
import re

class Engine:
    def __init__(self):
        self.__sorted_tracks = []
    
    def reset_tracks(self):
        self.__sorted_tracks = []

    def load_tracks(self, column):
        self.reset_tracks()
        valid_columns = ["Likes", "Comments", "Views", "Duration_ms", "Stream", "Track"]
        if column not in valid_columns:
            print(f"Error: La columna {column} no es válida.")
            return []

        with open("Listado_temas_2023.csv", "r") as file:
            reader = csv.DictReader(file)

            # Ajustamos el método de ordenamiento para manejar columnas no numéricas
            if column not in ["Track"]:
                key_function = lambda x: float(x[column]) if x[column].replace('.', '', 1).isdigit() else 0
            else:
                key_function = lambda x: x[column]

            self.__sorted_tracks = sorted(reader, key=key_function, reverse=True)

        return self.__sorted_tracks

    def list_top5(self, column):
        sorted_tracks = self.load_tracks(column)
        print(f"\nTop 5 by {column}:")
        
        seen_tracks = set()
        i = 0
        while len(seen_tracks) < 5 and i < len(sorted_tracks):
            track_name = sorted_tracks[i]['Track']
            if track_name not in seen_tracks:
                seen_tracks.add(track_name)
                print(f"{len(seen_tracks)}. {track_name} - {sorted_tracks[i][column]} {column}")
            i += 1
    def list_for_ratio(self):
        # Cargar la columna "Track"
        track_column = "Track"
        self.load_tracks(track_column)

        # Calcular el ratio (Likes/Views) y agregarlo como una nueva columna
        for track in self.__sorted_tracks:
            likes = float(track['Likes']) if track['Likes'] else 0
            views = float(track['Views']) if track['Views'] else 0
            ratio = likes / views if views != 0 else 0
            track['Ratio'] = ratio

        # Ordenar las canciones por el ratio de forma descendente
        self.__sorted_tracks.sort(key=lambda x: x['Ratio'], reverse=True)

        # Mostrar las 5 canciones con el mejor ratio
        print("\nTop 5 canciones con mejor ratio (Likes/Views):")
        for i, track in enumerate(self.__sorted_tracks[:5], start=1):
            print(f"{i}. {track['Track']} - Ratio: {track['Ratio'] * 100:.2f}%")