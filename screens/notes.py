from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Label, Button, ListView, ListItem

from services.notes import (
    list_notes,
    load_note,
    save_note
)

class NotesScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("Notes [WIP]")
        
        yield ListView(id="notes")

        yield Button("󰈆\nGo Back", id="button_back", variant="error")

    def on_mount(self):

        self.notes = list_notes()

        list_view = self.query_one("#notes", ListView)

        for note in self.notes:
            list_view.append(
                ListItem(
                    Label(note.stem)
                )
            )

    def on_list_view_selected(self, event: ListView.Selected):
        note = self.notes[event.list_view.index]
        
        text = load_note(note)

        print(text)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "button_back":
            self.app.pop_screen()