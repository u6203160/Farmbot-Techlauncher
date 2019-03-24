import paho.mqtt.client as mqtt
import api_token_gen.token_data as token_data
# This information was created using `token_generation_example.py`.
my_device_id = token_data['token']['unencoded']['bot']
# This information was created using `token_generation_example.py`.
my_token = token_data['token']['encoded']
# I *think* this gets the server right
my_server = token_data['token']['unencoded']['mqtt']

# This is our custom on_connect fuction which is called by the server when
# we connect to it.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # "bot/device_name/status" will broadcast the FarmBot "state tree"- it is a
    # data structure representing _all_ bot state, such as pin status, lock
    # lock status, installed farmware, etc.
    client.subscribe("bot/" + my_device_id + "/status")

    # "bot/device_name/logs" shows the messages typically seen in the status bar
    # of the web app. Like everything else on MQTT, it is encoded as JSON.
    client.subscribe("bot/" + my_device_id + "/logs")

    # "bot/device_name/from_clients" allows you to listen to your echo.
    # All incoming commands to the device will show up here.
    # We use a special form of JSON called "CeleryScript". Read more here:
    # https://github.com/FarmBot/farmbot-js/wiki/Celery-Script
    # https://github.com/FarmBot/farmbot-js/wiki/Using-Raw-MQTT
    client.subscribe("bot/" + my_device_id + "/from_clients")

    # "bot/device_18/from_device" contains all of FarmBot's responses to
    # commands. It's JSON, like everything else.
    client.subscribe("bot/" + my_device_id + "/from_device")

# This is our custom on_message fuction which is called by the server when
# it wants to send a message.
def on_message(client, userdata, msg):
    # Print stuff to the screen.
    # EXERCISE: Try running this script and pushing buttons on the Web App.
    #           You shoud see activity print to the screen.
    print("Incoming MQTT messages: ")
    print(msg.topic + " " + str(msg.payload))


# Connect to the broker...
client = mqtt.Client("name_set_by_user")
# ...using credentials from `token_generation_example.py`
client.username_pw_set(my_device_id, my_token)

# Attach event handlers:
client.on_connect = on_connect
client.on_message = on_message

# Finally, connect to the server:
client.connect(my_server, port=1883, keepalive=60)

client.loop_forever()
