import csv
import re

class AddSong:
    @staticmethod
    def convert_to_milliseconds():
        duration_input = input("Enter duration (minutes:seconds): ")
        minutes, seconds = map(int, duration_input.split(':'))
        try:
            minutes = int(minutes)
            seconds = int(seconds)
            duration_ms = (minutes * 60 + seconds) * 1000
            return duration_ms
        except ValueError:
            print("Invalid input. Please enter valid numbers for minutes and seconds.")
            return None
    @staticmethod
    def validate_input(prompt, regex_pattern):
        while True:
            user_input = input(prompt)
            if re.match(regex_pattern, user_input):
                return user_input
            else:
                print(f"Invalid input format. Please enter a valid value.")
    @staticmethod
    def add_new_song():
        new_row = {}

        # Pedir datos por consola
        new_row["Artist"] = input("Enter Artist: ")

        # Validar y pedir Spotify URL hasta que sea válida
        spotify_prompt = "Enter Spotify URL (artist/track): "
        spotify_url_pattern = re.compile(r'^https://open\.spotify\.com/(artist|track)/[a-zA-Z0-9_-]+(\?si=[a-zA-Z0-9]+)?$')
        new_row["URL_spotify"] = AddSong.validate_input(spotify_prompt, spotify_url_pattern)

        new_row["Track"] = input("Enter Track: ")
        new_row["Album"] = input("Enter Album: ")
        new_row["Album type"] = input("Enter Album type: ")

        # Validar y pedir URL_youtube hasta que sea válida
        youtube_prompt = "Enter URL_youtube: "
        youtube_pattern = r'^https://www\.youtube\.com/watch\?v=[a-zA-Z0-9_-]+$'
        new_row["URL_youtube"] = AddSong.validate_input(youtube_prompt, youtube_pattern)

        new_row["Duration_ms"] = AddSong.convert_to_milliseconds()
        new_row["title"] = input("Enter title: ")
        with open("Listado_temas_2023.csv", "a", newline="") as file:
            fieldnames = ["Artist", "URL_spotify", "Track", "Album", "Album type", "url", "Duration_ms", "URL_youtube", "title"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Escribir la nueva fila en el archivo CSV
            writer.writerow(new_row)

        print("New row added successfully!")

    @staticmethod
    def add_multiple_songs_from_file():
        csv_file = './Listado_temas_2023.csv'
        try:
            with open(csv_file, 'a', newline='', encoding='utf-8') as file:
                columns = ['Artist', 'URL_spotify', 'Track', 'Album', 'Album type', 'url', 'Duration_ms', 'URL_youtube', 'title']
                writer = csv.DictWriter(file, fieldnames=columns)

                file_path = input("Enter the path of the file with new songs: ")
                with open(file_path, 'r', encoding='utf-8') as input_file:
                    for line in input_file:
                        line_data = dict(zip(columns, line.strip().split(',')))
                        writer.writerow(line_data)
                print("Multiple songs added successfully!")

        except FileNotFoundError:
            print(f"El archivo {csv_file} no fue encontrado.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
