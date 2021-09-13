FROM debian:bullseye

RUN apt-get update && apt-get install -y python3-pip
ADD . /user_register/

RUN pip3 install -r /user_register/requirements.txt

WORKDIR /user_register/
CMD ["uvicorn", "main:app"]

