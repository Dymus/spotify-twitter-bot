from twython import Twython, TwythonError
import win32gui
import datetime, time

APP_KEY = 'hidden'
APP_SECRET = 'hidden'
OAUTH_TOKEN = 'hidden'
OAUTH_TOKEN_SECRET = 'hidden'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

pyHANDLE = win32gui.FindWindow("Chrome_WidgetWin_0", "Spotify")
old_string = win32gui.GetWindowText(pyHANDLE)

while(True):
	try:
		new_string = win32gui.GetWindowText(pyHANDLE)
		if new_string != old_string:
			if new_string == "Spotify":
				time.sleep(1.5)
				continue
			elif new_string == "":
				print("LOST CONNECTION! Spotify client has been closed.")
				quit()

			now = datetime.datetime.now()
			timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
			print("["+timestamp+"]"+new_string)

			now = datetime.datetime.now()
			timestamp = now.strftime("%Y-%m-%d %H:%M")
			if len(("["+timestamp+"]"+" Now playing: "+new_string)) > 280:
				print("Warning! Twitter's character limit breached. Skipping...\n")
				old_string = new_string
				time.sleep(1.5)
				continue

			now = datetime.datetime.now()
			timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
			print("["+timestamp+"]"+ "Tweeting...")

			now = datetime.datetime.now()
			timestamp = now.strftime("%Y-%m-%d %H:%M")
			final_string = "["+timestamp+"]"+" Now playing: "+new_string
			twitter.update_status(status=final_string)

			now = datetime.datetime.now()
			timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
			print("["+timestamp+"]"+ "Tweeting done!\n")
			time.sleep(1.5)

			old_string = new_string
		else:
			time.sleep(1.5)
	except TwythonError as e:
		print(e)