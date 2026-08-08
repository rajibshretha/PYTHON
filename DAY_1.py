import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"
engine.setProperty('rate', 190) 
engine.say("no he is afraid of light ")
engine.runAndWait()
print("Day 1 ::" )
