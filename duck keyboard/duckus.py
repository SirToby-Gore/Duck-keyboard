import os, random, playsound, multiprocessing, keyboard

files = [f for f in os.listdir() if "mp3" == f[-3:]]

def play_sound():
    playsound.playsound(random.sample(files, 1)[0])

def check_key():
    while True:
        if keyboard.read_key() not in ["backspace","left windows", "ctrl", "delete"]:
            play_sound()

multiprocessing.Process(target=check_key())