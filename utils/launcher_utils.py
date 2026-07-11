from subprocess import run

def launch(app, command:list[str]) -> None:
    with app.suspend():
        run(command)