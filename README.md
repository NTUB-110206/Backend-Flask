# backend-flask

## env
#### You must fill the following variables in your .env file:
- SECRET_KEY
- SQLALCHEMY_DATABASE_URI
- DEBUG ( option )
- SQLALCHEMY_TRACK_MODIFICATIONS ( option )

## How to use
<details>
<summary><b>Windows</b></summary>

```
# init virtual environment
python -m venv backend-env

# activate virtual environment
backend-env\Scripts\activate.bat

# requirements package
python -m pip install --upgrade pip
pip install -r requirements.txt

# Start ( choose one )
py -3 runserver.py
python runserver.py
```

</details>

<details>
<summary><b>macOS</b></summary>

```
# init virtual environment
python3 -m venv backend-env

# activate virtual environment
source backend-env/bin/activate

# requirements package
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
pip3.9 install psycopg2-binary --force-reinstall --no-cache-dir

# Start
python3 runserver.py
```

</details>