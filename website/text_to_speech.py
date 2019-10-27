#!/usr/bin/env python

import requests
import xmltodict
from google.cloud import texttospeech
import os
import socket


def play_text_to_speech(text):

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "HackGT19-d602e3624538.json"

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text='dot ' + text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    with open('assets/output.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

    url = 'http://192.168.1.174:8090/'
    host_name = socket.gethostname() 
    my_ip = "http://" + socket.gethostbyname(host_name) + ":8000/"

    req = "<play_info><app_key>od7y58yQRxoiA2J3IQdi53OAlGuNFvuk</app_key><url>" + my_ip + "assets/output.mp3</url><volume>60</volume><service>service text</service><reason>reason text</reason><message>message text</message></play_info>"
    x = requests.post(url + 'speaker', req)


if __name__ == '__main__':
    play_text_to_speech("  I love chaitya b shah")
