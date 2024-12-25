from ollama import chat
from ollama import ChatResponse


import pyttsx3
var_mouth = pyttsx3.init()
var_mouth.setProperty('rate' , 150)
var_mouth.say(" I am working properly and everything is good 1 2 3 4 5 6 ")
var_mouth.runAndWait()



voices = var_mouth.getProperty('voices') # List available voices 
for index, voice in enumerate(voices): 
    #if 'english' in voice.name.lower():
    print(f"Voice {index}: {voice.name}, ID: {voice.id}")
    var_mouth.setProperty('voice', voice.id)
    var_mouth.say(" Hello everyone")
    var_mouth.runAndWait()


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
#     var_ear.adjust_for_ambient_noise(var_mic,duration = 0.2)
#     audio_data = var_ear.listen(var_mic) 
#     print("Recognizing...") 
#     try: 
#         text = var_ear.recognize_google(audio_data) 
#         print(f"Recognized text: {text}") 
#     except sr.UnknownValueError: 
#         print(" could not understand audio") 
#     except sr.RequestError as e: 
#         print(f" error; {e}")



# for i in range(5):
#     var_user_ask = input("--->>> : ")
#     var_user_ask = 'Respond in one sentence .'+ str(var_user_ask)
#     var_resp = mth_ask_for_response(str(var_user_ask))
#     #print(var_resp['message']['content'])
#     var_mouth.say(str(var_resp['message']['content']))
#     var_mouth.runAndWait()