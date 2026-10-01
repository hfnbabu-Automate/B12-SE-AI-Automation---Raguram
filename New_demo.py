import subprocess
import time
import pyautogui

print("Step 1: Open the Chrome browser...")

subprocess.Popen(["open", "-a", "Google Chrome"])
time.sleep(3)

# Bring Chrome to the front
subprocess.run([
    "osascript",
    "-e",
    'tell application "Google Chrome" to activate'
])

time.sleep(2)

print("Step 2: Go to the website...")

pyautogui.hotkey("command", "l")
time.sleep(0.5)

pyautogui.write("https://www.accuweather.com/en/in/chennai/206671/hourly-weather-forecast/206671", interval=0.03)
time.sleep(1)
pyautogui.press("enter")
time.sleep(5)
print("Step 3: Copy the full date of the website")
pyautogui.hotkey('command', 'a', interval=0.1)
time.sleep(1)
pyautogui.hotkey('command', 'c', interval=0.1)
time.sleep(1)
print("Step 4: Open the text editor and paste the data")
pyautogui.hotkey('command', 'Space', interval=0.1)
time.sleep(1)
pyautogui.write('textedit', interval=0.15)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('command', 'v', interval=0.15)
time.sleep(2)
