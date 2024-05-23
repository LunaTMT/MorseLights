import time
import gpiozero

"""
inter element gap: 1 time unit
for example: letter: B  = -...      "- . . ."
each has an inter element gap

inter-letter gap: 3 time units      A _ _ _ B _ _ _ C

inter-word gap: 7 time units    ( H___E___L___L___O ) _______ ( W___O___R___L___D )

"""

text_to_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

string = input("Please enter text to convert to morse code : ").upper()



led = gpiozero.LED(17);

words = string.split()
letters = [c for word in words for c in word]

print(words)
print(letters)

morse = []
for word in words:
    for c in word:
        morse += (m for m in text_to_morse.get(c, ''))
        morse.append(3/10)
    morse.append(7/10)

for item in morse:
    if type(item) is int:
        time.sleep(item)
    else:
        led.on()
        if item == "-":
            time.sleep(1.5/10)
        else:
            time.sleep(0.5/10)
        led.off()
        time.sleep(1/10)

