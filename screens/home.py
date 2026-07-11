import subprocess

from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Label, Button, Digits

from utils.datetime_utils import (
    get_datetime
)

from utils.motd_utils import(
    get_motd
)

from utils.launcher_utils import (
    launch
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
        }

        #motd {
            margin-bottom: 2;
        }
    """

    def compose(self) -> ComposeResult:
        time, date, day = get_datetime()
        motd = get_motd()

        with Vertical(id="main-wrapper"):

            # The Header, essentially.    
            with Horizontal():
                yield Label(date, id="date")
                yield Label(day, id="day")
            yield Digits(time, id="clock")

            yield Label(motd, id="motd")

            # The middle parts with button.
            with Horizontal():
                yield Button("󰖟\nBrowser", id="button_browser")
                yield Button("󰆍\nConsole", id="button_console")

            with Horizontal():
                yield Button("\nMessage", id="button_message")
                yield Button("\nSettings", id="button_settings")

            # The exit button.
            with Horizontal():
                yield Button("\nNotes", id="button_notes")
                yield Button("󰈆\nExit", id="button_exit", variant="error")

    def on_mount(self) -> None:
        self.clock = self.query_one("#clock", Digits)
        self.date = self.query_one("#date", Label)
        self.day = self.query_one("#day", Label)

        self.motd = self.query_one("#motd", Label)

        self.refresh_datetime()
        self.set_interval(1.0, self.refresh_datetime)

    def refresh_datetime(self):
        time, date, day = get_datetime()

        self.clock.update(time)
        self.date.update(date)
        self.day.update(day)

    def refresh_motd(self):
        motd = get_motd()
        self.motd.update(motd)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "button_browser":
                launch(self.app, ["w3m", "www.wikipedia.org/"])

            case "button_console":
                print("Pro-tip: Press CTRL+D to go back!") #Why the fuck aren't you printing???
                launch(self.app, ["bash"])

            case "button_settings":
                self.app.push_screen("settings")

            case "button_notes":
                self.app.push_screen("notes")
            
            case "button_exit":
                exit("See ya later!")