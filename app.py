from signalwire.voice_response import VoiceResponse, Gather
from flask import Flask, request
from signalwire.rest import Client as SignalWireClient 

app = Flask(__name__)

# SignalWire credentials
account_sid = '1af50fb5-cbf5-4dda-8427-9958ea296ff2'
auth_token = 'PTb76b85a669f0cfd94a0f23a7f056f347d55a359cad6ba69c'
space_url = 'danielezils.signalwire.com'
client = SignalWireClient(account_sid, auth_token, space_url=space_url)

@app.route('/')
def home():
    return "Daniele's IVR"

# Route to handle incoming calls
@app.route('/incoming_call', methods=['POST'])
def incoming_call():
    response = VoiceResponse()

    # Create a Gather to handle user input
    with Gather(numDigits=1, action='/handle-key', method='POST') as gather:
        gather.say("Thanks for calling Daniele. Press 1 for support, Press 2 for sales.")

    # If no input received, redirect back to the main menu
    response.append(gather) 

    return str(response)

# Route to handle user input
@app.route('/handle-key', methods=['POST'])
def handle_key():
    digit_pressed = request.form['Digits']

    if digit_pressed == '1':
        # Handle support option (you can add your logic here)
        response = VoiceResponse()
        response.say("You selected support. Forwarding your call to the support team.")
        # Add further actions or redirects as needed

    elif digit_pressed == '2':
        # Handle sales option (you can add your logic here)
        response = VoiceResponse()
        response.say("You selected sales. Forwarding your call to the sales team.")
        # Add further actions or redirects as needed

    else:
        # Invalid option
        response = VoiceResponse()
        response.say("Invalid option. Please try again.")
        response.redirect('/incoming_call')

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
