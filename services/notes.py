#TODO: Make this actually function lmfao

from pathlib import Path

NOTES_DIR = Path("notes")

def list_notes():
    return sorted(NOTES_DIR.glob("*.txt"))

def load_note(path):
    return path.read_text()

def save_note(path, text):
    path.write_text(text)