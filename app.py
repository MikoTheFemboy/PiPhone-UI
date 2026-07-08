from textual.app import App
from screens.home import HomeScreen

class PiPhone(App):
    CSS_PATH = "global.tcss"

    BINDINGS= [
        ("q", "quit", "Quit")
    ]

    def on_mount(self):
        self.push_screen(HomeScreen())