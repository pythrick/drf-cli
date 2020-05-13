import os
import yaml


ROOT_DIR = os.path.dirname(os.getcwd())


def load_settings():
    settings_file_path = os.path.join(ROOT_DIR, "settings.yaml")
    print(settings_file_path)
    with open(settings_file_path) as settings_file:
        return yaml.load(settings_file, Loader=yaml.FullLoader)


def move_model_file():
    settings = load_settings()
    source = os.path.join(
        ROOT_DIR,
        "{{cookiecutter.name}}/{{cookiecutter.name}}.py"
    )
    destination = os.path.join(
        ROOT_DIR,
        settings["default"]["module_name"],
        "{{cookiecutter.app_name}}",
        "models",
        "{{cookiecutter.name}}.py"
    )
    os.rename(source, destination)


def delete_model_temp_dir():
    ...


if __name__ == '__main__':
    move_model_file()
