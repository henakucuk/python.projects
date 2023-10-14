from gtts import gTTS
from playsound import playsound

import os
tts = gTTS(text="Good Morning",lang="en") #lang ı tr yaparsak türkçe olur good morning yerine selamlar diyebiliriz
tts.save("deneme.mp3")
os.system("mpg321 deneme.mp3")
playsound(".\deneme.mp3")
