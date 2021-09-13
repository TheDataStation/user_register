FROM debian:bullseye

RUN apt-get update && apt-get install -y python3-pip

# for testing:
RUN apt-get update && apt-get install -y wget

ADD . /user_register/

RUN pip3 install -r /user_register/requirements.txt

WORKDIR /user_register/
CMD ["uvicorn", "--host", "0.0.0.0", "main:app"]

