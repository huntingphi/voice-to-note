from flask import Flask, jsonify, request
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse
from recognize_speech import fetch_and_recognize


app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({"message": "Hello World!"})
app = Flask(__name__)

@app.route('/bot-status', methods=['POST'])
def bot_status():
    incoming_msg = request.values.get('MediaUrl0', '')
    print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

@app.route('/bot-receiver', methods=['POST'])
def bot_receiver():
    incoming_msg = request.values.get('MediaUrl0', '')
    transcript = fetch_and_recognize(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    msg.body(transcript)
    responded= True
    if responded == False:
        msg.body('Sorry, Can\'t help with that!')
    return str(resp)

if __name__ == '__main__':
 app.run()
