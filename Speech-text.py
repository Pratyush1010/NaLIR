import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)  # here
	print('Say Something')
	audio=r.listen(source,timeout=3)

try:
	print('Answer:\n' + r.recognize_google(audio))

except:
	pass
  
  
  #Reference : https://www.geeksforgeeks.org/speech-recognition-in-python-using-google-speech-api/
