from signalwire.voice_response import VoiceResponse, Gather
from flask import Flask, request
from signalwire.rest import Client as signalwire_client
import os
from dotenv import load_dotenv 

load_dotenv()

app = Flask(__name__)

# SignalWire credentials
account_sid = os.environ['SIGNALWIRE_PROJECT']
auth_token = os.environ['SIGNALWIRE_TOKEN']
space_url = os.environ['SIGNALWIRE_SPACE_URL']
signalwire_number = os.environ['SIGNALWIRE_NUMBER']
client = signalwire_client(account_sid, auth_token, signalwire_space_url='danielezils.signalwire.com')

@app.route('/')
def home():
    return "Daniele's IVR"

# incoming calls
@app.route('/incoming_call', methods=['POST'])
def incoming_call():
    response = VoiceResponse()

   
    with Gather(numDigits=1, action='/handle-key', method='POST') as gather:
        gather.say("Thanks for calling Daniele. Press 1 for support, Press 2 for sales.")

  
    response.append(gather) 

    return str(response)


@app.route('/handle-key', methods=['POST'])
def handle_key():
    digit_pressed = request.form['Digits']

    if digit_pressed == '1':
        response = VoiceResponse()
        response.say("You selected support. Forwarding your call to the support team.")
       

    elif digit_pressed == '2':
        response = VoiceResponse()
        response.say("You selected sales. Forwarding your call to the sales team.")
       

    else:
        response = VoiceResponse()
        response.say("Invalid option. Please try again.")
        response.redirect('/incoming_call')

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
