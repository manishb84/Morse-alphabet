import winsound
import time

frequency = 1000
MorseCode={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.",
           "g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..",
           "m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.",
           "s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-",
           "y":"-.--","z":"--.."," ":" "}
while(True):
	Text = input("Enter your Text: ")
	Text = Text.lower()
	Coded_Text = ''

	for c in Text:
		Coded_Text = Coded_Text + " " + MorseCode[c]
		
	print(Coded_Text)

	for s in Coded_Text:
		if s == ".":
			winsound.Beep(frequency, 100)
		elif s == "-":
			winsound.Beep(frequency, 300)
		else:
			time.sleep(.5)
		time.sleep(.1)
