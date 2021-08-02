# user_register
The user register component of Data Station

## User Model
```python
id: int
user_name: str
first_name: str
last_name: str
password: str
email_address: str
institution: str
country: str
```

## Technique Stack

Language -> Python3.8

Rest API -> [FastAPI](https://fastapi.tiangolo.com/)

Storage -> SQLite

ORM -> SQLalchemy

Deploy -> [Docker Compose](https://docs.docker.com/compose/) [todo]

## Quick Start
```shell
# install required packages
pip install -r requirements.txt

# start fastAPI server
uvicorn main:app --reload
```

Then, open http://127.0.0.1:8000/docs and try APIs interactively.