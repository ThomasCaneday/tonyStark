# tonyStark

## Overview

This project contains multiple Python scripts working together to detect claps, record audio, and handle MP3 playback. It integrates audio input/output functionalities using `pyaudio` and `pygame`, making it suitable for audio-triggered actions and basic audio recording and processing.

## Features

- **Clap Detection**: Detects claps using real-time microphone input and triggers an action (such as playing an MP3 file).
- **MP3 Playback**: Plays MP3 files from a specified directory in response to detected claps.
- **Audio Recording**: Records audio input from the microphone, saves it as a WAV file, and converts it to MP3.
- **Dynamic Thresholds**: Adjusts sensitivity to detect claps in various audio environments.

More features will be added in the future as additional Python files are integrated.

## Dependencies

This project requires the following Python libraries:

- `pyaudio`: For capturing audio input and managing streams.
- `pygame`: For playing MP3 files.
- `os`: For file directory management.
- `wave`: For saving audio as WAV files.
- `pydub`: For converting WAV files to MP3.
- `threading`: For running audio recording and key-press listeners concurrently.

To install the required dependencies, run:

```bash
pip install pyaudio pygame pydub
```

Make sure you have `ffmpeg` installed for `pydub` to handle MP3 conversion:

- On Ubuntu: `sudo apt install ffmpeg`
- On macOS: `brew install ffmpeg`
- On Windows: [Download ffmpeg](https://ffmpeg.org/download.html)

## How It Works

### `clap-detection.py`

This script listens for claps using the microphone and triggers an MP3 playback when a clap is detected.

1. **Microphone Input**: Captures real-time audio using `pyaudio`.
2. **RMS Calculation**: Computes the Root Mean Square (RMS) to detect the volume of the sound.
3. **Clap Detection**: If the volume exceeds a threshold, it detects a clap and triggers MP3 playback.
4. **MP3 Playback**: Calls the function from `playmp3.py` to play MP3 files.

### `playmp3.py`

This script handles MP3 file playback.

1. **MP3 Discovery**: Retrieves all `.mp3` files from a specified directory.
2. **MP3 Playback**: Uses `pygame` to play each MP3 file in order.

### `recording.py`

This script allows you to record audio input from the microphone, save it as a WAV file, and convert it to MP3.

1. **Audio Recording**: Records audio input using `pyaudio` and saves it as a WAV file.
2. **MP3 Conversion**: Converts the WAV file to MP3 using the `pydub` library.
3. **Threading**: Uses separate threads to handle real-time recording and listen for a key press to stop recording.

## Parameters

### Clap Detection (`clap-detection.py`):
- `INITIAL_TAP_THRESHOLD`: Adjusts the sensitivity of the clap detection.
- `FORMAT`, `RATE`, `CHANNELS`, `INPUT_BLOCK_TIME`: Configurable audio input parameters for `pyaudio`.
- `OVERSENSITIVE`, `UNDERSENSITIVE`, `MAX_TAP_BLOCKS`: Threshold controls for handling noisy and quiet environments.

### MP3 Playback (`playmp3.py`):
- `directory`: Path to the folder where MP3 files are stored.

### Audio Recording (`recording.py`):
- `FORMAT`, `CHANNELS`, `RATE`, `CHUNK`: Audio input parameters for recording.
- `WAVE_OUTPUT_FILENAME`: Name of the WAV file where audio is saved.
- `MP3_OUTPUT_FILENAME`: Name of the MP3 file generated from the WAV file.

## Usage

### Running Clap Detection

To run the clap detection script:

```bash
python clap-detection.py
```

The program will listen for claps and play MP3 files from the specified directory when a clap is detected.

### Running MP3 Playback

You can run the `playmp3.py` script standalone to play all MP3 files in a directory:

```bash
python playmp3.py /path/to/your/mp3/directory
```

### Recording Audio

To record audio, run:

```bash
python recording.py
```

Press `Enter` to stop the recording, and the program will save the recording as a WAV file and convert it to MP3.

## Example

- **Clap Detection**: Detect a clap and play MP3 files from the `../tonyStarkClap` directory.
  ```python
  playmp3.play_mp3s_from_directory("../tonyStarkClap")
  ```

- **Recording**: Record audio and convert it to MP3.
  ```bash
  python recording.py
  ```

## Future Development

- **Advanced Clap Detection**: Enhance the sensitivity adjustments for different environments.
- **Feature Expansion**: Add more features like sound classification or more advanced audio processing.
- **User Interface**: Implement a simple GUI for configuring thresholds and managing recordings.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

Contributions are welcome! Feel free to submit pull requests or open issues for improvements.
