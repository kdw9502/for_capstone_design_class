import requests
import time
import random

for i in range(10):
    value = random.randint(-100, 100)

    response = requests.get(f"https://api.thingspeak.com/update?api_key=VJQUUVRHIALEZUBV&field1={value}")
    time.sleep(16)
