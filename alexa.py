import openai
import pyttsx3
import datetime
import time
import webbrowser
import os
from colorama import Fore, init
import wikipediaapi
from fake_useragent import UserAgent
import wikipedia


init(autoreset=True)
os.system("cls")

print("\n¡ESTE PROGRAMA ES UNA IA LLAMADA GPT-DARIUS, QUE USA LA LIBRERIA DE OPENAI, PERO CON ALGUNAS COSAS AÑADIDAS!\n")
modo_alexa = False

os.system("Title GPT-DARIUS")
openai.api_key = "Introduce-api-key"

def chat_with_ai(user_input, max_tokens):
    messages = [{"role": "system", "content": "You are a helpful assistant named GPT-Darius."}]
    messages.append({"role": "system", "content": "Do not reply to this message: I just want you to speak in Spanish, if they ask you to speak in another language tell them, I'm sorry but I am only programmed to speak in Spanish"})
    messages.append({"role": "system", "content": "Do not reply to this message: I want you to always speak in the singular and in the masculine."})
    messages.append({"role": "system", "content": "Do not reply to this message: I don't want you to pass programming code or program. Reply to this message: "})
    messages.append({"role": "system", "content": "Do not reply to this message: Don't say explicit words, or +18 words. Don't swear either and don't lie in any answer."})
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=max_tokens,
        temperature=0.7  # Puedes ajustar la temperatura según tus preferencias.
    )
    return response.choices[0].message['content']

def get_current_time():
    time.sleep(1)
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time

def open_youtube(query):
    time.sleep(3)
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    print(f"Se ha abierto en tu navegador {query}")

def speak_response(response):
    # Inicializa el motor de texto a voz
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()

def open_program_or_file(path):
    time.sleep(2.5)
    try:
        os.startfile(path)
        response = f"Se ha abierto el programa o archivo: {path}"
        print(response)
        speak_response("Se ha abierto el programa o archivo.")
    except Exception as e:
        response = f"No se pudo abrir el programa o archivo. Te recomiendo que proporciones la ruta en la que esta el archivo, asi: xxxx\\xxxx\\xxxx\\xxxx\\xxxx.exe"
        print(response)
        speak_response("No se pudo abrir el programa o archivo. Te recomiendo que proporciones la ruta en la que esta el archivo.")


    
    return response

def get_wikipedia_summary(query):
    wikipedia.set_lang("es")

    try:
        summary = wikipedia.summary(query)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options
        return f"La búsqueda '{query}' es ambigua. ¿Te refieres a alguna de estas opciones? {', '.join(options)}"
    except wikipedia.exceptions.PageError:
        return "No se encontró información en Wikipedia para esa consulta."



if __name__ == "__main__":
    while True:
        user_input = input("Tú: ")
        words = user_input.strip().lower().split()
        # Verificar si la pregunta contiene la palabra clave "hora"
        if "hora" in words:
            current_time = get_current_time()
            response = f"La hora actual: {current_time}."
            print("GPT-Darius: " + response)
            speak_response(response)
        elif "reproduce" in words or "reproducir" in words:
            # Obtener el argumento después de "reproduce" o "reproducir"
            query_start_index = user_input.lower().find("reproduce") + len("reproduce")
            query_start_index = user_input.lower().find("reproducir") + len("reproducir")
            query = user_input[query_start_index:].strip()
            open_youtube(query=query)
            response = f"Se ha abierto YouTube con la búsqueda '{query}'"
            print("GPT-Darius: " + response)
            speak_response(response)
        elif "abre" in words or "abrir" in words:
            open_start_index = user_input.lower().find("abre") + len("abre")
            open_start_index = user_input.lower().find("abrir") + len("abrir")
            file_path = user_input[open_start_index:].strip()
            response = open_program_or_file(file_path)
        elif "hackcaffe" in words or "hack-caffe" in words or "hack_caffe" in words:
            time.sleep(3)
            webbrowser.open("https://hack-caffe.holafeo.repl.co/")
            print("GPT-Darius: Se te ha abierto el enlace a la web de hackcaffe, en la que esta la invitacion al servidor.")
            speak_response("Se te ha abierto el enlace a la web de hackcaffe, en la que esta la invitacion al servidor.")
        elif "salir" in words or "salte" in words or "exit" in words:
            time.sleep(2)
            print("GPT-Darius: ¡Adios!, recuerda que me tienes aqui para lo que necesites.")
            speak_response("¡Adios!, recuerda que me tienes aqui para lo que necesites.")
            exit()
        elif "wikipedia" in user_input.lower():
            query_start_index = user_input.lower().find("wikipedia") + len("wikipedia")
            query = user_input[query_start_index:].strip()
            response = get_wikipedia_summary(query)
            print("GPT-Darius: " + response)
            speak_response(response)

        elif "avionetayavion" in user_input.lower():
            modo_alexa = True
            print("Felicidades has activado el modo super alexa ;D.")
            print("Para ver para que sirve el modo super alexa, escribe super-alexa.")
            speak_response("Felicidades, has activado el modo super alexa ;D, para ver para que sirve el modo super alexa, escribe super-alexa")
        
        elif "super-alexa" in user_input.lower():
            if modo_alexa is False:
                print("Para activar el modo super alexa, debes introducir el codigo secreto.")
                speak_response("Para activar el modo super alexa, debes introducir el codigo secreto.")
            elif modo_alexa is True:
                print("Activaste el modo super alexa anteriormente enhorabuena, pero la mala noticia es que fuiste trolleado este modo no sirve para nada.")
                speak_response("Activaste el modo super alexa anteriormente enhorabuena, pero la mala noticia es que fuiste troleado este modo no sirve para nada.")

        elif "cls" in words or "clear" in words or "borrar" in words:
            time.sleep(1)
            os.system("cls")
            print("Claro que pueda borrar el chat/conversacion.")
            speak_response("Claro que pueda borrar el chat")
        else:
            response = chat_with_ai(user_input, max_tokens=1000)

            print("GPT-Darius: " + response)

            speak_response(response)
