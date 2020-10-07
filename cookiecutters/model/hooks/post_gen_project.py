import os
import shutil
import sys

import yaml

ROOT_DIR = os.path.dirname(os.getcwd())


def load_settings():
    settings_file_path = os.path.join(ROOT_DIR, "settings.yaml")
    with open(settings_file_path) as settings_file:
        return yaml.load(settings_file, Loader=yaml.FullLoader)


def move_model_file():
    settings = load_settings()
    source = os.path.join(ROOT_DIR, "{{cookiecutter.name}}/{{cookiecutter.name}}.py")
    destination = os.path.join(
        ROOT_DIR,
        settings["default"]["module_name"],
        "{{cookiecutter.app_name}}",
        "models",
        "{{cookiecutter.name}}.py",
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
        "__init__.py",
    )
    with open(init_file_path, "a+") as init_file:
        init_file.write(
            "from .{{cookiecutter.name}} import {{cookiecutter.class_name}}\n"
        )


def add_model_properties():
    print("Enter an empty property name when done.")
    properties = []
    while True:
        # TODO: Validate property_name
        property_name = input("Property name: ").lower()
        if not property_name:
            break
        property_verbose = property_name.title()
        property_types = {
            "string": f"CharField(verbose_name=_('{property_verbose}'), max_length=200)",
            "integer": f"IntegerField(verbose_name=_('{property_verbose}'), )",
            "decimal": f"DecimalField(verbose_name=_('{property_verbose}'), max_digits=9, decimal_places=2)",
            "boolean": f"BooleanField(verbose_name=_('{property_verbose}'), )",
            "date": f"DateField(verbose_name=_('{property_verbose}'), )",
            "datetime": f"DateTimeField(verbose_name=_('{property_verbose}'), )",
        }
        types = ", ".join(property_types.keys())
        property_chosen = input(f"Property type: [{types}]")
        if property_chosen not in property_types:
            print("Invalid property type.")
            sys.exit(-1)
        property_type = property_types[property_chosen]
        properties.append({"name": property_name, "type": property_type})

    write_properties_to_file(properties)


def write_properties_to_file(properties: list):
    settings = load_settings()
    model_file_path = os.path.join(
        ROOT_DIR,
        settings["default"]["module_name"],
        "{{cookiecutter.app_name}}",
        "models",
        "{{cookiecutter.name}}.py",
    )
    with open(model_file_path, "a+") as model_file:
        model_file.write("\n")
        for p in properties:
            model_file.write(f"    {p['name']} = models.{p['type']}\n")


if __name__ == "__main__":
    move_model_file()
    delete_model_temp_dir()
    add_model_import()
    print("Let's add some {{cookiecutter.name}} properties now.")
    add_model_properties()
