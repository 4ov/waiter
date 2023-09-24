from pygame import mixer
import time
from consts import say_map
import sys
from sutil import wait_key


def say(message: str) -> int:
    mixer.init()
    parts = message.split()
    for part in parts:
        if part in ["c", "w", "a"]:
            mixer.music.load(say_map[part])
            mixer.music.play()
            time.sleep(0.75 if part == "a" else 2)
        else:
            int_part = int(part)
            if (int_part <= 9):
                mixer.music.load(say_map[part])
                mixer.music.play()
                time.sleep(0.75)
            elif int_part > 9 and int_part <= 19:
                mixer.music.load(say_map[part])
                mixer.music.play()
                time.sleep(2)
            else:
                ones = int_part % 10
                tens = int_part // 10 % 10 * 10
                hnds = int_part // 100 % 10 * 100
                thnds = int_part // 1000 % 10 * 1000
                # for nums between 11 and 19
                ones_tens = ones + tens

                if thnds > 0:
                    mixer.music.load(say_map[str(thnds)])
                    mixer.music.play()
                    time.sleep(1.75)
                if hnds > 0:
                    if thnds > 0:
                        say("a")
                    mixer.music.load(say_map[str(hnds)])
                    mixer.music.play()
                    time.sleep(1)
                if (ones > 0 and not (ones_tens >= 11 and ones_tens <= 19)):
                    say("a")
                    say(str(ones))

                if tens > 0:
                    say("a")
                    sleeping = 1
                    if (ones_tens >= 11 and ones_tens <= 19):
                        mixer.music.load(say_map[str(ones_tens)])
                        sleeping = 1.75
                    else:
                        mixer.music.load(say_map[str(tens)])
                    mixer.music.play()
                    time.sleep(sleeping)
                # x_0 = x % 10
                # x_1 = x // 10 % 10 * 10


# c_number = 10
# while True:
#     try:
#         key = wait_key()
#         if (key == "+"):
#             say(f"c {c_number} w 1")
#             c_number += 10
#         elif key == "i":
#             say(input("custom message: "))
#     except KeyboardInterrupt:
#         print("exitting")
#         exit(0)


say(" ".join(sys.argv[1:]))
