# install an external package module and use to perform an operarion in your intrest
import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("hey my name is Bishesh ")
engine.runAndWait()