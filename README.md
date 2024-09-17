# tonyStark

## Overview

The `clap-detection.py` program is designed to detect claps or loud sounds using a microphone. When a clap is detected, it triggers an action (such as playing MP3 files from a directory). The program leverages `pyaudio` to capture audio, processes the audio data in real-time, and calculates the Root Mean Square (RMS) value to detect claps based on predefined thresholds.

The program integrates with additional Python files, such as `playmp3.py`, which handles MP3 playback functionality.

## Features

- **Clap detection**: Listens for claps by measuring sound amplitude through RMS calculations.
- **Dynamic threshold adjustment**: Automatically adjusts sensitivity to detect claps in noisy or quiet environments.
- **MP3 playback**: Plays MP3 files from a specified directory when a clap is detected.
  
More Python files and features will be integrated into this program in the future.

## Dependencies

This program requires the following Python libraries:

- `pyaudio`: For capturing audio input from the microphone.
- `struct`: For unpacking audio data.
- `math`: For calculating the RMS value of the audio input.
- `pygame`: For playing MP3 files.
- `os`: For file directory management.

To install the necessary dependencies, run:

```
pip install pyaudio pygame
```

Ensure that a valid MP3 file directory is available for playback.

## How It Works

### `clap-detection.py`

1. **Microphone Input**: The program opens a microphone stream using `pyaudio`.
2. **Audio Processing**: Continuously reads short blocks of audio data.
3. **RMS Calculation**: For each block, the program calculates the RMS value, indicating the volume of the sound.
4. **Clap Detection**: If the RMS value exceeds a predefined threshold, the program registers a "clap" and triggers an action (e.g., playing MP3 files).
5. **MP3 Playback**: When a clap is detected, the program calls the `play_mp3s_from_directory()` function from `playmp3.py` to play MP3 files from a specified directory.

### `playmp3.py`

1. **MP3 File Discovery**: This script retrieves all `.mp3` files from a specified directory.
2. **MP3 Playback**: Uses the `pygame` library to load and play MP3 files one by one in alphabetical order.
3. **Playback Control**: Waits for the current MP3 file to finish before playing the next one.

## Parameters

- **Clap Detection (clap-detection.py)**:
  - `INITIAL_TAP_THRESHOLD`: Initial threshold for detecting claps. Adjust this value to control sensitivity.
  - `OVERSENSITIVE` and `UNDERSENSITIVE`: Values that adjust the threshold based on continuous noise or quietness.
  - `MAX_TAP_BLOCKS`: Maximum duration a sound can last to still be considered a clap.

- **MP3 Playback (playmp3.py)**:
  - `directory`: Path to the folder where the MP3 files are stored.

## Usage

### Running Clap Detection

1. Ensure you have a microphone connected to your system.
2. Create a directory with MP3 files for playback. Update the path in `playmp3.play_mp3s_from_directory()` to point to your directory.
3. Run the clap detection script:

```
python clap-detection.py
```

The program will listen for claps and play MP3 files from the specified directory when a clap is detected.

### Running MP3 Playback Script

You can also run `playmp3.py` as a standalone script to play all MP3 files in a directory:

```
python playmp3.py /path/to/your/mp3/directory
```

## Example

In `clap-detection.py`, when a clap is detected, it will trigger the playback of MP3 files from the `../tonyStarkClap` directory.

```python
playmp3.play_mp3s_from_directory("../tonyStarkClap")
```

You can change this path to any directory containing MP3 files.

## Future Development

- **More Sound Detection Features**: Additional actions triggered by different types of sounds.
- **User Interface**: A simple GUI for setting thresholds and controlling playback.
- **Advanced Sensitivity Adjustments**: More refined noise filtering for varying environments.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
