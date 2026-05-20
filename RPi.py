import RPi.GPIO as GPIO 
import tm1637 
import time 
from datetime import datetime 
 
# ===== PIN SETUP ===== 
PIR_PIN = 17 
CLK = 23 
DIO = 24 
 
# ===== GPIO SETUP ===== 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
 
# ===== DISPLAY SETUP ===== 
tm = tm1637.TM1637(clk=CLK, dio=DIO) 
tm.brightness(2) 
 
print("System Ready...") 
 
try: 
 while True: 
  pir_state = GPIO.input(PIR_PIN) 
 
  if pir_state == 1: 
   print("Motion Detected!") 
 
   now = datetime.now() 
   current_time = now.strftime("%H%M") 
 
   tm.show(current_time) 
 
   time.sleep(0.5) 
 
  else: 
   tm.write([0, 0, 0, 0]) 
 
  time.sleep(0.2) 
 
except KeyboardInterrupt: 
 GPIO.cleanup() 
 tm.clear() 
 print("Program stopped")