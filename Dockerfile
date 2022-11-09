FROM python:3.7.15

WORKDIR /app

ADD . /app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install Flask
RUN pip install flask_cors
RUN pip install line-bot-sdk
RUN pip install requests-oauthlib
RUN pip install SQLAlchemy
RUN pip install Flask-Login
RUN pip install Flask-WTF
RUN pip install selenium
RUN pip install beautifulsoup4
RUN apt-get install dnf
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN apt update
RUN apt install google-chrome-stable -y
RUN wget https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d /usr/bin/

CMD ["python3", "app.py"] 
