import os
import yaml
import shutil


ROOT_DIR = os.path.dirname(os.getcwd())


def load_settings():
    settings_file_path = os.path.join(ROOT_DIR, "settings.yaml")
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
    temp_dir = os.getcwd()
    os.chdir("..")
    shutil.rmtree(temp_dir)


def add_model_import():
    settings = load_settings()
    init_file_path = os.path.join(
        ROOT_DIR,
        settings["default"]["module_name"],
        "{{cookiecutter.app_name}}",
        "models",
        "__init__.py"
    )
    with open(init_file_path, "a+") as init_file:
        init_file.write("from .{{cookiecutter.name}} import {{cookiecutter.class_name}}\n")


if __name__ == '__main__':
    move_model_file()
    delete_model_temp_dir()
    add_model_import()
