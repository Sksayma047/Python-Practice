import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("I will speak this text")
engine.runAndWait()


string = input("Enter you string")
for ch in string.lower():
    if ch in "aeiou":
        count += 1
print("Number of vowels is: ", count)

