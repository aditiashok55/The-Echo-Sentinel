import pyautogui
import webbrowser
import time
import speech_recognition as sr

def search_on_chatgpt(search_query):
    base_url = "https://www.chatgpt.com"
    final_url = base_url
    webbrowser.open(final_url)
    time.sleep(3)  # Adjust this delay based on your system's loading time
    pyautogui.click(1000, 990)
    time.sleep(1)  # Delay before typing
    pyautogui.write(search_query, interval=0.1)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.click(1620, 63)

def search_with_voice():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        search_query = query.lower()

        if 'jarvis play' in search_query:
            webbrowser.open("https://www.youtube.com")
            time.sleep(2)
            pyautogui.click(600, 160)
            time.sleep(4)
            pyautogui.typewrite(search_query)
            pyautogui.press('enter')
            time.sleep(3)
            pyautogui.click(600, 390)
        elif 'i am bored jarvis' in search_query:
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.write('valorant')
            time.sleep(2)
            pyautogui.press('enter')
        elif 'jarvis run' in search_query:
            pyautogui.press('win')
            time.sleep(2)
            pyautogui.write("spotify")
            time.sleep(2)
            pyautogui.click(596, 370)
            time.sleep(3)
            pyautogui.click(36, 189)
            command_index = search_query.find(' ', search_query.find(' ') + 1)
            if command_index != -1:  # Check if there's a second space in the command
                search_query = search_query[command_index + 1:]  # Extract command after the second word
                pyautogui.write(search_query)
        elif 'jarvis self destruct' in search_query:
            pyautogui.hotkey('winleft')  # Open Windows menu
            time.sleep(1)  # Adjust the delay if necessary
            pyautogui.click(1260,957)  # Search for Shut down
            time.sleep(3) 
            pyautogui.click(1255,875)
        else:
            search_on_chatgpt(search_query)

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError:
        print("Sorry, the service is unavailable. Please try again later.")

search_with_voice()