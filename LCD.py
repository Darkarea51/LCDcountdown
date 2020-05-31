import os
import json
import datetime
import requests
import time
import Adafruit_CharLCD as LCD


lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

lcd.message('countdown is Booting up...')
time.sleep(5.0)

Upcoming = requests.get("https://api.spacexdata.com/v3/launches/upcoming").text
json_Upcoming=json.loads(Upcoming)

now = datetime.datetime.now()

liftoff = str(now)
countdowntimer = str(json_Upcoming[0]["launch_date_local"])
s = countdowntimer.split('T')
a = s[0].split('-')
t = s[1].split('-')
u = t[0].split(',')
v = u[0].split(':')
launch = a + v
launchtime = []
for e in launch:
    launchtime.append(int (e))
    
launchtime[3]=launchtime[3]-4   
launchdatetime = datetime.datetime(*launchtime)
looplaunch = launchdatetime-now

print (str(looplaunch) + " Until Launch!")

lcd.message(str(looplaunch) + " Until Launch!")


