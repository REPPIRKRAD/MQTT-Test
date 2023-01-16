import paho.mqtt.client as mqtt
import json

#-------------------------------------------------------------------------#

host  = 'test.mosquitto.org'
port = 1883
group = 'calculus2'
yourname = 'Apichai'
topic = group + '/' + yourname
username = ''
password = ''

#--------------------------------------------------------------------------#

client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(host, port)

#---------------Define a data-----------------------#

data = {}
data['name'] = 'Apichai Charoenkittikhunpaisal'
data['nickname'] = 'Guy'
data['age'] = '20'
data['occupation'] = ['student']
data['com-lang'] = ['Python', 'C#']
data['table'] = 0
print('Original Input Data Type : {}'.format(type(data)))

data = json.dumps(data)
print('Converted Input Data Type : {}'.format(type(data)))

try:
    client.publish(topic = topic, payload = data, qos = 0, retain = True)
    print('Publish Success')
except:
    print('Failed')