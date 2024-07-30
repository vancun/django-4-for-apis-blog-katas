# Setup Django Project

```bash
mkdir blogapi
cd blogapi
```

Create `.gitignore`

```
.venv*/
.dev*/
.vscode/
```

## Virtual Environment

```bash
# Create virtual environment with Python 3.10
py -3.10 -m venv .venv310
# Activate virtual environment
.venv310\Scripts\activate.bat
# Upgrade pip
python -m pip install --upgrade pip
```

In Visual Code select Python Interpreter. Opening new terminal will activate the virtual environment.

## Dependencies

Create `requirements.txt` to define package dependencies.

```requirements
django
djangorestframework
pytest
pytest-cov
pytest-django
python-dotenv
```

Intall the required packages.

```bash
pip install -r requirements.txt
```


## Create Django Project

```bash
django-admin startproject django_project .
python manage.py migrate
python manage.py runserver
```

Open the browser at http://127.0.0.1:8000/ to inspect the result.



