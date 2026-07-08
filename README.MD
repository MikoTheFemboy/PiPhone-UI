# WORK IN PROGRESS. THIS UI CURRENTLY ONLY LOOKS PRETTY, NOT FUNCTIONAL.

## PiPhone UI (Might change the name idk)

This is a terminal-only User Interface made using Textual for a future project for a Raspberry Pi Phone.

*How to use*

1. Clone the repository.
    ```
    git clone https://github.com/MikoTheFemboy/PiPhone-UI.git
    cd PiPhone-UI
    ```

2. Install dependencies.
    `pip install -r requirements.txt`<br>
    If that doesn't work, then you might need to create a virtual environment.
    `python -m venv .venv`<br>
    Then activate it and install the requirements.txt.
    If you're on Linux/MacOS (Bash/Zsh)
    ```
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

    If you're on Windows (CMD)
    ```
    .venv/Scripts/activate.bat
    pip install -r requirements.txt
    ```

    If you're on Windows (Powershell)
    ```
    .venv/Scripts/Activate.ps1
    pip install -r requirements.txt
    ```

13. Run the program.
`python main.py`

*Explanation*

I'm currently planning to make a phone using a Raspberry Pi Zero W. Since the SBC isn't powerful (at all), I'll be using this terminal-only UI instead of a heavy Desktop Environment.

Here are (almost) all the hardware that I'll be using for this project, if you want to follow.
*The main stuff*
1. Raspberry Pi Zero W.
2. ILI9341
3. 3.7V 4000mAh LiPo
4. MT3608
5. TP4056
6. Either cardboard or a 3D printed case.
*Misc*
7. USB Hub.
8. Foldable keyboard.

*ps sorry for the bad markdown, sincerely -みこ*