# DRF CLI: Project Management for Django + Django Rest Framework
DRF CLI helps you create and manage Django + DRF 
projects, ensuring you have the best development tools in 
a fast way. 
 

## Install
Assuming you have already installed Python 3.8+...
Install the DRF CLI tool.
```shell script
$ pip install drf-cli
```

## Create project
Create a new Django + DRF project.
```shell script
$ drf new project
```


## Create backend APIs through models
Executing the following command it will generate a new Model
(and the full combination of Model Serializer, Model ViewSet,
Route, Migration, etc...)
```shell script
$ drf new model
```

The generator guides you through creating your resource.
Enter the values. To accept the default, just press Enter.
```shell script
[?] Enter the model name: pizza
[?] Custom plural form: pizzas
Let's add some model properties now.
```

Define a property for model
```shell script
Enter an empty property name when done.
[?] Property name: size
```

Choose the property type:
```shell script
[?] Property type:
* [1] string
  [2] integer
  [3] boolean
  [4] decimal
  [5] float
  [6] date
  [7] datetime
```

Make the property required or not:
```shell script
[?] Required? (y/N) y
```

Repeated these steps until define all model properties 
you need.

Press Enter when prompted for a property name to finish 
up and create the resource.

## Run the project:
Run as you would any Django application.
```shell script
$ python manage.py runserver
```

## Explore your REST API
Load http://0.0.0.0:8000/api to see the built-in API Explorer.

## Development tools included
This tool follows the best development practices included in [12-factor app](https://12factor.net/) and in [this blog post](https://sourcery.ai/blog/python-best-practices/).
- Dependencies Management:
  - [Poetry](https://python-poetry.org/)
- Project Configurations
  - [Dynaconf](https://dynaconf.readthedocs.io/en/latest/)
- Code Formating
  - [Black](https://black.readthedocs.io/en/stable/)
  - [Isort](https://github.com/timothycrosley/isort)
- Style Enforcement
  - [Flake8](https://flake8.pycqa.org/en/latest/)
- Static Typing
  - [Mypy](http://mypy-lang.org/)
- Testing and Coverage
  - [Pytest](https://docs.pytest.org/en/latest/)
  - [Pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)
- Git hooks   
  - [Pre-commit](https://pre-commit.com/)
- Conteiners Management
  - [Docker](https://www.docker.com/why-docker)
  - [Docker-Compose](https://docs.docker.com/compose/)
- Authentication
  - [JWT](https://jwt.io)
  - [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
