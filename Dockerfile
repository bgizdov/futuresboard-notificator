FROM python:3-slim

COPY ./ /code/

WORKDIR /code

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "send_loop.py"]
