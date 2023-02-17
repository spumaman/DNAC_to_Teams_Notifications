# app.py
import json
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
#Microsoft Teams Webhook URL to the Alerts Channel
 teams_webhook = 'https://'

#Recieving the Webhook from DNAC grabbing the relevant information from the details section of the alert sent
 if request.method == 'POST':
  json_webhook = request.json

# Parse on the details section of the payload of the alert put each key\value into pre_payload, add new lines so it looks pretty on the MS Teams channel
  pre_payload = "\\\n ".join(key +': ' + value.capitalize() for key,value in json_webhook['details'].items())
# Create a payload with the JSON object "Text": and the value of the pre_payload as a string.
  payload = {"text": str(pre_payload)}
# Send the payload off to MS Teams webhook URL for it to display in your chosen channel
  response = requests.post(teams_webhook, json=payload)
# Print the payload for debugging purposes can comment out.
  print(payload)
  return "Webhook received!"
 
app.run(host='0.0.0.0', port=8000, ssl_context='adhoc')