import requests as re
from time import sleep
import random


# value1 = re.get('http://127.0.0.1:8000/sen_update?code=1234')
# print(value1.text)


# value1 = re.get('http://127.0.0.1:8000/sen_update?code=1234&id=1&sensor=sensor1&value=33')
# print(value1.text)

print()
print()
print("--------------------------------------------------")
sleep(1)
print("Sending  Sensor Values .... Webserver http://192.168.1.8")
sleep(1)
print("--------------------------------------------------")
value = ["10","20","30","40","50","60","70","80","90","100"]
while True:
    a = random.randint(0,9)
    v1 = value[a]
    value1 = re.get('http://127.0.0.1:8000/sen_update?code=1234&id=1&sensor=sensor1&value={}'.format(v1))
    print("Sending Sensor1 value {} .... ".format(v1))
    sleep(1)

    a = random.randint(0,9)
    v2 = value[a]
    value2 = re.get('http://127.0.0.1:8000/sen_update?code=1234&id=2&sensor=sensor2&value={}'.format(v2))
    print("Sending Sensor2 value {} .... ".format(v2))
    sleep(1)

    a = random.randint(0,9)
    v3 = value[a]
    value3 = re.get('http://127.0.0.1:8000/sen_update?code=1234&id=3&sensor=sensor3&value={}'.format(v3))
    print("Sending Sensor3 value {} .... ".format(v3))
    sleep(1)

    a = random.randint(0,9)
    v4 = value[a]
    value4 = re.get('http://127.0.0.1:8000/sen_update?code=1234&id=4&sensor=sensor4&value={}'.format(v4))
    print("Sending Sensor4 value {} .... ".format(v4))
    sleep(1)
    print("--------------------------------------------------")
    sleep(3)

    
    


    # value3 = re.get('http://127.0.0.1:8000/sen_update?code=1234&id=3&sensor=sensor1&value=33')
    # sleep(1)
    # print("Sending Sensor3 value .... ")


    # value4 = re.get('http://127.0.0.1:8000/sen_update?code=1234&id=4&sensor=sensor1&value=33')
    # sleep(1)
    # print("Sending Sensor4 value .... ")

    

    
