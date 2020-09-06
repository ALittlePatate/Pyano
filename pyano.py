import sys, os, getopt, time
from pygame import mixer
from pynput.keyboard import Key, Listener

mixer.init()
file_content = []
opened_file_content = []
record = False

def play(key) :
    mixer.music.load('sounds/'+key+'.mp3')
    mixer.music.play()

def main(argv) :
    global opened_file_content
    tempo = 25
    try:
        opts, args = getopt.getopt(argv,"hi:t:o:",["tempo=","open="])
    except getopt.GetoptError:
        print('python pyano.py -t <tempo> -o <file to open>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Usage :")
            print('python pyano.py -t <tempo> -o <file to open>')
            sys.exit()

        if opt in ("-t", "--tempo") :
            tempo = float(arg)

        if opt in ("-o", "--open"):
            mixer.init()
            with open("records/"+arg+".pyano", "r") as file_to_open :
                opened_file_content_str = file_to_open.read()
                opened_file_content = opened_file_content_str.split(",")
                file_to_open.close()
            
            a = 0
            while True :
                try :
                    mixer.music.load('sounds/'+opened_file_content[a]+'.mp3')
                    mixer.music.play()
                except Exception as e :
                    sys.exit()
                time.sleep(tempo)
                a = a + 1
    
def rec(key) :
    global file_content
    global record

    key = str(key)
    key = key.replace("'", "")

    if key == "&" or key == "1":
        key = "1"
        play(key)
    elif key == "é" or key == "2":
        key = "2"
        play(key)
    elif key == '"' or key == "3":
        key = "3"
        play(key)
    elif key == '""' or key == "4":
        key = "4"
        play(key)
    elif key == '(' or key == "5":
        key = "5"
        play(key)
    elif key == '-' or key == "6":
        key = "6"
        play(key)
    elif key == 'è' or key == "7" :
        key = "7"
        play(key)
    elif key == '_' or key == "8":
        key = "8"
        play(key)
    elif key == 'ç' or key == "9":
        key = "9"
        play(key)
    elif key == 'à' or key == "0":
        key = "0"
        play(key)

    if key == 'Key.f7' :
        print("recording stoped !")
        try :
            a=input("Press [ENTER] to continue...")
        except :
            pass
        name = input("Name your recording : ")
        with open('records/'+name+'.pyano', 'w') as rec_file :
            rec_file.write(','.join(file_content))
            rec_file.close()
        print("File saved !")
        os.system("cls")
        record = False
        #sys.exit()
    
    if key != "Key.f6" :
        if key != "Key.f7" :
            file_content.append(key)

def on_press(key) :
    global record
    global listener

    #On garde juste le nom de la touche, et  on supprime les " "
    key = str(key)
    key = key.replace("'", "")
    
    if key == 'Key.f6' :
        print("starting recording")
        record = True

    if record == True :
        rec(key)

    if key == "&" :
        key = "1"
        play(key)
    elif key == "é" :
        key = "2"
        play(key)
    elif key == '"' :
        key = "3"
        play(key)
    elif key == '""' :
        key = "4"
        play(key)
    elif key == '(' :
        key = "5"
        play(key)
    elif key == '-' :
        key = "6"
        play(key)
    elif key == 'è' :
        key = "7"
        play(key)
    elif key == '_' :
        key = "8"
        play(key)
    elif key == 'ç' :
        key = "9"
        play(key)
    elif key == 'à' :
        key = "0"
        play(key)
    elif key == 'Key.f8' :

        play(key)

if __name__ == "__main__":
   main(sys.argv[1:])

with Listener(on_press=on_press) as listener :
    listener.join()