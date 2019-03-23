from dotenv import load_dotenv
import os
import json
import urllib.request


load_dotenv()


# Get an API token using email / password.
data = {'user': {'email': 'user@user.com', 'password': 'password123'}}

# To generate the token, we POST JSON to `api/tokens`.
req = urllib.request.Request('https://my.farmbot.io/api/tokens')
req.add_header('Content-Type', 'application/json')
response = urllib.request.urlopen(req, json.dumps(data).encode('utf-8'))

# It will return a JSON object...
raw_json = response.read()
token_data = json.loads(raw_json)

# ... response_body.token.encoded is the important part- you will use this as
# an MQTT password.
the_token = token_data['token']['encoded']

print("\n\nYou will need to know your device_id to use MQTT.\n")
print("Your device id is: \n" + token_data['token']['unencoded']['bot'] + "\n")
print("The MQTT Host is: \n" + token_data['token']['unencoded']['mqtt'] + "\n")
# You can copy/paste this data and move on to `subscribe_example.py`.
print("The token is: \n" + the_token)



print(os.getenv("EMAIL"))
print(os.getenv("PASSWORD"))
