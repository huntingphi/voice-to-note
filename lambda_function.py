from flask import Flask, jsonify, request
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse
from recognize_speech import recognize
from fetch_vn import fetch


app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({"message": "Hello World!"})
app = Flask(__name__)

@app.route('/bot-status', methods=['POST'])
def bot_status():
    incoming_msg = request.values.get('Body', '')
    print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

@app.route('/bot-receiver', methods=['POST'])
def bot_receiver():
    responded = False
    resp = MessagingResponse()
    msg = resp.message()
    try:
        incoming_msg = request.values.get('MediaUrl0', '')
        path_to_audio = fetch(incoming_msg)
        transcript = recognize(path_to_audio)
        msg.body(transcript)
        responded= True
    except:
        msg.body('Sorry, Can\'t help with that!')
    return str(resp)

if __name__ == '__main__':
 app.run()
