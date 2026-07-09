from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Label, Button, Digits

class NotesScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("Notes [WIP]")
        yield Button("󰈆", id="button_back", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "button_back":
            self.app.pop_screen()