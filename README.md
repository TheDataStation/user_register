# user_register

This component handles user registration in the context of Data Stations.

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
user model [source file](/models/users.py)

## Software Stack

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
x
