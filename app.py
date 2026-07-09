from textual.app import App

from screens.home import HomeScreen
from screens.settings import SettingsScreen
from screens.notes import NotesScreen

class PiPhone(App):
    CSS_PATH = "global.tcss"

    BINDINGS= [
        ("q", "quit", "Quit"),
        ("escape", "back", "Go Back")
    ]

    def on_mount(self):
        self.install_screen(HomeScreen(), "home")
        self.install_screen(SettingsScreen(), "settings")
        self.install_screen(NotesScreen(), "notes")

        self.push_screen("home")

    def action_back(self):
        self.app.pop_screen()