import csv
import re

class AddSongEngine:

    def add_new_song():
        csv_file = 'Listado_temas_2023.csv'
        try:
            with open(csv_file, 'a', newline='', encoding='utf-8') as file:
                # Define las columnas que se agregarán
                columns = ['Artist', 'URL_spotify', 'Track', 'Album', 'Album type', 'url', 'Duration_ms', 'URL_youtube', 'title']
                writer = csv.DictWriter(file, fieldnames=columns)

                # Pide datos al usuario
                new_song_data = {}
                for column in columns:
                    user_input = input(f"Enter {column}: ")
                    # Aplica validaciones 
                    if column == 'URL_spotify':
                        spotify_url_pattern = re.compile(r'^https://open\.spotify\.com/artist/[a-zA-Z0-9]+$')
                        if not spotify_url_pattern.match(user_input):
                            print("Invalid Spotify URL. Please enter a valid Spotify URL.")
                            return
                    elif column == 'url':
                        url_pattern = re.compile(r'^(https?://[^\s]+|spotify:track:[a-zA-Z0-9]+)$')
                        if not url_pattern.match(user_input):
                            print("Invalid URL. Please enter a valid URL.")
                            return
                    elif column == 'Duration_ms':
                        duration_pattern = re.compile(r'^\d+$')
                        if not duration_pattern.match(user_input):
                            print("Invalid duration. Please enter a valid duration in milliseconds.")
                            return
                    elif column == 'URL_youtube':
                        youtube_url_pattern = re.compile(r'^https://www\.youtube\.com/watch\?v=[a-zA-Z0-9_-]+$')
                        if not youtube_url_pattern.match(user_input):
                            print("Invalid YouTube URL. Please enter a valid YouTube URL.")
                            return

                    new_song_data[column] = user_input
                writer.writerow(new_song_data)

                print("New song added successfully!")

        except FileNotFoundError:
            print(f"El archivo {csv_file} no fue encontrado.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")


    def add_multiple_songs_from_file():
        csv_file = 'Listado_temas_2023.csv'
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
