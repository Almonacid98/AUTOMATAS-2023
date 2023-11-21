from engine import Engine

# Menú principal
def menu():
    engine = Engine()
    
    while True:
        print("\nMenu:")
        print("1. List Top 5 songs by different parameters")
        print("2. Get Top 5 by ratio")
        print("3. Search for a song by name")
        print("4. Add a new song")
        print("5. Get Top 10 songs by duration")
        print("6. Get Top 10 artists")
        print("7. Save changes and exit")
        print("8. Exit")
        option = input("Enter your choice: ")

        if option == "1":
            print("\nSelect any of the following columns:")
            valid_columns = ["Likes", "Comments", "Views", "Duration_ms", "Stream"]
            for i, selection in enumerate(valid_columns):
                print(f"{i+1}. {selection}")
            print("0. Exit")
            selection = int(input("Enter your choice: "))
            
            if selection not in range(len(valid_columns) + 1):
                print(f"Error: Option {selection} is not valid.")
                continue
            elif selection == 0:
                break
            else:
                engine.list_top5(valid_columns[selection - 1])

        elif option == "2":
            engine.list_for_ratio()
        elif option == "3":
            partial_name = input("Enter part of the song name: ")
            engine.search_song(partial_name)
        elif option == "4":
            engine.add_new_row()
        elif option == "5":
            engine.get_top10_duration()
        elif option == "6":
            engine.get_top10_artists()
        elif option == "7":
            engine.write_csv_file()  # Save changes before exiting
            engine.clear_console()
            break
        elif option == "8":
            engine.clear_console()
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
