# PiPhone UI

A lightweight, terminal-based UI built with Textual for a Raspberry Pi Zero W phone.

Instead of using a desktop environment, PiPhone UI provides a simple application launcher for essential applications while keeping resource usage basically non-existent.

![Home screen of the PiPhone UI](media/Home%20Screen.png)

## Under Construction 🏗️
1. Screens ⚠️
    1. Home Screen ✔️
    2. Settings ❌
    3. Notes ❌
2. Features ⚠️
    1. Launching apps ✔️
    2. Message Of The Day ✔️
    3. Date and Time ✔️
    4. WiFi management ❌
    5. Messaging ❌
    6. Note taking ❌

## Todos 🗒️
Make it actually work lmfao

## Requirements ❗
1. Git.
2. Python 3.12+
3. pip.
4. Nerd Font (Required for the icons)

<hr>

## Usage 💻

1. Clone the repository:
    ```
    git clone https://github.com/MikoTheFemboy/PiPhone-UI.git
    cd PiPhone-UI
    ```

2. Install dependencies:
    `pip install -r requirements.txt`<br>
    If that doesn't work, then you might need to create a virtual environment.
    `python -m venv .venv`<br>
    Then activate it and install the requirements.txt.
    If you're on Linux/MacOS (Bash/Zsh):
    ```
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

    If you're on Windows (CMD):
    ```
    .venv/Scripts/activate.bat
    pip install -r requirements.txt
    ```

    If you're on Windows (Powershell):
    ```
    .venv/Scripts/Activate.ps1
    pip install -r requirements.txt
    ```

3. Run the program.
`python main.py`
<br>

4. When you're done, deactivate the venv using:
`deactivate`

<hr>

*Ps: I know the markdown is still bad, am sorry.
Sincerely, みこは男の娘*