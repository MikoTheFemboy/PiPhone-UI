from datetime import datetime
from textual.containers import Horizontal, Vertical
from textual.app import App, ComposeResult
from textual.widgets import *

class PiPhone(App):
    """PiPhone UI"""

    CSS = """
        Screen {
            align: center top;
        }

        #main-wrapper {
            align: center top;
            width: auto;
            height: auto;
            padding-top: 2;
        }

        #date {
            width: auto;
            border: white;
        }

        Digits {
            border: white;
            width: auto;
            margin-bottom: 2;
        }

        Horizontal {
            width: auto;
            height: auto;
        }

        Button{
            margin: 1 1;
        }
    """

    BINDINGS = [
        ("q", "quit", "Quit UI")
    ]

    def compose(self) -> ComposeResult:
        with Vertical(id="main-wrapper"):

            # The Header, essentially.    
            with Horizontal():
                yield Label(self.get_current_date_string(), id="date")
                yield Label(self.get_current_day_string(), id="day")
            yield Digits("", id="clock")

            # The middle parts with button.
            with Horizontal():
                yield Button("󰖟", id="button_browser")
                yield Button("󰆍", id="button_console")

            with Horizontal():
                yield Button("", id="button_message")
                yield Button("", id="button_setting")

            # The exit button.
            yield Button("󰈆", id="button_exit", variant="error")

        # TODO: Remove this once ready to use.
        yield Footer()

    # TODO: Put these in a different file. Make it less cluttered.
    def on_ready(self) -> None:
        self.update_clock()
        self.set_interval(1.0, self.update_clock)

    def update_clock(self) -> None:
        now = datetime.now().time()
        self.query_one("#clock", Digits).update(f"{now:%T}")

    def get_current_date_string(self) -> None:
        return datetime.now().strftime("%d/%m/%Y")
    
    def get_current_day_string(self) -> None:
        return datetime.now().strftime("Hello PiPhone!\nToday is: %A")
    
    def update_date(self) -> None:
        self.query_one("#date", Label).update(self.get_current_date_string())

    def update_day(self) -> None:
        self.query_one("#day", Label).update(self.get_current_day_string())    

if __name__ == "__main__":
    app = PiPhone()
    app.run()