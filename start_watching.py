from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
import time
import sys

headers={
	'Client-ID':'mq8x7uz3vxy8c4e1xafyyjz7mqmnps'
}

def findNewStream():
	r = requests.get('https://api.twitch.tv/helix/streams?game_id=516575', headers=headers)
	streamer_info = r.json()['data'][0]
	user_name = streamer_info['user_name']
	user_id = streamer_info['user_id']
	return user_id, user_name, 'https://www.twitch.tv/{}'.format(user_name)

def checkStreamUp(user_id):
	r = requests.get('https://api.twitch.tv/helix/streams?game_id=516575&user_id={}'.format(user_id), headers=headers)
	return r.json()['data'] != []


if __name__ == "__main__":
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--mute-audio")
	d = webdriver.Chrome('./chromedriver', chrome_options=chrome_options) 
	d.get('https://www.twitch.tv/login')
	try:
		print('Enter your login information')
		while d.current_url != 'https://www.twitch.tv/?no-reload=true':
			pass
		user_id, user_name, url = findNewStream()
		d.get(url)
		print('Watching: {}!'.format(user_name))
	except:
		d.close()
	minutes = 1
	while True:
		for i in range(60):
			try:
				time.sleep(1)
			except KeyboardInterrupt:
				d.close()
				print('Done watching!')
				sys.exit()
		if not checkStreamUp(user_id):
			user_id, user_name, url = findNewStream()
			d.get(url)
			print('Watching: {}!'.format(user_name))
			minutes = 1
		else:
			if minutes == 1:
				print('Watched {} for {} minute!'.format(user_name, minutes))
			else:
				print('Watched {} for {} minutes!'.format(user_name, minutes))
			minutes += 1



