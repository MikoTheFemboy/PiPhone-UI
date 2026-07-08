from datetime import datetime

def get_datetime():
    now = datetime.now()
    return (
        now.strftime("%H:%M:%S"),
        now.strftime("%d/%m/%Y"),
        now.strftime("Hello PiPhone!\nToday is: %A")
    )