FROM python:3.6-slim-buster

ENV BOT_TOKEN="YOUR_TOKEN_HERE"

RUN apt-get update && \
    apt-get install -y ffmpeg git

RUN pip install python-telegram-bot \
                git+https://github.com/johnstef99/spotify-downloader.git


RUN mkdir /var/opt/spotel && \
    chown -R www-data:www-data /var/opt/spotel

USER www-data

WORKDIR /var/opt/spotel

COPY  --chown=www-data:www-data ./telegram_bot.py /var/opt/spotel

ENTRYPOINT ["python", "/var/opt/spotel/telegram_bot.py"]
