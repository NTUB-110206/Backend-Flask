# backend-flask

### env
#### You must fill the following variables in your app/setting.py file:
- SECRET_KEY
- SQLALCHEMY_DATABASE_URI

#### init virtual environment
- for Windows
```
python -m venv backend-env
python -m pip install --upgrade pip
```
- for macOS
```
python -m venv backend-env
python3 -m pip install --upgrade pip 
```

#### activate virtual environment
- for Windows
```
backend-env\Scripts\activate.bat
```
- for macOS
```
source backend-env/bin/activate
```

#### requirements package
- for Windows
```
pip install -r requirements.txt
```
- for macOS
```
pip3 install -r requirements.txt
pip3.9 install psycopg2-binary --force-reinstall --no-cache-dir
```

### Start
- for Windows ( choose one )
```
py -3 runserver.py
python runserver.py
```
- for macOS
```
python3 runserver.py
```
