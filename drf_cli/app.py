import os

import typer
from cookiecutter.main import cookiecutter

app = typer.Typer()
new_app = typer.Typer()
app.add_typer(new_app, name="new")


def get_cookiecutter_path(name: str) -> str:
    script_path = os.path.abspath(__file__)
    module_path = os.path.dirname(script_path)
    project_path = os.path.dirname(module_path)
    cookiecutters_path = os.path.join(project_path, "cookiecutters")
    return os.path.join(cookiecutters_path, name)


@new_app.command("project")
def new_project():
    typer.echo("Creating new project...")
    cookiecutter_path = get_cookiecutter_path("project")
    cookiecutter(cookiecutter_path)


@new_app.command("model")
def new_model():
    typer.echo("Creating new model...")
    try:
        cookiecutter_path = get_cookiecutter_path("model")
        cookiecutter(cookiecutter_path)
    except Exception as e:
        typer.echo(e)


if __name__ == "__main__":
    app()
