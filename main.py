import os


def generate_playlist_and_config(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("Folder path does not exist.")
        return

    # Get the folder name
    folder_name = os.path.basename(folder_path)

    # Generate playlist content
    playlist_base_url = "file:///{}/".format(
        "/".join(folder_path.replace('\\', '/').split('/')[:-1]))
    playlist_content = "-- vlcTADED Playlist --\n\n{}\n\n".format(
        playlist_base_url)
    config_content = "-- vlcTADED Config --\n{}\n".format(folder_name)

    # Loop through files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(('.mp4', '.avi', '.mkv', '.mov')):
            file_path = os.path.join(folder_path, filename)
            url = "{}/{}".format(folder_name, filename.replace(' ', '%20'))
            playlist_content += "{}\n{}\n".format(url, filename)

    # Write playlist to a text file
    playlist_file_name = "{}Playlist.txt".format(folder_name)
    playlist_file_path = os.path.join(folder_path, playlist_file_name)
    with open(playlist_file_path, 'w', encoding='utf-8') as f:
        f.write(playlist_content)

    # Write config to a text file
    config_file_name = "{}Config.txt".format(folder_name)
    config_file_path = os.path.join(folder_path, config_file_name)
    with open(config_file_path, 'w', encoding='utf-8') as f:
        f.write(config_content)

    print("Playlist file has been saved to", playlist_file_path)
    print("Config file has been saved to", config_file_path)


def main():
    folder_path = input("Enter the folder path: ")
    generate_playlist_and_config(folder_path)


if __name__ == "__main__":
    main()