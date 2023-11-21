import csv
import re
import os

class Engine:
    def __init__(self):
        self.__sorted_tracks = []
    
    
    
    def clear_console(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    
    def reset_tracks(self):
        self.__sorted_tracks = []

    def validate_input(self, prompt, regex_pattern):
            while True:
                user_input = input(prompt)
                if re.match(regex_pattern, user_input):
                    return user_input
                else:
                    print(f"Invalid input format. Please enter a valid value.")
    def load_tracks(self, column):
        self.reset_tracks()
        valid_columns = ["Likes", "Comments", "Views", "Stream", "Track"]
        if column not in valid_columns:
            print(f"Error: The column {column} isn't valid.")
            return []

        with open("Listado_temas_2023.csv", "r") as file:
            reader = csv.DictReader(file)

            # Sort by column (descending)
            if column not in ["Track"]:
                key_function = lambda x: float(x[column]) if x[column].replace('.', '', 1).isdigit() else 0
            else:
                key_function = lambda x: x[column]

            self.__sorted_tracks = sorted(reader, key=key_function, reverse=True)

        return self.__sorted_tracks

    def list_top5(self, column):
        sorted_tracks = self.load_tracks(column)
        self.clear_console()
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
        # Load "Track" column
        track_column = "Track"
        self.load_tracks(track_column)

        # Calculate ratio(Likes/Views) and add a new column
        for track in self.__sorted_tracks:
            likes = float(track['Likes']) if track['Likes'] else 0
            views = float(track['Views']) if track['Views'] else 0
            ratio = likes / views if views != 0 else 0
            track['Ratio'] = ratio

        # Short the tracks by ratio (descending)
        self.__sorted_tracks.sort(key=lambda x: x['Ratio'], reverse=True)

        # Show Top 5 tracks by Ratio
        print("\nTop 5 songs with the best ratio (Likes/Views):")
        self.clear_console()
        for i, track in enumerate(self.__sorted_tracks[:5], start=1):
            print(f"{i}. {track['Track']} - Ratio: {track['Ratio'] * 100:.2f}%")
    

    def add_new_row(self):
        new_row = {}

        new_row["Artist"] = input("Enter Artist: ")

        url_spotify_prompt = "Enter URL_spotify: "
        url_spotify_pattern = r'https://open\.spotify\.com/artist/[a-zA-Z0-9]+$'
        new_row["URL_spotify"] = self.validate_input(url_spotify_prompt, url_spotify_pattern)

        new_row["Track"] = input("Enter Track: ")
        new_row["Album"] = input("Enter Album: ")

        album_type_prompt = "Enter Album type: "
        album_type_pattern = r'^[a-z]+$'
        new_row["Album type"] = self.validate_input(album_type_prompt, album_type_pattern)

        uri_prompt = "Enter uri: "
        uri_pattern = r'spotify:track:[a-zA-Z0-9]+$'
        new_row["uri"] = self.validate_input(uri_prompt, uri_pattern)

        new_row["Duration_ms"] = input("Enter Duration_ms: ")
        
        youtube_prompt = "Enter URL_youtube: "
        youtube_pattern = r'^https://www\.youtube\.com/watch\?v=[a-zA-Z0-9_-]+$'
        new_row["URL_youtube"] = self.validate_input(youtube_prompt, youtube_pattern)

        new_row["title"] = input("Enter title: ")

        
        with open("Listado_temas_2023.csv", "a", newline="") as file:
            fieldnames = ["Artist", "URL_spotify", "Track", "Album", "Album type", "url", "Duration_ms", "URL_youtube", "title"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            
            writer.writerow(new_row)

        print("New row added successfully!")