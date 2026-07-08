from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Label, Button, Digits

from utils.datetime_utils import (
    get_datetime
)

class HomeScreen(Screen):
    CSS = """
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
    """

    def compose(self) -> ComposeResult:
        time, date, day = get_datetime()

        with Vertical(id="main-wrapper"):

            # The Header, essentially.    
            with Horizontal():
                yield Label(date, id="date")
                yield Label(day, id="day")
            yield Digits(time, id="clock")

            # The middle parts with button.
            with Horizontal():
                yield Button("󰖟", id="button_browser")
                yield Button("󰆍", id="button_console")

            with Horizontal():
                yield Button("", id="button_message")
                yield Button("", id="button_setting")

            # The exit button.
            with Horizontal():
                yield Button("󰈆", id="button_exit", variant="error")

    def on_mount(self) -> None:
        self.clock = self.query_one("#clock", Digits)
        self.date = self.query_one("#date", Label)
        self.day = self.query_one("#day", Label)

        self.refresh_datetime()
        self.set_interval(1.0, self.refresh_datetime)

        print("HomeScreen Ready!")

    def refresh_datetime(self):
        time, date, day = get_datetime()

        self.clock.update(time)
        self.date.update(date)
        self.day.update(day)