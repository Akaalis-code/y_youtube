################################ Summary when I come back ##

    # pyttsx3 is cutiing off the last word 

    # speech_recognition is also having an issue  like below error messages
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.surround71
        # ALSA lib setup.c:547:(add_elem) Cannot obtain info for CTL elem (MIXER,'IEC958 Playback Default',0,0,0): No such file or directory
        # ALSA lib setup.c:547:(add_elem) Cannot obtain info for CTL elem (MIXER,'IEC958 Playback Default',0,0,0): No such file or directory
        # ALSA lib setup.c:547:(add_elem) Cannot obtain info for CTL elem (MIXER,'IEC958 Playback Default',0,0,0): No such file or directory
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
        # Cannot connect to server socket err = No such file or directory
        # Cannot connect to server request channel
    
    # Trying OPENAI s whisper














import whisper
import pyaudio
import numpy as np

# Load the Whisper model
model = whisper.load_model("base")

# PyAudio parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open a stream to read from microphone
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Listening...")

try:
    while True:
        frames = []
        for _ in range(0, int(RATE / CHUNK * 5)):  # Record for 5 seconds
            data = stream.read(CHUNK)
            frames.append(np.frombuffer(data, dtype=np.int16))
        
        audio_data = np.hstack(frames)
        
        # Perform speech recognition
        result = model.transcribe(audio_data, fp16=False)
        print("Transcript:", result["text"])

except KeyboardInterrupt:
    print("Stopped listening.")

finally:
    stream.stop_stream()
    stream.close()
    p.terminate()



# from ollama import chat
# from ollama import ChatResponse

# import time


# import pyttsx3
# var_mouth = pyttsx3.init()
# var_mouth.setProperty('rate' , 120)
# var_mouth.say(" I am working properly and everything is good  ")
# var_mouth.runAndWait()

# time.sleep(5) # Wait for 1 second
# var_mouth.stop()


# import pyttsx3
 
# speaker = pyttsx3.init (debug=True)
# voices = speaker.getProperty('voices')
# speaker.setProperty('voice', 'english+f1')
# #speaker.setProperty('voice',voices[0].id)
# speaker.setProperty ('rate', 120)
# speaker.say ("I am working properly and everything is good in the situation very good")
# speaker.runAndWait ()
# speaker.stop()



# voices = var_mouth.getProperty('voices')
# for index, voice in enumerate(voices): 
#     #if 'english' in voice.name.lower():
#     print(f"Voice {index}: {voice.name}, ID: {voice.id}")
#     var_mouth.setProperty('voice', voice.id)
#     var_mouth.say(" Hello everyone")
#     var_mouth.runAndWait()


# def mth_ask_for_response(para_question):
#     response: ChatResponse = chat(model='llama3.2', messages=[
#                                                                 {
#                                                                     'role': 'user',
#                                                                     'content': 'In short , '+str(para_question),
#                                                                 },
#                                                             ]
#                                 )
#     return response


# import speech_recognition
# var_ear = speech_recognition.Recognizer()
# with speech_recognition.Microphone() as var_mic: 
#     #var_ear.adjust_for_ambient_noise(var_mic,duration = 0.2)
#     audio_data = var_ear.listen(var_mic) 
#     print("Recognizing...") 
#     try: 
#         text = var_ear.recognize_google(audio_data) 
#         print(f"Recognized text: {text}") 
#     except: 
#         print(f" error; {e}")



# for i in range(5):
#     var_user_ask = input("--->>> : ")
#     var_user_ask = 'Respond in one sentence .'+ str(var_user_ask)
#     var_resp = mth_ask_for_response(str(var_user_ask))
#     #print(var_resp['message']['content'])
#     var_mouth.say(str(var_resp['message']['content']))
#     var_mouth.runAndWait()