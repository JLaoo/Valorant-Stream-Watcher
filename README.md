# Valorant Stream Watcher

## Description:

Watches Valorant streams for you so you can get a key drop lol.

## Instructions

1) pip install -r requirements.txt
2) Setup Selenium (see below)
3) python3 start_watching.py
4) Enter your login and 2FA code

## Selenium setup:

In order for the driver to work, go to the ChromeDriver downloads page here: https://sites.google.com/a/chromium.org/chromedriver/home and download the correct driver for your OS and version of Chrome. Other browsers may work, but will require modifications to the code and also have not been tested. Place the driver into the same directory as the script. There is currently a MacOS ChromeDriver for Chrome version 77 in the directory that can be replaced.

## Features

- Automatic stream switching to another streamer with drops enabled when a streamer goes offline.
- Automatic browser muting so you don't need to hear the streamer in the background.
- Console logs how long you've been watching the current streamer.
- Selenium browser automatically exits upon keyboard interrupt in console.
