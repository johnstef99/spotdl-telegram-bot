# Telegram spotify-downloader bot

You can setup this bot for you and your friends to download music to your
phone. What's great with downloading music with this bot is that you get
**Artists Info** and **Album Thumbnail** embedded into the mp3 file.

# How it works

The bot uses [spotdl](https://github.com/johnstef99/spotify-downloader) to
download the music. Also you **need to have ffmpeg** installed so it can
convert it to mp3 and apply metadata. After the file is sent to telegram the
bot deletes the local files from the machine.

# Requirements

- python 3.6
- [spotdl v2](https://github.com/johnstef99/spotify-downloader.git)

# Set-up

- Create a new python environment (**recomended**) and source into it
  ```sh
  python3.6 -m venv spotel_env
  source spotel_env/bin/activate
  ```
- Install [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
  with `pip install python-telegram-bot`
- Install [spotdl](https://github.com/johnstef99/spotify-downloader.git) `pip install git+https://github.com/johnstef99/spotify-downloader.git`
- Make sure you have ffmpeg install (not a python package)

# Config

Clone this repo somewhere on your machine and edit the `telegram_bot.py` file,
add your **token**, and then you can run `python telegram_bot.py` (**make
sure you source to you virtual environment where spotdl and telegram-bot
is installed**). Now try sending a message to your bot (see the available
commands)

# Commands

- **/song** _song's title/link_ (downloads a single song)

# Extra Info

> - The bot can also download songs from youtube link but it's better to send
>   spotify link or the song title so you get the metadata.
> - A good app for Android users is
>   [Musicolet](https://play.google.com/store/apps/details?id=in.krosbits.musicolet)

```

```
