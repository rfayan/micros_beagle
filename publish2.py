import paho.mqtt.client as mqtt #import the client1
import time
import datetime
import sys

if length(sys.argv) < 3:
    print("ERRO: python publish.py [evento] [placa]")
    sys.exit(1)
    
evento = sys.argv[1]
placa = sys.argv[2]

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
#    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

f=open("carro.jpeg", "rb")
fileContent = f.read()
byteArr = bytearray(fileContent)

client.connect("localhost", 8187, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()

while True:
    input("Aperte alguma tecla para enviar a foto")
    client.publish("beagle", byteArr, 0)
