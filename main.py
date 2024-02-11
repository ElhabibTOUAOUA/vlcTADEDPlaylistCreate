import os
import urllib.parse


def generate_playlist_and_config(folder_path, course_name):
    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            raise FileNotFoundError("Folder path does not exist.")

        # Get the root folder of the drive
        drive, _ = os.path.splitdrive(folder_path)
        root_folder = os.path.splitdrive(os.path.abspath(folder_path))[1]

        # Generate playlist content
        playlist_base_url = f"file:///{drive}/"
        playlist_content = "-- vlcTADED Playlist --\n\n{}\n\n".format(
            playlist_base_url)
        config_content = f"-- vlcTADED Config --\n{course_name}\n"

        # Loop through files in the folder
        for root, _, files in os.walk(folder_path):
            for filename in files:
                if filename.endswith(('.mp4', '.avi', '.mkv', '.mov')):
                    file_path = os.path.join(root, filename)
                    rel_path = os.path.relpath(
                        file_path, drive).replace('\\', '/')
                    playlist_content += f"{rel_path}\n{filename}\n"

        # Write playlist to a text file
        playlist_file_name = f"{course_name} Playlist.txt"
        playlist_file_path = os.path.join(folder_path, playlist_file_name)
        with open(playlist_file_path, 'w', encoding='utf-8') as f:
            f.write(playlist_content)

        # Write config to a text file
        config_file_name = f"{course_name} Config.txt"
        config_file_path = os.path.join(folder_path, config_file_name)
        with open(config_file_path, 'w', encoding='utf-8') as f:
            f.write(config_content)

        print("Playlist file has been saved to", playlist_file_path)
        print("Config file has been saved to", config_file_path)
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    folder_path = input("Enter the folder path: ").strip()
    course_name = input("Enter the course name: ").strip()
    generate_playlist_and_config(folder_path, course_name)


if __name__ == "__main__":
    main()
