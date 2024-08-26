import os
import pygame

def play_mp3s_from_directory(directory):
    # Initialize the mixer module
    pygame.mixer.init()

    # Get all mp3 files in the directory
    mp3_files = [f for f in os.listdir(directory) if f.endswith('.mp3')]

    if not mp3_files:
        print("No MP3 files found in the directory.")
        return

    # Sort the files to play them in order
    mp3_files.sort()

    # Play each mp3 file
    for mp3_file in mp3_files:
        mp3_path = os.path.join(directory, mp3_file)
        print(f"Now playing: {mp3_file}")
        pygame.mixer.music.load(mp3_path)
        pygame.mixer.music.play()

        # Wait for the music to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Check every 100ms if the music is still playing

    print("Finished playing all MP3 files.")

# Example usage
if __name__ == "__main__":
    import argparse

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Play all MP3 files in a directory")
    parser.add_argument("directory", help="Path to the directory containing MP3 files")

    args = parser.parse_args()

    play_mp3s_from_directory(args.directory)
