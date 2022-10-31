FROM python:3.7.15

WORKDIR /app

ADD . /app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install Flask
RUN pip install flask_cors
RUN pip install line-bot-sdk
RUN pip install requests-oauthlib

CMD ["python3", "app.py"]
