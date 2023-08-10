from signalwire.voice_response import VoiceResponse, Gather
from flask import Flask, request

app = Flask(__name__)

# Route to handle incoming calls
@app.route('/incoming_call', methods=['POST'])
def incoming_call():
    response = VoiceResponse()

    # Create a Gather to handle user input
    with Gather(numDigits=1, action='/handle-key', method='POST') as gather:
        gather.say("Thanks for calling Daniele. Press 1 for support, Press 2 for sales.")

    # If no input received, redirect back to the main menu
    response.redirect('/incoming_call')

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
