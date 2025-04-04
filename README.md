# Clipboard Manager

## Overview

A simple clipboard monitoring tool that tracks and displays everything you copy during a session. Great for productivity and keeping track of temporary data.

## Feature

- Tracks new clipboard content in real-time
- Automatically stores and displays clipboard history
- Lightweight and runs in the terminal

## Installation

Install the required library:
```sh
pip install pyperclip
```

## How to use

1. Clone the repository:
    ```sh
    git clone https://github.com/Aditya15267/clipboard-manager.git
2. Run the script:
    ```sh
    python clipboard_manager.py
    ```

    - Starts listening to clipboard changes.
    - Press ```Ctrl+C``` to stop and view clipboard history.

## Example output

```yaml
Clipboard Manager started. Press Ctrl+C to stop.
Copied: Hello
Copied: Hello World
Copied: python is awesome

Clipboard Manager stopped.

Clipboard History:
1: Hello
2: Hello World
3: python is awesome
```