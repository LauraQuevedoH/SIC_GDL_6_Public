import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.IN)
start = 0
try:
	stop = 0
	while True:
		GPIO.output(21, False)
		time.sleep(0.5)
		
		GPIO.output(21, True)
		time.sleep(0.00001)
		GPIO.output(21, False)
		
		while GPIO.input(20) == 0:
			start = time.time()
			
		while GPIO.input(20) == 1:
			stop = time.time()
			
		time_interval = stop - start
		distance = time_interval * 17000
		distance = round(distance, 2)
		
		print(f"distance : {distance}")

except KeyboardInterrupt:
	GPIO.cleanup()
