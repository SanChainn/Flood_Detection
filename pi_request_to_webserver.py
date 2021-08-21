import requests as re
from time import sleep


print()
print()
print("--------------------------------------------------")
#sleep(1)
print("Requesting Sensor Values From WebServer.... http://192.168.1.8")
#sleep(1)
print("--------------------------------------------------")
#sleep(1)
while True:
    value1 = re.get('http://127.0.0.1:8000/value1')
    sleep(1)
    print("Get Sensor Value 1 :",value1.text)


    value2 = re.get('http://127.0.0.1:8000/value2')
    sleep(1)
    print("Get Sensor Value 2 :",value2.text)


    value3 = re.get('http://127.0.0.1:8000/value3')
    sleep(1)
    print("Get Sensor Value 3 :",value3.text)


    value4 = re.get('http://127.0.0.1:8000/value4')
    sleep(1)
    print("Get Sensor Value 4 :",value4.text)
    print("--------------------------------------------------")
    sleep(1)
    
