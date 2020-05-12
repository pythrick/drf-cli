import typer
from cookiecutter.main import cookiecutter


app = typer.Typer()
new_app = typer.Typer()
app.add_typer(new_app, name="new")


@new_app.command("project")
def new_project():
    typer.echo("Creating new project...")
    cookiecutter("cookiecutters/project")


@new_app.command("model")
def new_model():
    typer.echo("Creating new model...")
    try:
        cookiecutter("cookiecutters/model")
    except Exception as e:
        typer.echo(e)


if __name__ == "__main__":
    app()
