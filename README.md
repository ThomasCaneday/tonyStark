# tonyStark

## Overview

This project contains multiple Python scripts working together to detect claps, play MP3s, record audio, and recognize speech. It integrates audio input/output functionalities using `pyaudio`, `pygame`, and `speech_recognition`, making it suitable for audio-triggered actions, speech-based interactions, and basic audio recording and processing.

## Features

- **Clap Detection**: Detects claps using real-time microphone input and triggers MP3 playback.
- **MP3 Playback**: Plays MP3 files from a specified directory in response to detected claps or speech commands.
- **Audio Recording**: Records audio input from the microphone, saves it as a WAV file, and converts it to MP3.
- **Speech Recognition**: Listens for voice commands and responds with appropriate actions, such as playing sound effects or delivering spoken responses.

More features will be added as additional Python files are integrated.

## Dependencies

The project requires the following Python libraries:

- `pyaudio`: For capturing audio input and managing streams.
- `pygame`: For playing MP3 files.
- `os`: For file directory management.
- `wave`: For saving audio as WAV files.
- `pydub`: For converting WAV files to MP3.
- `gTTS`: For text-to-speech functionality.
- `speech_recognition`: For speech-to-text conversion using Google's Speech Recognition API.
- `playsound`: For playing audio files.

To install the required dependencies, run:

```bash
pip install pyaudio pygame pydub gtts speechrecognition playsound
```

Make sure you have `ffmpeg` installed for `pydub` to handle MP3 conversion:

- On Ubuntu: `sudo apt install ffmpeg`
- On macOS: `brew install ffmpeg`
- On Windows: [Download ffmpeg](https://ffmpeg.org/download.html)

## How It Works

### `clap-detection.py`

This script listens for claps and triggers an MP3 playback when a clap is detected.

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

### `speech_recognition.py`

This script listens for voice commands using the microphone and responds with appropriate actions:

1. **Speech Recognition**: Uses the `speech_recognition` library to capture and recognize speech via Google Speech Recognition API.
2. **Voice Commands**: Recognizes specific phrases (e.g., "Wake up", "Jarvis you there", "Shut down") and plays corresponding audio files or responds using `gTTS` for text-to-speech.
3. **Action Triggers**: Based on recognized phrases, it triggers different actions, such as playing MP3 files, booting up a system sound, or shutting down the program.

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

### Speech Recognition (`speech_recognition.py`):
- `recognizer.adjust_for_ambient_noise`: Adjusts the microphone sensitivity based on the surrounding noise.
- Phrases to recognize:
  - "Wake up", "Wake up daddy's", "Wake up daddy's home": Responds with a welcome message and plays MP3 files from a directory.
  - "Jarvis you there": Responds with "At your service" and plays a startup sound.
  - "Boot up Jarvis": Plays the startup sound.
  - "Shut down": Exits the program with a farewell message.

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

### Voice Command Recognition

To use speech recognition and respond to voice commands:

```bash
python speech_recognition.py
```

The program will listen for specific phrases and respond accordingly by playing sounds or generating text-to-speech responses.

## Example

- **Clap Detection**: Detect a clap and play MP3 files from the `../tonyStarkClap` directory.
  ```python
  playmp3.play_mp3s_from_directory("../tonyStarkClap")
  ```

- **Recording**: Record audio and convert it to MP3.
  ```bash
  python recording.py
  ```

- **Voice Command**: Recognize the phrase "Wake up" and respond with a welcome message.
  ```bash
  python speech_recognition.py
  ```

## Future Development

- **Enhanced Clap Detection**: Improve sensitivity to work in noisy environments.
- **Additional Voice Commands**: Expand the list of recognized phrases and actions.
- **Feature Expansion**: Add more functionalities like sound classification and audio processing.
- **User Interface**: Implement a GUI for controlling various features and configuring settings.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

Contributions are welcome! Feel free to submit pull requests or open issues for improvements.
