import os
import platform

op_system = platform.system()
file = None
words = None

elif:
    file = open("/usr/share/dict/words", "r")
    words = file.readlines()
    file.close()