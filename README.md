# tonyStark

## Overview

The `clap-detection.py` program is designed to detect claps or loud sounds using a microphone. When a clap is detected, it triggers an action (in this case, playing an MP3 file from a directory). The program uses `pyaudio` to capture audio, processes the audio data in real-time, and calculates the Root Mean Square (RMS) value to detect claps based on predefined thresholds.

## Features

- **Clap detection**: Listens to audio input and identifies claps by measuring sound amplitude.
- **Threshold management**: Dynamically adjusts sensitivity based on the audio environment.
- **MP3 playback**: Upon detecting a clap, an MP3 file from a specified directory is played.
  
More features and Python files will be integrated into this program in the future.

## Dependencies

This program requires the following Python libraries:

- `pyaudio`: To capture audio input from the microphone.
- `struct`: For unpacking audio data.
- `math`: To compute the RMS value.
- `playmp3`: A custom module for playing MP3 files from a directory.

To install `pyaudio`, use the following command:

```bash
pip install pyaudio
```

Ensure that you have a valid MP3 file directory set up for playback.

## How It Works

1. **Microphone Input**: The program opens a microphone stream using `pyaudio`.
2. **Audio Processing**: It continuously reads audio blocks (short chunks of audio data).
3. **RMS Calculation**: For each block, the program calculates the RMS value, which indicates the volume of the sound.
4. **Clap Detection**: If the RMS value exceeds a threshold, the program considers it a "clap" and performs an action.
5. **MP3 Playback**: Once a clap is detected, the program plays an MP3 file using the `playmp3` module.

## Parameters

- `INITIAL_TAP_THRESHOLD`: Initial threshold to detect claps. Adjust this value to change the sensitivity.
- `FORMAT`: Audio format (16-bit PCM).
- `RATE`: Sampling rate (44.1 kHz).
- `CHANNELS`: Number of audio channels (mono).
- `INPUT_BLOCK_TIME`: Time duration for each audio block (0.05 seconds).
- `OVERSENSITIVE`: Number of noisy blocks required to increase the threshold.
- `UNDERSENSITIVE`: Number of quiet blocks required to decrease the threshold.
- `MAX_TAP_BLOCKS`: Maximum duration a clap sound can last for detection.

## Usage

1. Ensure you have a microphone connected to your system.
2. Create a directory with MP3 files for playback. Update the path in `playmp3.play_mp3s_from_directory()` to point to your directory.
3. Run the script:

```bash
python clap-detection.py
```

4. The program will listen for claps and play an MP3 file when a clap is detected.

## Future Development

- Integration with additional modules for more complex sound detection tasks.
- Fine-tuning of threshold settings for different environments.
- Additional audio feedback or actions triggered by claps.

## Known Issues

- **Error Handling**: Occasional errors while reading audio input (e.g., device issues) are handled but may result in missed detections.
- **Device Compatibility**: The program tries to find a suitable microphone but defaults to the system's default input device if no specific device is found.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
