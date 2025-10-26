# README for KeyLogger

## Description

`KeyLogger` is a Python script designed to log keystrokes from the user's keyboard and send the logged data to a specified Discord webhook. It includes features for persistence and can run in the background, logging keys even after a system reboot.

## Features

- **Keystroke Logging**: Captures and logs all keystrokes, including special keys and modifiers (Ctrl, Alt, Shift).
- **Discord Webhook Integration**: Sends logged data to a specified Discord webhook.
- **Persistence**: Can add itself to the Windows startup folder to ensure it runs on system startup.
- **Debug Mode**: Provides detailed debug information if enabled.
- **Threading**: Uses threading to run the key logger and data sender concurrently.

## Requirements

- Python 3.x
- Additional libraries: `time`, `threading`, `requests`, `keyboard`, `os`, `sys`, `shutil`, `winshell`

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the necessary libraries:
   ```bash
   pip install requests keyboard
   ````
## Usage

### Configuration

- Set the `webhook` variable to your Discord webhook URL.
- Set the `debug` variable to `True` to enable debug mode.

### Running the Script

1. Run the script:
    
    bash
    

2. ```bash
    python key_logger.py
    ```
    
3. The script will start logging keystrokes and sending data to the specified Discord webhook.
4. To stop the script, press `Ctrl+C` in the terminal.

## Internal Workings

### Class `PersistenceManager`

- **`__init__`**: Initializes the instance with the debug setting.
- **`add_to_startup`**: Adds the script to the Windows startup folder to ensure it runs on system startup.
- **`run`**: Executes the persistence logic.

### Class `KeyLogger`

- **`__init__`**: Initializes the instance with the webhook URL, debug setting, and other parameters.
- **`listen_keys`**: Listens for keystrokes and appends them to the `keys_chain` list. Sends data to the webhook when the Enter key is pressed.
- **`send_data`**: Sends the logged keystrokes to the specified Discord webhook.
- **`send_to_discord_loop`**: Runs a loop to send data to the webhook at regular intervals.
- **`run`**: Starts the key logger and data sender threads.

### Function `main`

- **`main`**: The main function that initializes the `KeyLogger` and `PersistenceManager` and handles the main loop of the script.

## Notes

- This script is designed to work on Windows systems due to its use of `winshell` for startup persistence.
- The `keyboard` library is used for capturing keystrokes.
- The `requests` library is used for sending data to the Discord webhook.
- Ensure that the Discord webhook URL is correct and that the webhook is configured to receive messages.
- The script clears the screen before prompting for user input to keep the interface clean.
- The delay between sending emails can be adjusted to avoid rate limiting by email servers.

# DISCLAIMER:
This script is provided for educational and research purposes only. The author assumes no responsibility for any misuse, damage, or illegal activity caused by the use of this code. Use it at your own risk and ensure compliance with all applicable laws and regulations.
