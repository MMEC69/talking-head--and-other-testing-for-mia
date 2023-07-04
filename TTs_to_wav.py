#importing the required module
import pyttsx3

#creating a string
string = "Hi, how are you doing"

#intialize the pyttsx3 engine
engine = pyttsx3.init()

#command to speak given string
#engine.say(string)

#Now with the installed ffmeg we can save this file to anyformat in here ill do it for ,mp3 and .wav
engine.save_to_file(string, 'speech.wav')

#wait until above command is not finished
engine.runAndWait()