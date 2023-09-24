from consts import chunks
from gtts import gTTS, lang
import time
from os import path


for k, v in chunks.items():
    if not path.isfile(f"chunks/{k}.mp3"):
        mytext = v
        language = 'ar'
        myobj = gTTS(text=mytext, lang=language, slow=False, tld="ad")
        myobj.save(f"chunks/{k}.mp3")
        time.sleep(0.25)
        print(f"generated {k}")
print("done ;)")
