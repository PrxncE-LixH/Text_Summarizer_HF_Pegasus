FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app   

COPY . /app

RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

CMD ["python3", "app.py"]

## create a new directory called app
## copy everything from root to app
## run the commands and run the app.py using python3