import RPi.GPIO as GPIO
from time import strftime
import time
import pygame
import sys
import pyttsx
import forecastio



#User inputs time HH:MM AM/PM
quest = raw_input("What time would you like to wake up? ")


def audio():
	pygame.mixer.pre_init(44100, -16, 2, 2048)
	pygame.init()
	music = pygame.mixer.Sound("/home/dan/Documents/Python/Alarm/alarm.ogg")
	music.set_volume(.10);
	music.play()


def weather():
	engine = pyttsx.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate-75)
	api_key = "" //API key for text to speech
	lat = 38.952893
	lng = -90.222545
	forecast = forecastio.load_forecast(api_key, lat, lng)
	current = forecast.currently()
	engine.say("The weather is %s" % current.summary)
	time.sleep(1)
	engine.say("The temperature is %d degrees Fahrenheit" % current.temperature) 
	time.sleep(1)
	engine.runAndWait()
	sys.exit()
	

while True:
	now_strf = strftime("%I:%M %p")
	sec_strf = strftime("%I:%M:%S %p")
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	input_state = GPIO.input(23)
	if quest == now_strf:
		audio()
	elif input_state == False:
		weather()
	else:
		print sec_strf
		time.sleep(1)




GPIO.cleanup()
	
	

		





