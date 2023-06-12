# [![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=841DF7&center=true&vCenter=true&width=435&lines=API+for+YaTube+project)](https://git.io/typing-svg)

## Description:

  The project is an API for the Yatube project. This interface can work with mobile apps, chatbots and frontend. 
Anonymous users receive read-only requests, except for access to subscribe content. Authenticated users can read or write, but only delete and change their own content, others content can only be read.

## Technology stack:

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
  ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

## Project file structure:

```shell
$ tree -I 'venv' -I '__pycache__' -I 'migrations'
yatube_api
    ├── api
    │   ├── __init__.py
    │   ├── apps.py
    │   ├── permissions.py
    │   ├── serializers.py
    │   ├── templates
    │   │   └── redoc.html
    │   ├── urls.py
    │   └── views.py
    ├── db.sqlite3
    ├── manage.py
    ├── posts
    │   ├── __init__.py
    │   ├── apps.py
    │   └── models.py
    ├── static
    │   └── redoc.yaml
    └── yatube_api
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

## Installation
### Step 1
Create and activate virtual environment:

```shell
python3 -m venv venv
```
* For Linux/macOs
  ```shell
  source venv/bin/activate
  ```
* For Windows
  ```shell
  .\venv\Scripts\activate
  ```
### Step 2
Install dependencies from requirements.txt :

```shell
python -m pip install --upgrade pip
pip install -r requirements.txt
```
### Step 3
Make migrations:

```shell
python3 manage.py migrate
```
### Step 4
Run project:

```shell
python manage.py runserver
```

## API Documentation

```
http://127.0.0.1:8000/redoc/
```
## Example API requests:

- Get a list of all publications. When specifying the limit and offset parameters, the output must work with pagination.

